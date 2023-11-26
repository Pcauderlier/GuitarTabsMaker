import cv2
from functions.getPositions import positions_en_px

def getFrames(path):
    #pos = (y,y,[(x,y),[bgr]])
    pos = positions_en_px()

    vid = cv2.VideoCapture(path)
    if not vid.isOpened():
        print('erreur : inpossible de lire la video')
        return 
    count = 0
    #position [bas, droite] comence en haut a gauche a 0,0
    position = pos[2][0]
    bgColor = pos[2][1]
    lastColor = bgColor
    if pos[0] > pos[1]:
        supp = pos[0]
        inf = pos[1]
    else:
        supp = pos[1]
        inf = pos[0]
    while True:
        Capturing, frame = vid.read()
        if not Capturing:
            break
      
        color = frame[position[0],position[1]]
        #[bleu, vert, rouge]
        capture = frame[inf:supp,:]
        if color[2] != bgColor[2] and lastColor[2]==bgColor[2] and color[0] != 0:
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

