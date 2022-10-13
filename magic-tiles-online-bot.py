
# Open magic tiles and play it in full screen mode after running this python command

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api,win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(747,200)[0]==0:
        click(747,200)
    if pyautogui.pixel(849,200)[0]==0:
        click(849,200)
    if pyautogui.pixel(1015,200)[0]==0:
        click(1015,200)
    if pyautogui.pixel(1144,200)[0]==0:
        click(1144,200)