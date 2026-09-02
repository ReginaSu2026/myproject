import streamlit as st

#Layout (A) Main
st.title("飆股特徵全解析")
st.divider()


col1, col2 = st.columns(2)
with col1:
    st.text_input("請輸入您的姓名", key="name")    

with col2:
    st.text_input("請輸入您的電子郵件", key="email")

c1 = st.container()
with c1:
    st.write("飆股特徵全解析：從籌碼與型態抓出翻倍潛力股。想要在股市中精準捕捉暴漲飆股，關鍵在於學會觀察籌碼面與技術面的共振訊號。當一檔股票在低檔盤整許久，突然出現成交量異常放大，且伴隨法人（外資、投信）或主力大戶連續買超時，往往就是發動的前兆。此時技術型態通常會呈現突破長期均線（如季線、半年線）或向上突破箱型整理區間。透過觀察主力籌碼集中度與K線型態，能在股價剛發動的第一時間順勢卡位，提高資金運用效率。")

st.divider()
st.header("掌握飆股起漲密碼")
st.image("image/ad01.png", caption="飆股分析", width=700)

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

    