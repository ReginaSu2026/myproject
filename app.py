# uv add streamlit 
# streamlit run app.py
import streamlit as st


st.title("用streamlit 架站")

st.header("CI/CD 自動化部署的含意")
st.write("Continuous Integration (CI) 和 Continuous Delivery/Deployment (CD) 是現代軟體開發中常用的實踐方法。CI/CD 的目標是提高軟體開發的效率和質量，通過自動化流程來減少人為錯誤，並加快軟體的交付速度。")
st.write("CI/CD 是一種軟體開發方法，旨在自動化軟體的構建、測試和部署過程。CI（持續整合）指的是將代碼變更自動集成到主分支中，並進行自動化測試，以確保代碼的穩定性。CD（持續交付/部署）則是將通過測試的代碼自動部署到生產環境中，從而加快軟體的交付速度。")
st.write("工程師在地端/本機開發好功能測試完成沒問題後 上傳到 GitHub 上，GitHub Actions 會自動幫你做 CI/CD 的流程，將程式碼自動部署到雲端伺服器上，讓使用者可以直接透過網頁使用你的功能。")

#左側選單
#st.sidebar.title("選單")
#st.sidebar.write("這是選單的內容")

with st.sidebar:
    st.header("選單標題")
    st.write("選單內容")
    st.button("按鈕A")
    st.button("按鈕K")
  

#網頁 footer 聯絡資訊
st.markdown("---")
st.header("關於我")
st.text("聯絡資訊: email: mymis168@gmail.com")