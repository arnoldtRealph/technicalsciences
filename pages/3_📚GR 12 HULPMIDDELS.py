import streamlit as st
from PIL import Image

img_plot = Image.open("IMAGES/newplot.png")

st.subheader("HIER IS DIE MAART-UITSLAE PER LEERDER")
st.image(img_plot)


st.title("GRADE 12 RESOURCES")
st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
st.write("[CLICK HERE](https://drive.google.com/drive/folders/1-OdRq6OwkDopuIZsSknbD9ipvRwFm1LJ?usp=share_link&utm_source=Google+Drive&utm_medium=Shared+link&utm_campaign=Grade+11+Streamlit&utm_id=G-QQREF8Y40R)")


import streamlit as st


st.title("GRADE 12 SUMMARIES")
st.markdown("""
Click the following link to download the summaries of 2022

- :red[You can save them on your device for later use]
- :blue[It is devided into topics, make sure to save it as such]
- :green[If you need any clarity, feel free to contact me]
""")
st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1diHiHHRHkkgjApAzRGK8PuX_vx4ekcp6?usp=share_link)")