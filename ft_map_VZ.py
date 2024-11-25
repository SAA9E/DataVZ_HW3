import streamlit as st


st.title("🌏 대한민국 출산율 지도")
st.write("🔍 통계청「인구동향조사-출생편」")
st.write("🔍 연령별 출산율 및 합계출산율(행정구역별)")

# 지도 출력

# 저장된 지도 HTML 파일 경로
ft_map_path = "C:/Users/hyunji/Documents/hongik_2024/2024-2/DataVZ/Streamlit/HW3_elements/ft_map.html"
ft_map_plus = "C:/Users/hyunji/Documents/hongik_2024/2024-2/DataVZ/Streamlit/HW3_elements/ft_map_plus.html"
ft_map_heat = "C:/Users/hyunji/Documents/hongik_2024/2024-2/DataVZ/Streamlit/HW3_elements/ft_map_heat.html"

# HTML 파일 내용 읽기
with open(ft_map_path, 'r', encoding='utf-8') as file1:
    map_html1 = file1.read()

with open(ft_map_plus, 'r', encoding='utf-8') as file2:
    map_html2 = file2.read()

with open(ft_map_heat, 'r', encoding='utf-8') as file3:
    map_html3 = file3.read()


# Streamlit에 HTML 렌더링
#st.components.v1.html(map_html, height=600)  # height 조정 가능

# 가독성을 위해 탭에 넣기 
# Streamlit 탭 설정
tab1, tab2, tab3 = st.tabs(["기본ver", "세부정보ver", "히트맵ver"])

with tab1:
    st.subheader("기본ver")
    st.components.v1.html(map_html1, height=600)

with tab2:
    st.subheader("세부정보ver")
    st.components.v1.html(map_html2, height=600)

with tab3:
    st.subheader("히트맵ver")
    st.components.v1.html(map_html3, height=600)
