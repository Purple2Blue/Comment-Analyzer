import streamlit as st 
import re
import os
from dotenv import load_dotenv
import googleapiclient.discovery

load_dotenv()

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = os.getenv("YOUTUBE-API")

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

def get_video_id(link): 
    match = None
    video_id = None
    if link:
        pattern_n = r"^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})$" 
        link = link.strip()
        match = re.fullmatch(pattern_n, link) #Using Regex for verification for normal youtube link
    if not match and link:
        pattern_s = r"^(https?://)?(www\.)?(youtube\.com/shorts/)([a-zA-Z0-9_-]{11})$" 
        link = link.strip()
        match = re.fullmatch(pattern_s, link) #Using Regex for verification for shorts link
    if match:
        video_id = match.group(4)
    if not match:
        st.warning("Please Enter a Valid link!")

    return video_id     

def get_comment_top_10(video_id): 
    if video_id:
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

        request = youtube.commentThreads().list(
            videoId=video_id, order="relevance", maxResults=10,
            part="snippet"
        )
        response = request.execute()

        formatted_comments = [] #Getting the comment text with commenter name

        for item in response.get('items', [])[:10]:
            snippet = item['snippet']['topLevelComment']['snippet']
            name = snippet['authorDisplayName']
            text = snippet['textOriginal']
            
            # Combine them into: Name: "Comment Text"
            formatted_comments.append(f'{name}: "{text}"')

        return formatted_comments


def get_comment_count(video_id):
    if video_id:
        pass
