import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def set_page_layout():
    st.set_page_config(
        page_title="My Webpage", 
        page_icon=":tada:", 
        layout="wide"
    )

def set_sidebar_style():
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                background-color: #800000;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_intro_section():
    st.title("Hi, I'm Mr. Visagie, your Technical Sciences teacher :wave:")
    st.subheader("Welcome to my website")
    st.header(" The AIM of Technical Sciences")
    st.write("""Let's embark on a journey together where I'll be your guide in Technical Sciences! 
    My mission is to help you shine by sharing my passion and skills, so you can confidently tackle any challenge
    life throws at you. With our powers combined, we'll soar to new heights, unravel the toughest problems,
    and craft cutting-edge solutions that'll make the world a better place! Are you ready to dive in?""")
    
def display_left_column():
    st.header("What is Technical Sciences?")
    st.write("##")
    st.write("""As emphasized in the CAPS document, Technical Sciences support learners in the three focus areas of technology, namely:
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

def display_right_column():
    lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_i9mtrven.json")
    st_lottie(lottie_coding, height=350, key="coding")

def display_up_your_game_section():
    img_contact_form = Image.open("IMAGES/STUDY.jpg")
    st.header("UP YOUR GAME!")
    st.write("##")
    text_column, image_column = st.columns((1, 2))
    
    with image_column:
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("5 ways to help you MASTER Technical Sciences")
        st.write("""
        1. Ditch that phone, dude! It is time to slay some homework dragons!
        2. Find your happy place (aka a peaceful, TV-free zone) and get your study groove on.
        3. Wanna be an exam ninja? Practice with past papers and sharpen those skills!
        4. Don't just read the questions, draw them a picture and watch the answers magically appear!
        5. DAILY HOMEWORK = DAILY PROGRESS. Let's crush this learning thing one assignment at a time!""")

def display_study_in_groups_section():
    img_contact_form2 = Image.open("IMAGES/GROUP WORK.jpg")
    st.header("STUDY IN GROUPS")
    st.write("##")
