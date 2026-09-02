import streamlit as st 
import requests
import os
from dotenv import load_dotenv
import googleapiclient.discovery


def get_comment():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("YOUTUBE-API")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        videoId="wiSIE-fKsUI", order="relevance", maxResults=10,
        part="snippet"
    )
    response = request.execute()

    print(response)