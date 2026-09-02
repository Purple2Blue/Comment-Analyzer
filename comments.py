import streamlit as st 
import requests
import os
from dotenv import load_dotenv
import googleapiclient.discovery

load_dotenv()

def get_comment(link):
    link = link.strip()[-11:]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE-API")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        videoId=link, order="relevance", maxResults=10,
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
