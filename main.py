import cv2
gstr = 'v4l2src device=/dev/video0 ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! xvimagesink'

cap = cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw,format=YUY2,width=640,height=480,framerate=30/1 ! videoconvert ! video/x-raw, format=BGR ! appsink drop=1 ", cv2.CAP_GSTREAMER)


while 1:
    ret, img = cap.read()
    cv2.imshow("window", img)
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
