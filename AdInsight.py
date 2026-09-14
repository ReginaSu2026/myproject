import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. 頁面基本設定 (Page Configuration)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="BloomInsight | 電商與數位廣告數據洞察",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自訂 CSS 樣式 (注入行銷美學與玻璃擬態視覺)
st.markdown("""
<style>
    /* 主背景與整體字型 */
    .main {
        background-color: #f8fafc;
    }
    
    /* Hero Banner 區塊 */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 2.5rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }
    
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(135deg, #f43f5e 0%, #ec4899 50%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #94a3b8;
    }

    /* KPI 卡片樣式 */
    .kpi-card {
        background: white;
        padding: 1.2rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .kpi-title { font-size: 0.85rem; color: #64748b; font-weight: 600; }
    .kpi-value { font-size: 1.8rem; color: #0f172a; font-weight: 800; margin: 0.2rem 0; }
    .kpi-sub { font-size: 0.8rem; color: #10b981; font-weight: 600; }
</style>
""", unsafe_allow_allowed_html=True)

# -----------------------------------------------------------------------------
# 2. 模擬數據生成器 (Mock Data Generator)
# -----------------------------------------------------------------------------
@st.cache_data
def load_ad_data():
    """生成廣告成效模擬數據 (Google Ads & Meta Ads)"""
    dates = pd.date_range(start="2026-01-01", periods=90, freq="D")
    channels = ["Google Ads (Search)", "Google Ads (Display)", "Meta Ads (Instagram)", "Meta Ads (Facebook)"]
    
    data = []
    np.random.seed(42)
    for date in dates:
        for channel in channels:
            spend = np.random.uniform(500, 3000)
            impressions = spend * np.random.uniform(15, 40)
            clicks = impressions * np.random.uniform(0.015, 0.05)
            conversions = clicks * np.random.uniform(0.02, 0.08)
            revenue = conversions * np.random.uniform(800, 2500)
            data.append({
                "Date": date,
                "Channel": channel,
                "Spend": spend,
                "Impressions": impressions,
                "Clicks": clicks,
                "Conversions": conversions,
                "Revenue": revenue
            })
    df = pd.DataFrame(data)
    df["CTR"] = (df["Clicks"] / df["Impressions"]) * 100
    df["CVR"] = (df["Conversions"] / df["Clicks"]) * 100
    df["CPA"] = df["Spend"] / df["Conversions"]
    df["ROAS"] = df["Revenue"] / df["Spend"]
    return df

@st.cache_data
def load_rfm_data():
    """生成電商 RFM 顧客分群數據 (參考 Olist 數據架構)"""
    np.random.seed(101)
    n_customers = 500
    segments = ["高價值 VIP", "忠誠顧客", "潛力新客", "流失風險顧客", "沉睡顧客"]
    
    df = pd.DataFrame({
        "CustomerID": [f"CUST-{1000+i}" for i in range(n_customers)],
        "Recency": np.random.randint(1, 180, n_customers),        # 近一次消費天數
        "Frequency": np.random.randint(1, 15, n_customers),      # 消費頻率
        "Monetary": np.random.exponential(scale=1500, size=n_customers) + 200, # 消費金額
        "Segment": np.random.choice(segments, n_customers, p=[0.15, 0.25, 0.3, 0.2, 0.1])
    })
    return df

ad_df = load_ad_data()
rfm_df = load_rfm_data()

# -----------------------------------------------------------------------------
# 3. 側邊欄與個人品牌導覽 (Sidebar)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=400&q=80", use_column_width=True)
    st.title("🌸 BloomInsight")
    st.caption("Precision Insights. Blooming Performance.")
    
    st.markdown("---")
    page = st.radio("📌 請選擇分析模組：", ["📢 廣告成效與 ROAS 診斷", "🛒 電商 RFM 顧客價值分群", "👤 關於創作者與作品集"])
    
    st.markdown("---")
    st.markdown("### 🔗 個人作品集連結")
    st.markdown("👉 [Regina's Official Portfolio](https://reginasu0804.neocities.org/)", unsafe_allow_html=True)
    st.info("💡 深度分析電商與廣告數據，驅動商業成效綻放。")

# -----------------------------------------------------------------------------
# 4. 模組一：社群與 Google 廣告成效診斷 (Ad Analytics)
# -----------------------------------------------------------------------------
if page == "📢 廣告成效與 ROAS 診斷":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">社群與關鍵字廣告效益診斷室</div>
        <div class="hero-subtitle">整合 Google Ads 與 Meta Ads 跨渠道流量，精準分析 CPA、CVR 與 ROAS 最佳化分配。</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 篩選條件
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        selected_channels = st.multiselect("選擇廣告渠道：", ad_df["Channel"].unique(), default=ad_df["Channel"].unique())
    with col_f2:
        date_range = st.date_input("選擇日期區間：", [ad_df["Date"].min(), ad_df["Date"].max()])
        
    filtered_ad = ad_df[(ad_df["Channel"].isin(selected_channels)) & 
                        (ad_df["Date"] >= pd.to_datetime(date_range[0])) & 
                        (ad_df["Date"] <= pd.to_datetime(date_range[1]))]
    
    # KPI 指標列
    total_spend = filtered_ad["Spend"].sum()
    total_revenue = filtered_ad["Revenue"].sum()
    avg_roas = total_revenue / total_spend if total_spend > 0 else 0
    avg_cpa = total_spend / filtered_ad["Conversions"].sum() if filtered_ad["Conversions"].sum() > 0 else 0
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("總廣告花費 (Spend)", f"${total_spend:,.0f}")
    kpi2.metric("總帶動營收 (Revenue)", f"${total_revenue:,.0f}")
    kpi3.metric("整體廣告回報率 (ROAS)", f"{avg_roas:.2f} x", delta="目標 ROAS > 3.0")
    kpi4.metric("平均獲客成本 (CPA)", f"${avg_cpa:.1f}")
    
    st.markdown("---")
    
    # 圖表 1：各渠道 ROAS vs Spend 散佈圖 (診斷藍海素材)
    st.subheader("🎯 廣告渠道效益矩陣 (ROAS vs. 花費金額)")
    channel_summary = filtered_ad.groupby("Channel").agg({
        "Spend": "sum",
        "Revenue": "sum",
        "Conversions": "sum",
        "Clicks": "sum"
    }).reset_index()
    channel_summary["ROAS"] = channel_summary["Revenue"] / channel_summary["Spend"]
    channel_summary["CPA"] = channel_summary["Spend"] / channel_summary["Conversions"]
    
    fig_scatter = px.scatter(
        channel_summary, x="Spend", y="ROAS", size="Conversions", color="Channel",
        text="Channel", hover_data=["CPA"], size_max=40,
        title="各渠道 ROAS 與花費關係圖 (氣泡大小表示轉換數)"
    )
    fig_scatter.add_hline(y=3.0, line_dash="dash", line_color="red", annotation_text="目標 ROAS 門檻 (3.0)")
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # 圖表 2：每日 ROAS 走勢與渠道對比
    st.subheader("📈 每日 ROAS 趨勢追蹤")
    fig_line = px.line(filtered_ad, x="Date", y="ROAS", color="Channel", title="動態 ROAS 變化趨勢")
    st.plotly_chart(fig_line, use_container_width=True)

# -----------------------------------------------------------------------------
# 5. 模組二：電商 RFM 顧客價值分群 (RFM Customer Segmentation)
# -----------------------------------------------------------------------------
elif page == "🛒 電商 RFM 顧客價值分群":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">電商 RFM 顧客價值與營運分析</div>
        <div class="hero-subtitle">參考 Olist 數據模型，依據 Recency (近因)、Frequency (頻率) 與 Monetary (金額) 進行精準 CRM 客戶分群。</div>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI 列
    total_customers = len(rfm_df)
    vip_count = len(rfm_df[rfm_df["Segment"] == "高價值 VIP"])
    avg_monetary = rfm_df["Monetary"].mean()
    
    c1, c2, c3 = st.columns(3)
    c1.metric("總顧客數", f"{total_customers:,} 人")
    c2.metric("高價值 VIP 顧客數", f"{vip_count} 人", f"佔比 {(vip_count/total_customers)*100:.1f}%")
    c3.metric("平均顧客消費金額 (AOV)", f"${avg_monetary:,.1f}")
    
    st.markdown("---")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("👥 顧客分群人數比例")
        segment_counts = rfm_df["Segment"].value_counts().reset_index()
        segment_counts.columns = ["Segment", "Count"]
        fig_pie = px.pie(segment_counts, values="Count", names="Segment", hole=0.4,
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_right:
        st.subheader("💰 各客群平均消費貢獻度 (Monetary)")
        fig_bar = px.bar(rfm_df.groupby("Segment")["Monetary"].mean().reset_index(), 
                         x="Segment", y="Monetary", color="Segment",
                         text_auto='.2s', title="各分群平均客單價 ($)")
        st.plotly_chart(fig_bar, use_container_width=True)
        
    st.subheader("🔍 顧客分群 3D 視覺化 (Recency vs. Frequency vs. Monetary)")
    fig_3d = px.scatter_3d(rfm_df, x="Recency", y="Frequency", z="Monetary", color="Segment",
                           opacity=0.8, size_max=10, height=500)
    st.plotly_chart(fig_3d, use_container_width=True)

# -----------------------------------------------------------------------------
# 6. 模組三：個人簡歷與作品集連結 (About & Portfolio)
# -----------------------------------------------------------------------------
elif page == "👤 關於創作者與作品集":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">About Regina Su</div>
        <div class="hero-subtitle">Data Analyst & Digital Marketing Strategist</div>
    </div>
    """, unsafe_allow_html=True)
    
    col_bio, col_link = st.columns([2, 1])
    
    with col_bio:
        st.markdown("### 🌟 個人簡介")
        st.write("""
        跨足 **數位行銷** 與 **數據分析** 的實務工作者。
        擅長整合跨平台廣告（Google Ads / Meta Ads）與電商營運數據，透過 Python ETL 清洗資料，並搭配 Power BI / Streamlit 打造即時互動的商業決策戰情室。
        """)
        
        st.markdown("### 🛠 核心專業領域")
        st.markdown("""
        - **行銷成效最佳化**：廣告 ROAS 診斷、CPA 降本增效、A/B Testing 評估。
        - **商業智慧 (BI) 與視覺化**：Streamlit Web App 開發、Power BI / DAX 數據建模。
        - **電商數據分析**：RFM 顧客價值模型、購物籃分析、轉換漏斗優化。
        """)
        
    with col_link:
        st.markdown("### 🌐 個人官方作品集")
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0; text-align: center;">
            <p style="font-size: 1.1rem; font-weight: 700; color: #0f172a;">觀看完整視覺化作品集：</p>
            <a href="https://reginasu0804.neocities.org/" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #ec4899, #8b5cf6); color: white; padding: 12px 24px; border-radius: 30px; font-weight: 700; text-decoration: none; margin-top: 10px;">前往 Neocities 作品集 🚀</a>
        </div>
        """, unsafe_allow_html=True)
