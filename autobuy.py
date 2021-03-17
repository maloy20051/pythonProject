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


ama_acc = 'maloy20051@gmail.com'
ama_pass = 'newHARD1488**'
img_amazon = r'C:/bot2/amazon.png'
img_continue = r'C:/bot2/continue.png'
img_login = r'C:/bot2/login.png'
img_password = r'C:/bot2/password.png'
img_sign = r'C:/bot2/sign.png'
img_cart = r'C:/bot2/cart.PNG'
img_buy = r'C:/bot2/buy.PNG'
img_amazon_link = r'C:/bot2/amazon_link.PNG'
img_disc_chan = r'C:/bot2/disc_chan.PNG'
img_disc_gc = r'C:/bot2/disc_gc.PNG'
img_cross = r'C:/bot2/cross.PNG'
img_place = r'C:/bot2/place.PNG'

def chrome_amazon():
    system("\"C:\Program Files\Google\Chrome\Application\chrome.exe\" www.amazon.com")

def time_USA():
    format = "%H:%M:%S %Z%z"
    now_utc = datetime.now(timezone('US/Eastern'))
    return (now_utc.strftime(format))

def click_img(img_go):
 #   pt = 0
    pg.screenshot("C:/bot2/screenshot.png")
    img = cv2.imread("C:/bot2/screenshot.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(img_go, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.96)
    #pg.click(x=1500, y=0)  # нужно что бы проинициализировать активное окно
    #  try: pt in zip(*loc[::-1]):
    #     print ('huh')
    #time.sleep(1)
    for pt in zip(*loc[::-1]):
        pg.leftClick(pt[0],pt[1]-2)
        pg.leftClick(pt[0],pt[1]-2)
        time.sleep(1)
        pg.move(100,100)
        return 1
    #print(pt[0]) #напечатать координату кортежа нажатия
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def wac_img(img_go): # wait and click on image
    counter = 0
    while (click_img(img_go)) !=1:
        counter+=1
        if counter %5==0:




wac_img(img_disc_chan) #ждать дискорд на нужном мониторе, перейти в дискорде на мой канал
click_img(img_disc_gc) #перейти в дискорде на текстовый канал graphic cards
wac_img(img_amazon_link) # ждать появления на канале новости с видеокартами, нажать на ссылку
pg.screenshot("C:/bot2/p/screenshot1.png")
wac_img(img_cross)
pg.screenshot("C:/bot2/p/screenshot2.png")
wac_img(img_buy) #найти и нажать buy
pg.screenshot("C:/bot2/p/screenshot3.png")
time.sleep(1)
pg.screenshot("C:/bot2/p/screenshot4.png")
click_img(img_password)#нажать на поле пароль если оно появится
pg.screenshot("C:/bot2/p/screenshot5.png")
pg.typewrite(ama_pass)#ввести пароль, если есть куда
pg.screenshot("C:/bot2/p/screenshot6.png")
click_img(img_sign)#нажать sing in, если такая кнопка есть
pg.screenshot("C:/bot2/p/screenshot7.png")
wac_img(img_place) # ВНИМАНИЕ!!! ОН ВСЕ САМ КУПИТ, ЭТО ПОСЛЕДНЯЯ КНОПКА
pg.screenshot("C:/bot2/p/screenshot8.png")