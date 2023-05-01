import streamlit as st
from PIL import Image
import os.path


st.set_page_config(page_title= "My Webpage", page_icon=":tada:", layout= "wide")
About_me = Image.open("IMAGES/about.jpg")

st.header("About me")
st.subheader("Hello, and welcome to my website!:wave:")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("I'm Mr. Visagie, and I'm a your Technical Sciences teacher")
        st.write("##")
    with right_column:
        st.image(About_me)


st.header("My story")
st.markdown("""
I've always known that I wanted to be a teacher. 
As a child, I loved learning and sharing my knowledge with others. 
After earning my Bachelor of Education Degree from the North West University(NWU-Potchefstroom), 
I started my career as a teacher at Saul Damon High School. Since then, I've taught:
- **:red[Mathematics]**
- **:green[Physical Sciences]**
- **:blue[Technical Sciences]**
- **:purple[Natural Sciences]**

I've also had the privilege of working with many wonderful students, like you.
""")

st.header("My Philosophy")
st.markdown("""
As a teacher, I believe that every student has the potential to succeed. 
My job is to help them unlock that potential by providing a supportive and engaging learning environment. 
I strive to create a classroom culture that promotes **:blue[curiosity], :green[critical thinking], and :red[collaboration]**. 
I also believe in tailoring my teaching approach to meet the needs of each individual learner.""")

st.header("My Classes")

st.markdown("""
**I currently teach Technical Sciences for**:

- **GRADE 12**
- **GRADE 11**
- **GRADE 10**

In my classes, we focus on reaching success by **hard work** and **continues co-operative learning**. 
I believe that by being positive and focused,
my learners can develop a love of learning that will serve them well throughout their lives.
""")

st.header("Contact me")
st.markdown("""
- Email: **:red[visagie.arnoldt@gmail.com]**
- Phone: **:green[076 728 3352]**
- Available hours: **:red[08:00 to 16:00]** 

""")


st.markdown("**:blue[Thank you for visiting my website, and I look forward to working with you!]**")






