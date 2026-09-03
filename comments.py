import streamlit as st 
import re
import os
from dotenv import load_dotenv
import googleapiclient.discovery

load_dotenv()

def get_video_id(link): 
    pattern = r"^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})$"
    link = link.strip()
    match = re.fullmatch(pattern, link)
    if match:
        videp_id = match.group(4)

def get_comment_top_10(video_id): 
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE-API")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        videoId=video_id, order="relevance", maxResults=10,
        part="snippet"
    )
    response = request.execute()

    formatted_comments = []

    for item in response.get('items', [])[:5]:
        snippet = item['snippet']['topLevelComment']['snippet']
        name = snippet['authorDisplayName']
        text = snippet['textOriginal']
        
        # Combine them into: Name: "Comment Text"
        formatted_comments.append(f'{name}: "{text}"')

    return formatted_comments
