import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

img_plot = Image.open("IMAGES/newplot.png")

st.subheader("HIER IS DIE MAART-UITSLAE PER LEERDER")
st.image(img_plot)


st.title("GRADE 12 RESOURCES")
st.subheader("Click on the following BUTTON to GET ACCESS to your STUDY MATERIAL.")

#CODE FOR THE BUTTON
button_html = '''
<style>
button {
  border-radius: .25rem;
  text-transform: uppercase;
  font-style: normal;
  font-weight: 400;
  padding-left: 25px;
  padding-right: 25px;
  color: #fff;
  -webkit-clip-path: polygon(0 0,0 0,100% 0,100% 0,100% calc(100% - 15px),calc(100% - 15px) 100%,15px 100%,0 100%);
  clip-path: polygon(0 0,0 0,100% 0,100% 0,100% calc(100% - 15px),calc(100% - 15px) 100%,15px 100%,0 100%);
  height: 40px;
  font-size: 0.7rem;
  line-height: 14px;
  letter-spacing: 1.2px;
  transition: .2s .1s;
  background-image: linear-gradient(90deg,#1c1c1c,#6220fb);
  border: 0 solid;
  overflow: hidden;
}

button:hover {
  cursor: pointer;
  transition: all .3s ease-in;
  padding-right: 30px;
  padding-left: 30px;
}
</style>
<button onclick="window.open('https://drive.google.com/drive/folders/1-OdRq6OwkDopuIZsSknbD9ipvRwFm1LJ?usp=share_link&utm_source=Google+Drive&utm_medium=Shared+link&utm_campaign=Grade+11+Streamlit&utm_id=G-QQREF8Y40R')" type="button">CLICK HERE</button>
'''

components.html(button_html)


st.title("GRADE 12 SUMMARIES")
st.markdown("""
Click the following link to download the summaries of 2022

- :red[You can save them on your device for later use]
- :blue[It is devided into topics, make sure to save it as such]
- :green[If you need any clarity, feel free to contact me]
""")
st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1diHiHHRHkkgjApAzRGK8PuX_vx4ekcp6?usp=share_link)")