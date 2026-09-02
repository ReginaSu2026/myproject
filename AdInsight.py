from pathlib import Path
import streamlit as st

#Layout (A) Main
st.title("跨平台廣告數據分析")
st.divider()
logo_path = Path(__file__).parent / "image" / "logo.jpg"
if logo_path.exists():
    st.logo(str(logo_path), size="large")

col1, col2 = st.columns(2)
with col1:
    st.text_input("請輸入您的姓名", key="name")    

with col2:
    st.text_input("請輸入您的電子郵件", key="email")

c1 = st.container()
with c1:
    st.write(
        "跨平台廣告數據分析01：跨平台廣告數據分析02，"
        "在多通路行銷時代，跨平台廣告數據分析是企業提升投資報酬率（ROI）與精準布局的核心策略。"
        "品牌往往同時在 Google、Meta、TikTok、LINE 等多個管道投放廣告，但各平臺數據獨立且歸因標準不一，"
        "容易導致數據孤島與預算浪費。\n\n"
        "跨平台數據分析的核心價值，在於將不同來源的點擊率、轉化率、顧客獲取成本（CAC）與顧客終身價值（LTV）等關鍵指標統整至單一儀表板。"
        "透過建立統一的歸因模型（Attribution Model），企業能清晰追蹤用戶從「受眾觸達」到「最終購買」的完整全通路路徑，"
        "精確評估各管道的真實貢獻度。\n\n"
        "此外，結合 AI 與自動化分析，團隊可實時發現高效益的廣告組合，並將預算自動挪移至表現優異的平台，"
        "擺脫傳統人工逐一調價的低效流程。掌控跨平台數據，不僅能大幅降低重複廣告觸達率，更能幫助企業以數據驅動決策，"
        "實現行銷預算效益最大化。"
    )

st.divider()
st.header("跨平台廣告數據分析")
st.image("./image/ad01.png", caption="跨平台廣告數據分析圖")
st.image("image/ad02.jpg", caption="YAHOO行動數據")

# Layout (B) Sidebar
with st.sidebar:
    with st.container():
        st.header("選單標題1")
        st.write("選單內容1")
        st.button("按鈕A1")
        st.button("按鈕K1")
    st.divider()
    with st.container():
        st.header("選單標題2")
        st.write("選單內容2")
        st.button("按鈕B")
        st.button("按鈕L")

# 任何不在 sidebar , footer 都是 Section A

# Layout (C) Footer
st.markdown("---")
st.header("關於我")
st.text("聯絡資訊: email:")

    