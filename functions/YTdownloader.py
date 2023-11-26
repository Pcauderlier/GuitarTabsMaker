from pytube import YouTube

def download(url):
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download('./video','vid.mp4')
        print('Vidéo Telechargée')

# download('https://www.youtube.com/watch?v=ZUs-mkNpm2A&ab_channel=SimpleGuitarTabs')