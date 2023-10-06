import pyautogui
import os
import time
pyautogui.press('win')
time.sleep(1)
pyautogui.write('vscode')
time.sleep(1)
pyautogui.press('enter')


def move_center(image):
    center_x = image[0] + image[2] // 2
    center_y = image[1] + image[3] // 2
    pyautogui.moveTo(center_x, center_y, duration=0.5)
    pyautogui.click()
   

     


#Searching for extension icon

ext_path=os.path.dirname(os.path.realpath(__file__))+"/ext.png"
ext1=None  
while ext1 is None:
    ext1=pyautogui.locateOnScreen(ext_path,confidence=0.7)
if ext1 is not None:
    move_center(ext1)
    time.sleep(1)
    pyautogui.write('clangd')
    

#Searching for clangd
cl1_path=os.path.dirname(os.path.realpath(__file__))+"/cl1.png"
cl1=None
while cl1 is None:
    cl1=pyautogui.locateOnScreen(cl1_path,confidence=0.7)

if cl1 is not None:
    move_center(cl1)
    #Searching for clangd install button
    install=None
    install_path=os.path.dirname(os.path.realpath(__file__))+"/install.png"    
    while install is None:
            install=pyautogui.locateOnScreen(install_path,confidence=0.7,region=cl1)
            
    if install is not None:
            
            move_center(install)

#Deleting old Search and search for new extension
sbar_path=os.path.dirname(os.path.realpath(__file__))+"/s1bar.png"
sbar=None
while sbar is None:
     sbar=pyautogui.locateOnScreen(sbar_path,confidence=0.7)
if sbar is not None:
    move_center(sbar)
    pyautogui.click()
    pyautogui.press('del')
    pyautogui.write("c++ testmate")




     