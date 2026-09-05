import streamlit as st 
import comments
import re

st.title("Comment Anal")
st.header("Please Paste The Youtube Link Below")

if "video_id" not in st.session_state:
    st.session_state.video_id = None

link = st.text_input("Enter Youtube Link") #Getting the Link

if link:
    st.session_state.video_id = comments.get_video_id(link) #Getting the id
else:
    st.info("Please enter a valid Youtube link.")

col1, col2 = st.columns(2)

if st.session_state.video_id:
    col1.metric(f"{comments.get_comment_count(st.session_state.video_id)}Comments")

if st.session_state.video_id:
    top_10_comments = comments.get_comment_top_10(st.session_state.video_id)

    if top_10_comments:
        st.header("Top Comments")
        with st.container(height=500):
            for item in top_10_comments:
                match = re.match(r'@(\w+): "(.*)"$', item, re.DOTALL)
                if match:
                    author = match.group(1)
                    comment = match.group(2)
                    
                    st.write(f"Author: @{author}")
                    st.write(f"Comment: {comment}")
                    st.write("---")
        if not match:
            st.warning("Video doesn't have enough comments")

