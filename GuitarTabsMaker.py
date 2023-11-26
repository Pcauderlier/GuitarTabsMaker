from YTdownloader import download
from tabsCreator import tabs
from screenshots import getFrames
from ClearFiles import clear
import time


def GuitarTabsMaker(url,name):
    download(url)
    time.sleep(1)
    getFrames('./video/vid.mp4')
    tabs(name)
    time.sleep(2)
    clear()

if __name__=='__main__':
    name = input('Entrer le nom de la tablature : ')
    url = input("Entrer l'adresse de l'url Youtube : ")
    GuitarTabsMaker(url,name)
    