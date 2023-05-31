import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pytube import YouTube
import tempfile
import os

st.set_page_config(page_title="YT - Download", page_icon=":tada:", layout="centered")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
       st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#Animate
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

local_css("style/style.css")

animate_image = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_szdrhwiq.json")


# ---- HEADER SECTION ----
with st.container():
    st.markdown(
        """
        <style>
        .centered-text {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        
    st_lottie(animate_image, height=200, key="coding")
    st.write("<h1 class='centered-text'>Welcome to YT Download</h1>", unsafe_allow_html=True)
    st.write("<h2 class='centered-text'>Final project of the basic computer course, the page allows you to download videos through the url in MP4 format.</h1>", unsafe_allow_html=True)
    st.write("<p class='centered-text'>Presented by: Diego Armando Torres López.</p>", unsafe_allow_html=True)

# ---- Contaienr ----
with st.container():
    st.write("---")        
    #Busqueda de videos
    video_url = st.text_input("Enter your URL")
    button_search = st.button("Search video")
    
    if button_search:
        try:
            st.video(video_url)
            st.write("Processing, please wait a moment")
            youtube_video = YouTube(video_url)
            video_title = youtube_video.title
            stream = youtube_video.streams.get_highest_resolution()
            archivo = stream.download(output_path=tempfile.gettempdir(), filename=f'{video_title}.mp4')
            with open(archivo, "rb") as file:
                btn =  st.download_button(
                        label="Download video",
                        data=file,
                        file_name=archivo,
                        mime="mp4"
                    )
        except Exception as e:
            print("Error when searching for the video, this error is due to two possible reasons, either you did not enter the URL correctly, or the video you want to download is not available.", str(e))
