import pyautogui
import time
from PIL import ImageGrab

while True:
    x,y = pyautogui.position()
    img = ImageGrab.grab(bbox=(x,y,x+1,y+1))
    color = img.getpixel((0,0))
    print(f"X:{x} Y:{y} RGB:{color}")
    if(color == (75, 219, 106)):
       pyautogui.click()
       break

    