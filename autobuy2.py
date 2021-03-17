from os import system
import numpy as np
import pyautogui as pg
import cv2
import time
from datetime import datetime
from pytz import timezone

img_amazon = r'C:/bot2/amazon.png'
img_continuebuy = r'C:/bot2/continuebuy.png'
img_proceed = r'C:/bot2/proceed.png'
img_place = r'C:/bot2/place.png'

def time_USA():
    format = "%H:%M:%S %Z%z"
    now_utc = datetime.now(timezone('US/Eastern'))
    return (now_utc.strftime(format))

def click_img(img_go):
    pg.screenshot("C:/bot2/screenshot.png")
    img = cv2.imread("C:/bot2/screenshot.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(img_go, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.96)
    for pt in zip(*loc[::-1]):
        pg.leftClick(pt[0],pt[1]-2)
        return 1
    #print(pt[0]) #напечатать координату кортежа нажатия
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def wac_img(img_go): # wait and click on image
    counter = 0
    while (click_img(img_go)) !=1:
        counter+=1
        if counter %5==0:
            print(time_USA())


wac_img(img_continuebuy) # ждать появления на канале новости, появления окна браузера с покупкой
print('continue')
pg.screenshot("C:/bot2/p/screenshot1.png")
wac_img(img_proceed) # ждать появления кнопки продолжить покупку
pg.screenshot("C:/bot2/p/screenshot2.png")
print('proceed')
#wac_img(img_place) # подтвердить реальную покупку
pg.screenshot("C:/bot2/p/screenshot3.png")
print('placed')







