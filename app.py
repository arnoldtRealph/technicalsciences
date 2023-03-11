from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title= "My Webpage", page_icon=":tada:", layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ybiszbil.json")
motivational_lottie = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_kyxinydn.json")
img_contact_form2 = Image.open("IMAGES/GROUP WORK.jpg")
img_contact_form = Image.open("IMAGES/STUDY.jpg")

st.header("Hi, I'm Mr. Visagie, your Technical Sciences teacher :wave:")
st.title(" The AIM of Technical Sciences")
st.write( """As you know, I'm very passionate about Technical Sciences and I hope to take you to the next level of solving Life's challenges.
         CLICK THE FOLLOWING LINK TO DOWNLOAD MORE QUESTION PAPERS AND MEMORANDUMS""")
st.write("[CLICK HERE >](https://play.google.com/store/apps/details?id=io.kodular.joegrapeacc.MatricGo)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is Technical Sciences")
        st.write("##")
        st.write(
            """As emphasized in the CAPS document,
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
            employment, citizenship, holistic and socio-economic development.""")

with right_column:
    st_lottie(lottie_coding, height = 350 , key="coding")

with st.container():
    st.write("---")
    st.header("UP YOUR GAME")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    
    with image_column:
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("5 ways to help you MASTER Technical Sciences")
        st.write("""
1. SWITCH YOUR CELL PHONE OFF when you do your HOMEWORK !

2. Study in a quiet place, away from the TV.

3. Use Past Exam papers, this will help you get used to the way questions are asked.

4. Make use of diagrams and sketches to help you interpret the questions.

5. DO YOUR HOMEWORK DAILY !!! 
            """)
        
with st.container():
    st.write("---")
    st.header("STUDY IN GROUPS")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_contact_form2)
with text_column:
    st.subheader("You can study in GROUPS to help you get better")
    st.write("""
    1. Studying in groups can help you BOOST your confidence and also helps you to make friends.

    2. If one friend struggles, there may be someone who understands a little bit more, 
       this way you can grow together.
             """)
with st.container():
    st.write("---")
st.header(" MOTIVATIONAL QUOTES :thought_balloon:")
st.write("##")
left_column, right_column = st.columns(2)
with left_column:
    st.write("""
Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do." - Pele

"You don't have to be great to start, but you have to start to be great." - Zig Ziglar

"The expert in anything was once a beginner." - Helen Hayes

"The difference between try and triumph is just a little umph!" - Marvin Phillips

"Believe you can and you're halfway there." - Theodore Roosevelt""")

with right_column:
    st_lottie(motivational_lottie,height= 350, key ="website")

with st.container():
    st.write("---")
    st.header("THANK YOU")
    st.subheader("More coming soon...")



