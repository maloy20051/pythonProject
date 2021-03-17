import os
from os import system
import numpy as np
import pyautogui as pg
import cv2
import sys
import keyboard
import time
from datetime import datetime
from pytz import timezone
img_datalover = r'C:/bot2/datalover.PNG'
img_del = r'C:/bot2/del.PNG'

def del_message_datalover():
 #   pt = 0
    pg.screenshot("C:/bot2/screenshot.png")
    img = cv2.imread("C:/bot2/screenshot.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('C:/bot2/datalover.PNG', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.96)
    for pt in zip(*loc[::-1]):
        #print(pt[0])  # напечатать координату кортежа нажатия
        #print(pt[1])
        pg.leftClick(pt[0]+105,pt[1]-9) #клик на крест около сообщения



    pg.screenshot("C:/bot2/screenshot2.png")
    img = cv2.imread("C:/bot2/screenshot2.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('C:/bot2/del.PNG', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.96)
    for pt in zip(*loc[::-1]):
        pg.moveTo(pt)
        print(pt[0])  # напечатать координату кортежа нажатия
        print(pt[1])
        pg.leftClick(pt)
        pg.leftClick(pt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




del_message_datalover()