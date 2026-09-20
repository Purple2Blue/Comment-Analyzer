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

col1, col2, col3 = st.columns(3)

if st.session_state.video_id:
    col1.metric(label = "Comment Count", value = comments.get_comment_count(st.session_state.video_id))

if st.session_state.video_id:
    col2.metric(label = "View Count", value = comments.get_view_count(st.session_state.video_id))

if st.session_state.video_id:
    col3.metric(label = "Like Count", value = comments.get_like_count(st.session_state.video_id))



if st.session_state.video_id:
    number_comments = st.number_input(label="How Many Top Comments Do You Wish To See", min_value=1, max_value=30, step=1, value=10)
    top_n_comments = comments.get_comment_top_n(st.session_state.video_id, number_comments)

    if top_n_comments:
        st.header(f"Top {number_comments} Comments")
        with st.container(height=550):
            for item in top_n_comments:
                match = re.match(r'(.+?): "(.*)\"$', item, re.DOTALL)
                if match:
                    author = match.group(1)
                    comment = match.group(2)
                    
                    st.write(f"Author: {author}")
                    st.write(f"Comment: {comment}")
                    st.write("---")
    else:
        st.warning("Video doesn't have enough comments")
