from PIL import ImageGrab,ImageOps
import pyautogui as gui
import time
from numpy import *

class cord():
    retrybtn=[496,338]
    # dinonose=[200,365]

def retry():
    gui.click(cord.retrybtn)

def jump():
    gui.keyUp('up')
    gui.keyDown('space')
    time.sleep(0.01)
    gui.keyUp('space')
def duck():
    gui.keyDown('down')
    time.sleep(0.01)
    gui.keyUp('down')

def ss():
    start=203
    length=165
    minus=10
    box=[start,350,start+length,380]
    # box=[200,200,300,300]
    # a=array(grayImage.getcolors())
    image=ImageGrab.grab(box).convert('L')
    img=image.load()
    # for i in range(220,200+length):
    #     for j in range(350,380):img[i,j]=0
    # image.show()
    for i in range(0,length):
        if img[i,29]<100:jump();break
    # for i in range(0,length):
    #     if img[i,0]<100:duck();break
    # for i in range(0,182):img[i,29]=0
    # for i in range(0,182):img[i,0]=0
    # img[4,4]=0
    # image.show()
    # print(a.sum())
    # if a.sum()!=622:jump()

retry()
time.sleep(5)
while(1):ss()
# ss()