import cv2
dispW = 320
dispH = 240
flip = 2

# camSet = 'nvarguscamerasrc ! video/x-raw(memory:NVMM),width=1920, height=1080, format=NV12, framerate=28/1 ! nvvidconv flip-method=' + str(flip) + ' ! video/x-raw, width=' + str(dispW) + ', height=' + str(dispH) + ", framat=BGRx ! video/x-raw, format=BGR ! appsink"
camSet = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3264, height=1848, framerate=28/1, format=NV12 ! nvvidconv flip-method=0 ! video/x-raw, width=1920, height=1080, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# for CSI-Camera
cam = cv2.VideoCapture(camSet)

# for webcam
# cam = cv2.VideoCapture(1)

while(True):
    ret, frame = cam.read()
    cv2.imshow('piCam', frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
