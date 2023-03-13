import streamlit as st

st.markdown(
    """
    <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            background-color:  #800000;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.title("GRADE 12 RESOURCES")
    st.header("This is your guide to success")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1-OdRq6OwkDopuIZsSknbD9ipvRwFm1LJ?usp=share_link)")

with st.container():
    st.write("---")
    st.subheader("You can also follow the link below which will take you to google play store to download the MATRIC App with moost past exam papers en memos loaded")
    st.write("[CLICK HERE >](https://play.google.com/store/apps/details?id=io.kodular.joegrapeacc.MatricGo)")