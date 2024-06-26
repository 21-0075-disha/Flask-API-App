import streamlit as st
import requests

def upload_video(video_file, tags):
    url = 'http://127.0.0.1:5000/upload-video'
    files = {'file': video_file}
    data = {'tags': tags}
    response = requests.post(url, files=files, data=data)
    return response.json()

st.title('Video Management System with FastAPI and AI/ML')

video_file = st.file_uploader("Upload a video:", type=["mp4", "avi", "mov"])
tags = st.text_input("Enter tags (comma separated)")

if video_file is not None and tags:
    if st.button('Upload and Transcribe'):
        with st.spinner('Uploading and transcribing...'):
            response = upload_video(video_file, tags)
            st.success('Transcription complete!')
            st.video(video_file)
            st.write(response['transcription'])
