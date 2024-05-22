import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2

"""
関数名 : check_camera_connection
説明　 : 使用可能なカメラの同接数を調べる
"""
def check_camera_connection():
    true_camera_is = []  # 空の配列を用意

    for camera_number in range(0, 10):
        cap = cv2.VideoCapture(camera_number)
        ret, frame = cap.read()

        if ret is True:
            true_camera_is.append(camera_number)
            print("camera_number", camera_number, "Find!")
    return len(true_camera_is)
 
nowCamera = 0
maxCamera = check_camera_connection()
box = -1

camera = cv2.VideoCapture(0) 
while True:
    ret, frame = camera.read()
    cv2.imshow('camera', frame)

    if box != nowCamera:
        print(nowCamera)
        box = nowCamera
 
    key = cv2.waitKey(100)

    if key == ord('d'):
        print("     STOP")
        break
    elif key == ord('s'):
        print("     >>")
        if nowCamera == maxCamera-1:
            nowCamera = 0
        else :
            nowCamera = nowCamera + 1
        camera = cv2.VideoCapture(nowCamera)

    elif key == ord('a'):
        print("     <<")
        if nowCamera == 0:
            nowCamera = maxCamera-1
        else :
            nowCamera = nowCamera - 1
        camera = cv2.VideoCapture(nowCamera)
        
camera.release()
cv2.destroyAllWindows()

"""
- [OpenCVで使われるwaitkeyとは?定義から実用例をわかりやすく解説!?](https://kuroro.blog/python/8DIolh7Pwggq2pvabysn/)
- [Pythonでカメラを制御する【研究用】](https://qiita.com/opto-line/items/7ade854c26a50a485159)
"""
