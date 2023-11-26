import cv2

def getFrames(path):
    vid = cv2.VideoCapture(path)
    if not vid.isOpened():
        print('erreur : inpossible de lire la video')
        return 
    fps = vid.get(cv2.CAP_PROP_FPS)
    count = 0
    #position [bas, droite] comence en haut a gauche a 0,0
    position = [670,300]
    lastColor = [20,20,20]
    while True:
        Capturing, frame = vid.read()
        if not Capturing:
            break
      
        color = frame[position[0],position[1]]
        #[bleu, vert, rouge]
        capture = frame[480:680,:]
        if color[2] != 20 and lastColor[2]==20 and color[0] != 0:
            print(f"couleur du pixel : {color}")
            frame[(position[0]-5):(position[0]+5),(position[1]-5):(position[1]+5)] = [0,0,255]
            # cv2.imshow("Pixel", capture)
            cv2.imwrite(f"./ScreenShots/{count}.jpg",capture)
            count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        lastColor = color
            

        
    vid.release()
    cv2.destroyAllWindows()
    print(f"nombre d'image = {count} ")

