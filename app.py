import streamlit as st
st.set_page_config(page_title= "My Webpage", page_icon=":tada:", layout= "wide")

from PIL import Image
import requests
from streamlit_lottie import st_lottie
from streamlit import components


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

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_i9mtrven.json")
motivational_lottie = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_kyxinydn.json")
img_contact_form2 = Image.open("IMAGES/GROUP WORK.jpg")
img_contact_form = Image.open("IMAGES/study_methods.jpg")



st.title("Hi, I'm Mr. Visagie, your Technical Sciences teacher :wave:")
st.subheader("Welcome to my website")
st.header(" The AIM of Technical Sciences")
st.write( """Let's embark on a journey together where I'll be your guide in Technical Sciences! 
My mission is to help you shine by sharing my passion and skills, so you can confidently tackle any challenge
life throws at you. With our powers combined, we'll soar to new heights, unravel the toughest problems,
 and craft cutting-edge solutions that'll make the world a better place! Are you ready to dive in?
""")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is Technical Sciences?")
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
    st.header("UP YOUR GAME!")
    st.write("##")
    st.image(img_contact_form)
    st.subheader("5 ways to help you MASTER Technical Sciences")
    st.write("""
1. Ditch that phone, dude! It is time to slay some homework dragons!

2. Find your happy place (aka a peaceful, TV-free zone) and get your study groove on.

3. Wanna be an exam ninja? Practice with past papers and sharpen those skills!

4. Don't just read the questions, draw them a picture and watch the answers magically appear!

5. DAILY HOMEWORK = DAILY PROGRESS. Let's crush this learning thing one assignment at a time! 
            """)
        
with st.container():
    st.write("---")
    st.header("STUDY IN GROUPS")
    st.write("##")
    st.subheader("You can study in GROUPS to help you get better")
    st.write("""
1. You can learn new things and get different perspectives from your peers when you study in a group.

2. Studying with others can help you stay motivated and on track with your academic goals.

3. Working in a group can help you remember and understand concepts better.

4. Collaborating with your peers can improve your critical thinking and problem-solving skills.

5. Studying in a group can be less stressful and help you feel more connected with others, which can improve your overall mood and well-being.
             """)
    st.image(img_contact_form2)
    


with st.container():
    st.write("---")
    st.title("GRADE 12 RESOURCES")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1-OdRq6OwkDopuIZsSknbD9ipvRwFm1LJ?usp=share_link)")

with st.container():
    st.write("---")
    st.title("GRADE 11 RESOURCES")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1Bu5kOYvpsZ6JkSSgKcsVFtzAnpd6GcAs?usp=share_link)")

with st.container():
    st.write("---")
    st.title("GRADE 10 RESOURCES")
    st.subheader("Click on the following link to GET ACCESS to your STUDY MATERIAL.")
    st.write("[CLICK HERE >](https://drive.google.com/drive/folders/1U7EkFEwMrJPpAjN-4xX9VdoHWjy7340p?usp=share_link)")

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
    st.write("Designed by Mr. Visagie at Saul Damon High School")





