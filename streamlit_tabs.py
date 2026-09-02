from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent

def safe_image(relative_path: str, caption: str):
    image_path = BASE_DIR / relative_path
    if image_path.exists():
        st.image(str(image_path), caption=caption)
    else:
        st.info(f"圖片不存在：{relative_path}")

st.title("PowerBI 簡報說明")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["肺癌男女分布", "依家族史與吸菸史分布", "依治療方式分布", "依年齡分布", "依病理分布"])

with tab1:
    st.header("肺癌男女分布")
    safe_image("image/ad01.png", "肺癌男女分布圖")

with tab2:
    st.header("依家族史與吸菸史分布")
    safe_image("image/ad02.jpg", "依家族史與吸菸史分布圖")

with tab3:
    st.header("Power BI 操作流程示範")
    st.video("https://www.youtube.com/watch?v=9RcQUhlIb_Y", format="video/mp4", start_time="2 m 30s", end_time="10 m", autoplay=True, muted=True)
    # st.video("images/PowerBI操作流程示範.mp4", format="video/mp4", start_time=0)