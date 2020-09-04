import pyautogui
import random
import time
import winsound
from PIL import Image
import pygetwindow as gw
# 
# for t in gw.getAllWindows(): 
#     print(t.isMaximized)


onmyo=gw.getWindowsWithTitle('Onmyoji')[0]

#print(onmyo)
onmyo.size
onmyo.restore()

print(onmyo.size)
print(onmyo.topleft,onmyo.bottomright)

x=onmyo.topleft[0]
print(x)