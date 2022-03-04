import cv2
# Author : Imtiaz Adar
# Project : Video Capture
# Language : Python

def video_capture():
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        print('Sorry there is some error while opening the front camera...')
    isCapturing = True
    while isCapturing:
        _, video_frame = capture.read()
        cv2.imshow("Imtiaz Adar's Camera", video_frame)
        if cv2.waitKey(10) == ord('q'):
            isCapturing = False
    capture.release()
    cv2.destroyAllWindows()

video_capture()