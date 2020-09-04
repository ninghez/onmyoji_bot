import pyautogui
import random
import time
import winsound


from PIL import Image


    
def click(x,y,dur):
    pyautogui.click(x,y,duration=dur)
    



def main():
	#souls inviting: only click ready/go (bottom right)
	#soul being invited: lock => only click end screen (twice)
    dur=0.15
    x=1
    y=1
    x, y = pyautogui.position() # Get the XY position of the mouse.
    #print(x,y)
    x,y=961,659
    
    for i in range(50): 
    	pyautogui.click(x,y,duration=dur,clicks=2,interval=0.5)
    	time.pause(75)

if __name__== "__main__":
    main()
