import streamlit as st
import requests
st.title("Image Generation!")
prompt=st.text_input("Enter the prompt")
url="https://image.pollinations.ai/prompt/"+requests.utils.quote(prompt)
img=requests.get(url).content
with open("stand1.png","wb")as f:
    f.write(img)
st.image("stand1.png")
