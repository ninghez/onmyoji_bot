import pyautogui
import random
import time
import winsound
import cv2
import pygetwindow as gw
import logging
from PIL import Image

#on the explore page w/ chapter
def find_window_coord():

    onmyo=gw.getWindowsWithTitle('Onmyoji')[0]
    onmyo.restore()

    #print(onmyo.size)
    pos1=(onmyo.topleft)
    pos2=(onmyo.bottomright)
    return (pos1,pos2)

class Explore():
    def __init__(self):
        (self.pos1,self.pos2)=find_window_coord()


    def find_color(pos1,pos2,color,tolerance=0):
        #im=pyautogui.screenshot()
        for x in range(pos1[0],pos2[0]+1):
            for y in range(pos1[1],pos2[1]+1):
                match=pyautogui.pixelMatchesColor(x,y,color,
                    tolerance=tolerance)
                if match: return (x,y)
        return -1

    #step 1: find explore, use a picture, then click

    def click_explore(self):
        dur=0.5
        try:
            (x,y,w,h)=pyautogui.locateOnScreen('img/explore.png')
            
        except TypeError:
            print("Can not find explore button")

        #explore button: x~x+120, y~y+20
        x=random.randint(x,x+120)
        y=random.randint(y,y+20)
        pyautogui.click(x,y,duration=dur)

        #loading scene...

    def find_exp_monster(self):
        res=1
        color=(140,122,44)
        #find by color
        exp_posi= find_color(self.pos1,self.pos2,color,2)
        #find by image
        if exp_posi==-1:
            try: 
                (x,y,w,h)=pyautogui.locateOnScreen("img/exp.png",
                    confidence=0.7)
                winsound.MessageBeep() #un
                logging.info("found")
            except:
                res=-1
                logging.info("no exp mons found")

    def start(self):
        logging.basicConfig(level=logging.INFO)
        time.sleep(3)
        
        print(self.pos1,self.pos2)


if __name__ =="__main__":
    e=Explore()
    e.start()