import streamlit as st
st.set_page_config(page_title= "My Webpage", page_icon=":tada:", layout= "wide")

from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit import components
import os
import pandas as pd


# The site without any updates
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_nzw3czxk.json")
motivational_lottie = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_kyxinydn.json")
img_contact_form2 = Image.open("IMAGES/GROUP WORK.jpg")
img_contact_form = Image.open("IMAGES/Study_methods.jpg")
img_grade_11 = Image.open("IMAGES/GRADE 11.jpg")

with st.container():
    st.image(img_grade_11)
    st.title("GRADE 11 RESOURCES")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1Bu5kOYvpsZ6JkSSgKcsVFtzAnpd6GcAs?usp=share_link)")