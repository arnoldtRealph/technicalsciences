import openai
import streamlit as st

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define the title and subtitle of the app
st.title("What is ChatGPT?")
st.subheader("A brief explanation of OpenAI's language model")

# Define a prompt to send to ChatGPT
prompt = "What is ChatGPT?"

# Send the prompt to the GPT-3 API
response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)

# Display the response from ChatGPT
st.write(response.choices[0].text)