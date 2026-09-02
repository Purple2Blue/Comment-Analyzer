import streamlit as st 
import requests
import os
import re
from dotenv import load_dotenv
import googleapiclient.discovery
import comments


load_dotenv()


st.title("Comment Anal")
st.header("Please Paste The Youtube Link Below")

link = st.text_input("Enter Youtube Link")
comments.get_comment(link)