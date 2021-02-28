from __future__ import unicode_literals
import youtube_dl
import os
import streamlit as st


class Download(object):
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        self.song()

    def song(self):
        opts = {
            'verbose': True,
            'fixup': 'detect_or_warn',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3'
            }],
            'extractaudio': True,
            'outtmpl': self.save_path + '/%(title)s.%(ext)s',
            'noplaylist': False
        }
        ydl = youtube_dl.YoutubeDL(opts)
        ydl.download([self.url])


if __name__ == '__main__':

    # Inserting left bar:
    sidebar = st.sidebar.title('Welcome!')
    app_options = st.sidebar.selectbox('Select an option:', ['Download music', 'Download Playlist (beta)'])

    # Branching for app options function above:
    anchor_text = st.empty()
    if app_options == 'Download music':
        link_box = st.text_input('Enter Music Link')

    btn_download = st.button('Download')

    if btn_download and link_box != '':
        url = link_box
        Download(url)
    # checking if download was succesful
    # pass