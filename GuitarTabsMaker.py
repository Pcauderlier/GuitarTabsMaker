
from functions.YTdownloader import download
from functions.tabsCreator import tabs
from functions.screenshots import getFrames
from functions.ClearFiles import clear
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
    