import streamlit as st 
import comments

st.title("Comment Anal")
st.header("Please Paste The Youtube Link Below")

link = st.text_input("Enter Youtube Link") #Getting the Link

id = comments.get_video_id(link) #Getting the id

top_10_comments = comments.get_comment_top_10(id) 

st.write(top_10_comments)