from pytube import YouTube
import time

def download(url):
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download('./video','vid.mp4')
        print('Vidéo Telechargée')

