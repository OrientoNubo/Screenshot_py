from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
# from PIL import Image
from PIL import ImageQt

import win32gui
import sys
import time
# import cv2
import numpy as np
import matplotlib.pyplot as plt         # show image
# import matplotlib.image as mpimg        # read image
import pyautogui


def timer_start():
    start_time = time.time()
    return start_time
def timer_end(start_time):
    end_time = time.time()
    time_spent = end_time - start_time
    return time_spent

def HwndList():
    # hwnd list
    # ref: https://blog.csdn.net/weixin_39662578/article/details/112836211?utm_term=python%E8%8E%B7%E5%8F%96%E8%BF%9B%E7%A8%8B%E6%88%AA%E5%9B%BE&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-3-112836211&spm=3001.4430
    hwnd_title = dict()
    def get_all_hwnd(hwnd,mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)
    print('--------------- hwnd list start ---------------')
    for h,t in hwnd_title.items():
        if t != "":
            print(h, t)
    print('---------------- hwnd list end ----------------')

def ScreenshotQT(title):
    # Screenshot for hwnd
    hwnd = win32gui.FindWindow(None, title)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    return img

def qtimage2numpy(img):
    # ImageQt 2 PILimage 2 Numpy
    # Convert Template: https://ithelp.ithome.com.tw/articles/10230274
    img = ImageQt.fromqimage(img)   # qimage2pil
    img = np.array(img)             # pil2numpy
    return img

def showbyplt(img):
    # img = mpimg.imread(img)     # is already a numpy object
    h,w,c = img.shape
    print('height:', h, ' width:', w, ' channel:', c)
    plt.imshow(img)
    plt.axis('on')
    plt.show()

def CheckBlock(img, check_area):
    # imput: img, numpyarray[[x1,y1,r,g,b],[x2,y2,r,g,b]...]
    # y↓ x→ c.
    check_flag = False
    for i in range(len(check_area)):
        # print('rgb:', img[check_area[i,0], check_area[i,1], 0], img[check_area[i,0], check_area[i,1], 1], img[check_area[i,0], check_area[i,1], 2],)
        
        if img[check_area[i,0], check_area[i,1], 0] > (check_area[i,2]-10) & img[check_area[i,0], check_area[i,1], 0] < (check_area[i,2]+10):
            check_flag = True
        else:
            check_flag = False
            break
        if img[check_area[i,0], check_area[i,1], 1] > (check_area[i,3]-10) & img[check_area[i,0], check_area[i,1], 1] < (check_area[i,3]+10):
            check_flag = True
        else:
            check_flag = False
            break
        if img[check_area[i,0], check_area[i,1], 2] > (check_area[i,4]-10) & img[check_area[i,0], check_area[i,1], 2] < (check_area[i,4]+10):
            check_flag = True
        else:
            check_flag = False
            break

    if (check_flag == False):
        return False
    elif (check_flag == True):
        return True
    else:
        pass

def MoveMouseClick():
    # ref: https://yanwei-liu.medium.com/pyautogui-%E4%BD%BF%E7%94%A8python%E6%93%8D%E6%8E%A7%E9%9B%BB%E8%85%A6-662cc3b18b80
    # ref: https://ithelp.ithome.com.tw/articles/10232225
    # pyautogui.moveTo(-1503, 713, duration=0.1)
    pyautogui.leftClick()
    pyautogui.keyDown('a')
    time.sleep(0.5)
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(0.5)
    pyautogui.keyUp('d')



def test():
    check_area = np.array([[441,41,51,51,51], 
                            [451,41,51,51,51], 
                            [461,41,51,51,51], 
                            [471,41,51,51,51], 
                            [481,41,51,51,51]], 
                            dtype = int)
    return check_area

if __name__ == '__main__':

    
    HwndList()
    
    check_area = np.array([[190,295,245,245,245],       # white
                            [190,305,245,245,245], 
                            [190,315,245,245,245], 
                            [190,325,245,245,245], 
                            [190,335,245,245,245], 
                            [190,345,245,245,245], 
                            [190,627,245,245,245], 
                            [190,637,245,245,245], 
                            [190,647,245,245,245], 
                            [190,656,245,245,245],
                            [203,300,48,48,48],         # black
                            [203,400,48,48,48],
                            [203,500,48,48,48],
                            [203,600,48,48,48],
                            [537,1300,48,48,48],        # black
                            [537,1390,48,48,48],
                            [537,1600,48,48,48],
                            ], 
                            dtype = int)

    # check_area = test()
    # for i in range(2):
    while True:
        start_time = timer_start()

        img = ScreenshotQT('РokeMMO.py')
        img = qtimage2numpy(img)        # numpy.ndarray
        # showbyplt(img)

        InBattle = CheckBlock(img, check_area)
        print(InBattle)
 
        time.sleep(0.1)
        time_spent = timer_end(start_time)
        print('processing cost ', time_spent, 's')


    





    
    

