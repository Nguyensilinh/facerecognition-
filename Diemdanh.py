import cv2
import os
from datetime import date

today = date.today()
currentTime = today.strftime("%d_%m_%Y")
print(type(currentTime))


if not os.path.exists("AttendanceData"):
    os.mkdir("AttendanceData")     #Chua du lieu cac anh diem danh

if not os.path.exists("AttendanceData/"+str(currentTime)):
    os.mkdir("AttendanceData/"+str(currentTime))
cap = cv2.VideoCapture(0)

i = 0
status = 0      #0: chuan bi diem danh, 1 dang diem danh, 2 cho nguoi tiep theo
while True:
    print(i)
    ret, frame = cap.read()
    height, width, _ = frame.shape     #(480,640)
    print(height, width)
    cv2.rectangle(frame, (0, 0), (width, 80), (255, 0, 0), -1)
    if i<200:
        status = 0
    else:
        if i%200 == 0:
            if i/200%2==1:
                status = 1
            else:
                status = 2

    if status == 0:
        text = "Chuan bi diem danh"
    elif status == 1:
        text = "Dang diem danh"
        cv2.rectangle(frame, (int(width/4), int(height/4)), (int(3*width/4), int(5*height/6)), (0,0,255),3)
        image = frame[int(height/4):int(5*height/6), int(width/4):int(3*width/4)]

        if i/100%2 == 1:
            cv2.imwrite("AttendanceData/"+ str(currentTime)+"/"+str(i)+".jpg", image)
    elif status == 2:
        text = "Nguoi tiep theo"

    cv2.putText(frame, text, (10,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Video", frame)
    i += 1
    if cv2.waitKey(1) == ord("q"):
        break