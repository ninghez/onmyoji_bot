import pyautogui
import random
import time
import winsound
import sys

from PIL import Image

def click(x,y,dur):
    pyautogui.click(x,y,duration=dur)
      



def paper_investigation():
    dur=0.2
    x=random.randint(1494,1608)
    y=815
    click(x,y,dur)
    time.sleep(3)

def totem():
    dur=0.3
    x=random.randint(1557,1690)
    y=919
    #start battle button
    pyautogui.click(x,y,duration=dur)
    #doll position
    x=1106
    y=576
    
    #pyautogui.click(x,y,clicks=4,interval=0.4,duration=dur)
    time.sleep(3)
 
def paper_doll_claim():
    x=1498
    y=963
    dur=0.2
    pyautogui.click(x,y,clicks=3,interval=0.4,duration=dur)
    time.sleep(60)
def s11():
    dur=0.2
    #1219,643
    #1190,859
    #1105,753
    #1344,733
    #1211，662; 1199,591; 1202,550
    x=random.randint(1301,1311) #1291
    y=random.randint(904,914) #519

    pyautogui.click(x,y,clicks=20,interval=1.5)

    #print(" done ")

    #42s (runtime) + 14s (downtime)
    #time.sleep(57)
    
def explore():
    dur=0.2
    x=1291
    y=519
    pyautogui.click(x,y,clicks=8,interval=0.2,duration=dur)
    time.sleep(3) 
def main():
    x=0
    while True:
        print("lp:",x, end="")
        x=x+1
        totem() 
        
 

if __name__== "__main__":
    option=1
    if(option==0):
        print(pyautogui.position())
    else:
        main()
