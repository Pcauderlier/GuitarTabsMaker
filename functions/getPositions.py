import cv2



def positions_en_px():
    global index , pos
    index = 0
    pos = []
    def obtenir_position(event, x, y, flags, param):
      global index , pos
      text = ["Position de la Tablature :","Position de la Tablature :","Position du Pointeur :"]
      if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Position du point sélectionné : ({x}, {y}) pixels")
        if index == 0:
           frame[y-2:y+2,:] = [255,0,0]
           pos.append(y)
           cv2.putText(frame, text[1], (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elif index == 1:
           frame[y-2:y+2,:] = [0,255,0]
           pos.append(y)
           cv2.putText(frame, text[2], (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        elif index == 2:
           color = frame[y,x]
           pos.append([[y,x],color])
           
           
        index += 1
         
    vid = cv2.VideoCapture('./video/vid.mp4')
    vid.set(cv2.CAP_PROP_POS_MSEC, 2000)
    capturing, frame = vid.read()
    cv2.putText(frame, "Position de la Tablature :", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    while True:
        if capturing:
           cv2.imshow('frame',frame)

        if cv2.waitKey(100) & 0xFF == ord('q') or index >= 3:
            break
        cv2.setMouseCallback('frame',obtenir_position)
        
    vid.release()
    cv2.destroyAllWindows()
    return pos

