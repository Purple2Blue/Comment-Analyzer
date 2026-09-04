import streamlit as st 
import comments
import re

st.title("Comment Anal")
st.header("Please Paste The Youtube Link Below")

if "video_id" not in st.session_state:
    st.session_state.video_id = None

link = st.text_input("Enter Youtube Link") #Getting the Link


if link:
    id = comments.get_video_id(link) #Getting the id
else:
    st.warning("Please enter a valid Youtube link.")

top_10_comments = comments.get_comment_top_10(id) 

for item in top_10_comments:
    match = re.match(r'@(\w+): "(.*)"$', item, re.DOTALL)
    if match:
        author = match.group(1)
        comment = match.group(2)
        
        st.write(f"Author: {author}")
        st.write(f"Comment: {comment}")
        st.write("---")
