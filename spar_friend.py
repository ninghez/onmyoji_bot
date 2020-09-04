import pyautogui
import random
import time
import winsound


from PIL import Image


    
def click(x,y,dur):
    pyautogui.click(x,y,duration=dur)
    

def spar_friend():
    time.sleep(2)
    dur=0.5
    click(1220,909,dur) #friends
    time.sleep(1)
    click(513,234,dur) #latest
    
    click(722,408,dur) # > button on friend

    click(832,528,dur) # spar

    time.sleep(14)

    click(1643,824,dur) #ready\
    time.sleep(6)
    click(177,962,dur) #manual -> auto

    time.sleep(8)
    click(1220,909,dur) #anywhere
    time.sleep(5)





def main():
    for i in range(27): spar_friend()

if __name__== "__main__":
    main()
