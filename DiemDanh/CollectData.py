import cv2
import os

name = input("Nhập tên của bạn: ")
os.mkdir(str(name))
cap = cv2.VideoCapture(0)

i = 0
while True:
    print(i)
    ret, frame = cap.read()
    height, width, _ = frame.shape
    cv2.rectangle(frame, (0, 0), (width, 80), (255, 0, 0), -1)
    if i<150:
        text = "Chuan bi chup anh"
    elif i>150 and i <500:
        text = "Xoay goc mat de chup anh"
    else:
        text = "Ket thuc chup anh"
    cv2.putText(frame, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    cv2.imshow("Video", frame)
    if i%50 == 0 and i>150 and i<500:
        cv2.imwrite(name+"/"+str(i)+".jpg", frame)
    i += 1
    if cv2.waitKey(1) == ord("q"):
        break