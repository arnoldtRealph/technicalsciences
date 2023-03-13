import streamlit as st

st.markdown(
    """
    <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            background-color: #800000;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.title("GRADE 11 RESOURCES")
    st.header("This is your guide to success")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1Bu5kOYvpsZ6JkSSgKcsVFtzAnpd6GcAs?usp=share_link)")