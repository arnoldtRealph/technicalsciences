import streamlit as st
import pandas as pd

# Set the title of the website
st.set_page_config(page_title='Technical Sciences')

# Create a header
st.header('Please fill out this information')

# Create input fields for user information
name = st.text_input("Name:")
surname = st.text_input("Surname:")
grade = st.selectbox("What grade are you in?", ["10", "11", "12"])
selection = st.selectbox("What are you looking for?", ["Study material", "Past papers", "Local information"])
comment = st.text_area("Leave a comment:")

# Create a dictionary to store user information
user_info = {
    "Name": name,
    "Surname": surname,
    "Grade": grade,
    "Selection": selection,
    "Comment": comment
}

# Create a pandas DataFrame from user information
user_df = pd.DataFrame(user_info, index=[0])

# Export user information to Excel
try:
    with pd.ExcelWriter('~/Desktop/Output/Output.xlsx', mode='a', engine='openpyxl') as writer:
        user_df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
except FileNotFoundError:
    with pd.ExcelWriter('Output.xlsx', engine='openpyxl') as writer:
        user_df.to_excel(writer, sheet_name='Sheet1', index=False, header=True)

# Display confirmation message
st.write("Your information has been saved. Thank you for using our website!")
