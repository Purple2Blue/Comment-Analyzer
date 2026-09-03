import streamlit as st 
import comments

st.title("Comment Anal")
st.header("Please Paste The Youtube Link Below")

link = st.text_input("Enter Youtube Link")
comments.get_video_id(link)