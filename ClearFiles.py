import os

def clear():
    os.remove('./video/vid.mp4')
    print("Video Surpimée")
    screenshot = os.listdir('./ScreenShots')
    for i in screenshot:
        path = f"./ScreenShots/{i}"
        if i.split('.')[1]=='jpg' and os.path.isfile(path):
            os.remove(path)
