from pickle import TRUE
import cv2
import easyocr
import time
import numpy as np

reader=easyocr.Reader(['en'], gpu=True)

vid=cv2.VideoCapture("C:/Users/aman9/Dropbox/PC/Downloads/OCR/OCR/numplate.mp4")
#vid=cv2.VideoCapture(0)
skip_frame= True;

while(TRUE):
   a=time.time()
   ret, img=vid.read()

   grayimg=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

   result=reader.readtext(grayimg)
   text=" "

   for res in result:
    text+=res[1]+" "


   cv2.putText(img, text, (50,70), cv2.FONT_HERSHEY_COMPLEX, 1, (58,58,255), 2)


   b=time.time()
   fps=1/(b-a)
   cv2.line(img, (20,25), (127,25), [85,45,255], 30)
   cv2.putText(img, f'FPS: {int(fps)}', (11,35), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, lineType=cv2.LINE_AA)
   cv2.imshow("result", img)

   if cv2.waitKey(1) & 0xff==ord('q'):
       break
   print(fps)
   print(text)







