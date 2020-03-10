import pyautogui
import random
import time
import winsound


from PIL import Image

width,height=pyautogui.size()
#width: 1920, height: 1080

root_path=r"E:\Other\Python Programs\onmyoji\\"


load_x0=976
load_y0=210
load_x1=1026
load_y1=275

load_x=1001
load_y=243
dura=0.5


def see_image(path):
    image=Image.open(path)
    image.show()
    
def click(x,y,dura):
    pyautogui.click(x,y,duration=dura)
    
def heian_story_reset(chapter):
    
    time.sleep(2)
    #moving to load    print(load_x,load_y)
    #click to load
    click(load_x,load_y,dura)

    pyautogui.moveTo(load_x,load_y,duration=dura)
    
    #click at chapter X
    if(chap==1)click(load_x,load_y,dura)
    else: click()
    #click at confirm
    pyautogui.click(1091,622,duration=dura)
    
    #loading scene
    time.sleep(4)
    
    #click to expand quest and to go to quest (twice)
    pyautogui.click(1785,324,clicks=2,interval=dura)
    #click skip
    click(1281,730,dura)
    #click confirm skip
    click(992,677,dura)
    
    #loading battle or prepared option
    time.sleep(2.5)
    
    #click to battle prepare interface
    click(969,296,dura)
    time.sleep(3.5)
    #click ready (pre-battle)
    click(1662,855,dura)
    #wait for battle to end
    time.sleep(36)
    
    #click result and skip screen, pick shiki
    click(640,519,dura)
    time.sleep(3)
    pyautogui.click(640,519,clicks=14,interval=0.3)
    #click to confirm picking shiki
    click(996,762,dura)
    #shiki shown, beep
    winsound.MessageBeep()
    
    time.sleep(1.5)
    #close
    click(1666,198,dura)
    click(1666,198,dura)
    
    #if not wanted
    time.sleep(3)   
    click(161,236,dura)
# 
# img_path="img/heian_skip_ip.png"
# find_skip=pyautogui.locateOnScreen(root_path+img_path,grayscale=True,minSearchTime=3)
# 
# print(find_skip)

chap=2
for i in range(10): heian_story_reset(chap)
