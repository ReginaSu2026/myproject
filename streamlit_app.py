import streamlit as st

st.set_page_config(
    page_title="Regina Su | Data Engineer & Performance Analyst",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Noto Sans TC', sans-serif;
        background: linear-gradient(180deg, #f5f1eb 0%, #f8f8f4 100%);
        color: #1d2a26;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        background: linear-gradient(135deg, #19332d 0%, #224f47 40%, #2f6d5c 100%);
        border-radius: 20px;
        padding: 2rem 2.2rem;
        box-shadow: 0 18px 40px rgba(25, 51, 45, 0.18);
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        color: #f6f1e8 !important;
        margin-bottom: 0.35rem;
        font-size: 2.6rem;
        line-height: 1.2;
    }

    .hero p {
        color: rgba(246, 241, 232, 0.88);
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
    }

    .section-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #18342f;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    .card {
        background: rgba(255,255,255,0.8);
        border: 1px solid rgba(24,52,47,0.08);
        border-radius: 18px;
        padding: 1.2rem 1.2rem;
        box-shadow: 0 8px 22px rgba(15,29,27,0.04);
        height: 100%;
    }

    .metric-box {
        background: linear-gradient(135deg, rgba(24,52,47,0.98), rgba(47,109,92,0.93));
        border-radius: 18px;
        padding: 1.2rem 1rem;
        color: #f7f3ee;
        text-align: center;
        height: 100%;
    }

    .metric-box .label {
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        opacity: 0.8;
    }

    .metric-box .value {
        font-size: 2rem;
        font-weight: 800;
        margin: 0.25rem 0;
    }

    .metric-box .sub {
        font-size: 0.8rem;
        opacity: 0.88;
    }

    .skill-card {
        background: rgba(255,255,255,0.8);
        border: 1px solid rgba(24,52,47,0.08);
        border-radius: 14px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.8rem;
    }

    .skill-header {
        display: flex;
        justify-content: space-between;
        font-weight: 700;
        color: #18342f;
        margin-bottom: 0.5rem;
    }

    .progress-bar {
        background: #e7e0d5;
        border-radius: 999px;
        overflow: hidden;
        height: 0.7rem;
    }

    .progress-fill {
        background: linear-gradient(90deg, #1c4c45 0%, #4d9a86 100%);
        height: 100%;
        border-radius: 999px;
    }

    .tag {
        display: inline-block;
        background: #eaf3f1;
        color: #1f4b42;
        border-radius: 999px;
        padding: 0.38rem 0.7rem;
        font-size: 0.76rem;
        margin: 0.18rem 0.3rem 0.18rem 0;
        font-weight: 600;
    }

    .timeline {
        padding-left: 1rem;
        border-left: 3px solid rgba(25, 51, 45, 0.2);
    }

    .timeline-item {
        position: relative;
        margin-bottom: 1.2rem;
        padding-left: 1.1rem;
    }

    .timeline-item:before {
        content: "";
        position: absolute;
        left: -1.2rem;
        top: 0.25rem;
        width: 0.7rem;
        height: 0.7rem;
        border-radius: 50%;
        background: #224f47;
        box-shadow: 0 0 0 3px rgba(34,79,71,0.12);
    }

    .timeline-year {
        color: #2d6b60;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }

    .portfolio-card {
        background: rgba(255,255,255,0.8);
        border: 1px solid rgba(24,52,47,0.08);
        border-radius: 16px;
        padding: 1rem 1rem 0.85rem;
        height: 100%;
    }

    .portfolio-card h4 {
        margin: 0 0 0.5rem 0;
        color: #18342f;
    }

    .portfolio-card p {
        margin: 0 0 0.65rem 0;
        color: #4d5b57;
        line-height: 1.6;
    }

    a {
        color: #214f48;
        text-decoration: none;
    }

    .footer-box {
        background: #163a35;
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        color: #f9f5f0;
        margin-top: 1.8rem;
    }

    .stSidebar {
        background: rgba(245, 241, 235, 0.7);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


PROFILE = {
    "name": "Regina Su",
    "title": "Data Engineer & Performance Marketing Analyst",
    "summary": "專精於 Google 廣告與跨平台廣告數據分析，將數據工程、資料建模與廣告投放策略結合，提升效益、優化成效與透視各平台的獲客與投資報酬。",
    "email": "pythonsu2026@gmail.com",
    "location": "Taiwan",
    "portfolio": "https://reginasu0804.neocities.org/",
}

SKILLS = [
    ("Google Ads / GA4 / GTM", 95),
    ("跨平台廣告數據整合", 94),
    ("SQL / Python / 資料清洗", 92),
    ("Data Warehouse / BI Dashboard", 90),
    ("廣告投資優化策略", 88),
    ("數據工程 ETL / 自動化報表", 86),
]

TOOLS = [
    "Google Ads", "GA4", "Looker Studio", "BigQuery", "SQL", "Python",
    "Pandas", "DBT", "GCP", "Tableau", "Meta Ads", "TikTok Ads",
    "LINE Ads", "YAHOO Ads", "Excel", "Power BI"
]

EXPERIENCE = [
    {
        "period": "2024 - Present",
        "title": "數據工程師 / 廣告分析師",
        "company": "跨平台電商與品牌行銷團隊",
        "details": [
            "建立 Google Ads、Meta、TikTok、Yahoo 等平台的資料整合流程，串接 API 與 GA4 事件資料，形成一致的效能看板。",
            "設計 SQL 與 Python ETL 流程，處理廣告點擊、轉換、重複計費與歸因資料，提升數據可信度與分析效率。",
            "將廣告花費、CTR、CVR、CPA、ROAS、LTV 等指標標準化，支援實時投放優化與跨平台投資分配。",
            "依據 A/B 測試結果與數據分群，協助優化素材、關鍵字、受眾與投放時段。",
        ],
    },
    {
        "period": "2021 - 2024",
        "title": "數位行銷企劃 / 數據分析",
        "company": "多品牌電商與網路行銷公司",
        "details": [
            "負責行銷開口、Google 廣告、SEO 關鍵字、社群與電商通路整合，追蹤 ROAS 與獲客成本。",
            "協同設計與文案團隊完成產品內容、廣告素材與轉換路徑優化，提升媒體效率。",
            "整理平台數據並製作報表，協助管理階層理解購物車轉換、流量來源、消費行為與成長機會。",
        ],
    },
    {
        "period": "2014 - 2021",
        "title": "數位行銷與品牌設計",
        "company": "網路電商 / 代理商 / 品牌行銷",
        "details": [
            "以品牌、內容、平面與數位行銷整合方向推動案件，包含社群行銷、電商通路、廣告文案與素材製作。",
            "執行廣告投放與 GA 分析，熟悉品牌曝光、成效追蹤與行銷轉換的優化流程。",
            "跨不同產業接觸行銷與購物導流策略，累積多平台數據實務經驗。",
        ],
    },
]

PROJECTS = [
    {
        "title": "Google Ads 成效優化儀表板",
        "summary": "彙整不同廣告群組的成本、點擊、轉換、CPA、ROAS 與品質分數，快速辨識低效關鍵字與高潛力素材。",
        "metrics": ["ROI 提升 28%", "CPA 降低 22%", "週報表自動化"],
    },
    {
        "title": "跨平台廣告資料整合分析",
        "summary": "串接 Google Ads、Meta Ads、TikTok Ads 與 GA4 資料，建立標準化維度，支援每月投資報酬與廣告來源比較。",
        "metrics": ["數據一致性提升 35%", "投放決策週期縮短 50%", "跨平台歸因分析"],
    },
    {
        "title": "BI Dashboard 與自動化報表",
        "summary": "以 Looker Studio / Tableau 為主，製作可視化 KPI 看板，讓行銷團隊能夠立即掌握流量、轉換與成效變化。",
        "metrics": ["報表更新自動化", "團隊決策效率提升", "告警與異常監控"],
    },
]


def render_skill_block(label, value):
    st.markdown(
        f"""
        <div class="skill-card">
            <div class="skill-header">
                <span>{label}</span>
                <span>{value}%</span>
            </div>
            <div class="progress-bar"><div class="progress-fill" style="width:{value}%"></div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with st.sidebar:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"## {PROFILE['name']}")
    st.markdown(f"### {PROFILE['title']}")
    st.markdown("---")
    st.markdown(f"📧 {PROFILE['email']}")
    st.markdown(f"📍 {PROFILE['location']}")
    st.markdown(f"🔗 [Portfolio]({PROFILE['portfolio']})")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Quick Summary")
    st.write(PROFILE['summary'])

    st.markdown("### Core Stack")
    for tool in TOOLS:
        st.markdown(f"<span class='tag'>{tool}</span>", unsafe_allow_html=True)


st.markdown(
    """
    <div class="hero">
        <h1>Yes! I am a Data Engineer & Performance Marketing Analyst</h1>
        <p>專精於 Google 廣告與跨平台廣告數據分析，將數據工程、廣告投放與商業決策統整為一個完整的成效閉環。</p>
        <p>擅長把流量、轉換與投資回報轉成可執行策略，讓品牌在不同媒體平台中持續成長。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(
        """
        <div class="metric-box">
            <div class='label'>Google Ads</div>
            <div class='value'>8+</div>
            <div class='sub'>years of performance optimization</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="metric-box">
            <div class='label'>Cross-platform</div>
            <div class='value'>5+</div>
            <div class='sub'>media channels integrated</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="metric-box">
            <div class='label'>ROAS</div>
            <div class='value'>3x+</div>
            <div class='sub'>optimization case results</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col4:
    st.markdown(
        """
        <div class="metric-box">
            <div class='label'>Automation</div>
            <div class='value'>90%</div>
            <div class='sub'>reporting workflow efficiency</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
left_col, right_col = st.columns([2, 1])
with left_col:
    st.markdown(
        """
        <div class="card">
            <p>我是一位結合行銷與數據工程能力的分析者，從廣告投放、數據清洗、報表建置到歸因分析與優化策略，皆有實務經驗。</p>
            <p>在廣告領域中，我注重的不只是流量，而是如何從 Google Ads、Meta、TikTok、Yahoo 等平台的數據中找到真正能帶來成長的決策點。</p>
            <p>我擅長將 BI、ETL、SQL、Python 與廣告效能分析結合，建立可持續運作的數據流程，讓行銷、產品與管理面都能基於一致的數據做判斷。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right_col:
    st.markdown(
        """
        <div class="card">
            <strong>專長領域</strong>
            <p>• Google Ads / GA4 / GTM</p>
            <p>• 跨平台廣告數據分析</p>
            <p>• SQL / Python / Dashboard</p>
            <p>• ROAS / CPA / 成效優化</p>
            <p>• 數據工程與自動化報表</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-title">My Skills</div>', unsafe_allow_html=True)
skill_cols = st.columns(2)
for idx, (label, value) in enumerate(SKILLS):
    with skill_cols[idx % 2]:
        render_skill_block(label, value)

st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)
for item in EXPERIENCE:
    st.markdown(
        f"""
        <div class="card" style="margin-bottom: 1rem;">
            <div class="timeline-year">{item['period']}</div>
            <h3 style="margin-top: 0.2rem; margin-bottom: 0.4rem; color: #173a35;">{item['title']}</h3>
            <div style="font-weight:700; color:#335d56; margin-bottom: 0.6rem;">{item['company']}</div>
            <ul>
                {''.join(f'<li>{detail}</li>' for detail in item['details'])}
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-title">Case Studies</div>', unsafe_allow_html=True)
for project in PROJECTS:
    with st.container():
        st.markdown(
            f"""
            <div class="portfolio-card" style="margin-bottom: 1rem;">
                <h4>{project['title']}</h4>
                <p>{project['summary']}</p>
                <div>
                    {''.join(f"<span class='tag'>{metric}</span>" for metric in project['metrics'])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="section-title">Portfolio</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <p>作品涵蓋：網站規劃、數位行銷、廣告投放、品牌視覺、攝影與電子商務內容策略。</p>
        <p>我整合文案、設計與數據分析的能力，協助品牌從曝光到成效轉換實現完整的行銷閉環。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="footer-box">
        <strong>Contact</strong><br>
        Email: pythonsu2026@gmail.com<br>
        Focus: Google 廣告 • 跨平台分析 • 數據工程 • 效益優化
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("© 2026 Regina Su • Data Engineer & Performance Marketing Analyst")
