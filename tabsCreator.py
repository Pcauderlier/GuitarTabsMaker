import cv2
import numpy as np
import os

def tabs (name):
    image = []

    for i in range (len(os.listdir('./ScreenShots'))):
        image.append(cv2.imread(f"./ScreenShots/{i}.jpg"))
    tabs = np.vstack(image)
    cv2.imwrite(f"./tabs/{name}.jpg",tabs)
    
