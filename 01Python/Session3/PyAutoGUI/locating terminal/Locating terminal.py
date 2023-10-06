
import pyautogui
import os



mypath =os.path.dirname(os.path.realpath(__file__))+"/terminal.png"
pyautogui.press('win')
pyautogui.write('term')
pyautogui.press('enter')

isfind =None
while isfind is None:
    isfind=pyautogui.locateOnScreen(mypath,confidence=0.5,grayscale=True)
    print("NOT YET")



print("i found it")
