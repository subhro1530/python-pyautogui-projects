# Search anything in youtube and view it in fullscreen from here


import pyautogui
from time import sleep

a=input("Enter what you want to be searched in youtube...\n")
input()
pyautogui.press('win')
pyautogui.write('firefox',0.01)
pyautogui.press("enter")
sleep(1)
pyautogui.click(364,75)
pyautogui.write('https://www.youtube.com/',0.01)
pyautogui.press("enter")
sleep(2)
pyautogui.click(605,142)
pyautogui.write(a,0.01)
pyautogui.press('enter')
sleep(2)
pyautogui.click(733,578)
sleep(2)
pyautogui.press('f')