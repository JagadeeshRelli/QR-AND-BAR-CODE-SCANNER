# to process image related things
import cv2
#to scan and decode qr and bar codes
from pyzbar.pyzbar import decode 
#to use numpy arrays
import numpy as np

#initialiazing the camera
capture=cv2.VideoCapture(0)
#setting the width of window
capture.set(3,600)
#setting the height of window
capture.set(4,600)

while True:
    #scanning the image
    success,img=capture.read()
    #keep scanning all the codes
    for qbcode in decode(img):
        #for decoding purposes
        mydata=qbcode.data.decode('utf-8')
        print(mydata)
        #storing the points of polygon in numpy array
        pnts=np.array([qbcode.polygon],np.int32)
        #reshaping the array into dynamic given no. of arrays
        #with 1 array each containing 2 elements
        pnts=pnts.reshape(-1,1,2)
        #applying the border of thckness: 5, color :(255,0,255)
        #closed: True for image:img with points :pnts
        cv2.polylines(img,[pnts],True,(255,0,255),5)
        #storing the rectangle points
        rectpnts=qbcode.rect
        #displaying the code info on the window
        cv2.putText(img,mydata,(rectpnts[0]-5,rectpnts[1]),cv2.FONT_HERSHEY_PLAIN
                   ,0.9,(0,0,0),2)
    #showing the camera window
    cv2.imshow('QR AND BAR CODE SCANNER',img)
    #waits for 1 millisecond after a key press on window
    cv2.waitKey(1)
    #closing the window by checking whether the close button is pressed or not
    if cv2.getWindowProperty('QR AND BAR CODE SCANNER', 4) < 1:
        capture.release()
        break
    
