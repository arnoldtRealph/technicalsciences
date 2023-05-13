import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit import components
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title= "TECHSCI", layout= "wide")

st.success("👈Thank you for visiting my site. Check out the sidebar for more info!")
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
img_home = Image.open("IMAGES/HOME.jpg")



st.title("Hi, I'm Mr. Visagie, your Technical Sciences teacher :wave:")
st.image(img_home)

st.subheader("Welcome to my website")
st.write("---")
st.header(" The AIM of Technical Sciences")
st.markdown( """**Let's embark on a journey together where I'll be your guide in Technical Sciences! 
My mission is to help you shine by sharing my passion and skills, so you can confidently tackle any challenge
life throws at you. With our powers combined, we'll soar to new heights, unravel the toughest problems,
 and craft cutting-edge solutions that'll make the world a better place! Are you ready to dive in?**
""")


import os.path


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is Technical Sciences?")
        st.write("##")
        st.markdown(
            """_As emphasized in the CAPS document,
            Technical Sciences support learners in the three focus areas of technology, namely:
            Mechanical, 
            Electrical and 
            Civil Technology.
            Learners at technical schools will be able to integrate scientific knowledge
            in a more informed way in their field of specialization. Scientific concepts and skills 
            will be easier to master if learners have a technical orientation in their schooling.
            Technical Sciences try to address the needs of the industry and 
            the technology subjects by being an enabling subject 
            to promote technology studies in schools.
            Technical Sciences aim to prepare learners for further education and training,
            employment, citizenship, holistic and socio-economic development._""")

with right_column:
    st_lottie(lottie_coding, height = 350 , key="coding")

with st.container():
    st.write("---")
    st.header("UP YOUR GAME!")
    st.write("##")
    st.image(img_contact_form)
    st.subheader("5 ways to help you MASTER Technical Sciences")
    st.markdown("""

     - Instead of getting distracted by your phone, **:blue[let's focus on finishing some homework challenges]**.

     - Find a quiet, peaceful place where you feel comfortable studying **:red[without any distractions]**, such as watching TV.

     - Want to excel in your exams? Practice by **:green[solving problems from previous papers]** and improve your skills!

     - Instead of just reading the questions, try to **:blue[draw them out]** to help you **:blue[visualize]** and solve the problems more easily!

     - :green[Completing your daily homework is essential for your academic progress]. Let's work hard and aim for success, one assignment at a time! 
            """)
        
with st.container():
    st.write("---")
    st.header("STUDY IN GROUPS")
    st.write("##")
    st.subheader("You can study in GROUPS to help you get better")
    st.markdown("""
- You can learn new things and get **:blue[different perspectives]** from your peers when you study in a group.

- Studying with others can help you **:red[stay motivated]** and on track with your academic goals.

- Working in a group can **:green[help you remember]** and understand concepts better.

- Collaborating with your peers can **:blue[improve your critical thinking]** and **:green[problem-solving skills]**.

- Studying in a group can be **:green[less stressful]** and help you **:green[feel more connected with others]**, which can improve your overall mood and well-being.
             """)
    st.image(img_contact_form2)
    


with st.container():
    st.write("---")
    st.title("GRADE 12 RESOURCES")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1-OdRq6OwkDopuIZsSknbD9ipvRwFm1LJ?usp=share_link&utm_source=Google+Drive&utm_medium=Shared+link&utm_campaign=Grade+11+Streamlit&utm_id=G-QQREF8Y40R)")

with st.container():
    st.write("---")
    st.title("GRADE 11 RESOURCES")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1Bu5kOYvpsZ6JkSSgKcsVFtzAnpd6GcAs?usp=share_link&utm_source=Google+Drive&utm_medium=Shared+link&utm_campaign=Grade+11+Streamlit&utm_id=G-7S7XQ3SXGP)")

with st.container():
    st.write("---")
    st.title("GRADE 10 RESOURCES")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1U7EkFEwMrJPpAjN-4xX9VdoHWjy7340p?usp=share_link&utm_source=Google+Drive&utm_medium=Shared+link&utm_campaign=Grade+10+Streamlit&utm_id=G-55964DLV42)")

with st.container():
    st.write("---")
st.header(" MOTIVATIONAL QUOTES :thought_balloon:")
st.write("##")
left_column, right_column = st.columns(2)
with left_column:
    st.markdown("""
- :green[Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do."] - :red[Pele]

- :blue["You don't have to be great to start, but you have to start to be great."] - :red[Zig Ziglar]

- :green["The expert in anything was once a beginner."] - :red[Helen Hayes]

- :blue["The difference between try and triumph is just a little umph!"] - :red[Marvin Phillips]

- :green["Believe you can and you're halfway there."] - :red[Theodore Roosevelt]""")
    


with right_column:
    st_lottie(motivational_lottie,height= 350, key ="website")
 
#Temperature widget

latitude = st.secrets["latitude"]
longitude = st.secrets["longitude"]
API_KEY = st.secrets["API_KEY"]

url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    description = data['weather'][0]['description']
    icon_code = data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/w/{icon_code}.png"

    st.title("Upington Weather")
    st.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.image(icon_url, width=100)
    st.markdown(f'<p style="color: #F2C94C;">{temperature:.1f}°C</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: #F2C94C;">{description.capitalize()}</p>', unsafe_allow_html=True)
    st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
else:
    st.write('Error retrieving temperature data.')


with st.container():
    st.write("---")
    st.header("THANK YOU")
    st.subheader("More coming soon...")
    st.write("Designed by Mr. Visagie at Saul Damon High School")





