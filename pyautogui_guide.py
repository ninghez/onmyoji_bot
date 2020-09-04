import pyautogui
import random
import time
import winsound

 


def main():
	pyautogui.click(x,y,duration=dur,button='right')
	'''duration: time it takes to perform the action, including mov ng to the mouse position '''
	pyautogui.position() # Get the XY position of the mouse.
	pyautogui.alert('msg') # Make an alert box appear and pause the program until OK is clicked.
	time.sleep(3) # time to sleep/pause
	winsound.MessageBeep() #beeps
	pyautogui.click('button.png') #find img and click

	button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9)
    #button7location
    #Box(left=1416, top=562, width=50, height=41)

if __name__== "__main__":
	main()
