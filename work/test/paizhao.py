# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File   :  paizhao.py    
@Time   :  2020/2/3 13:43 
@Author :  ByFan
'''
import cv2

def get_img_from_camera_local(folder_path):
    cap = cv2.VideoCapture(0)
    i = 1
    # while True:
    ret, frame = cap.read()
    # cv2.imshow("capture", frame)
    print(str(i))
    cv2.imwrite(folder_path + str(i) + '.jpg', frame)   # 存储为图像
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return
        # i += 1
    cap.release()
    # cv2.destroyAllWindows()

if __name__=="__main__":
    get_img_from_camera_local("G:\\")
