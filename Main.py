from Settings import *

import pyautogui
import win32api, win32con
import keyboard
import time
import random
import threading

FishAgainPng = "./Assets/FSB/FishAgain.png"
SellPng = "./Assets/FSB/Sell.png"

def Click(X, Y):
    win32api.SetCursorPos((X, Y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def FindOnScreen(File):
    Vec4Location = pyautogui.locateOnScreen(File, confidence=.75)
    if Vec4Location is not None:
        Location = pyautogui.center(Vec4Location)
        return Location[0], Location[1]

def AutoFishThread():
    global AutoFish
    global FishAgainPng
    global FishCooldown

    while 1:
        if AutoFish:
            Goto = FindOnScreen(FishAgainPng)
            Click(Goto[0], Goto[1])
            LocalCooldown = FishCooldown + random.randint(1,3) // 1000
            time.sleep(LocalCooldown)

def AutoSellThread():
    global AutoSell
    global SellAgainPng
    global SellCooldown

    while 1:
        if AutoSell:
            Goto = FindOnScreen(SellPng)
            Click(Goto[0], Goto[1])
            LocalCooldown = (SellCooldown + random.randint(1,3) // 1000) * 60
            time.sleep(LocalCooldown)

def ToggleAutoFishThread():
    global AutoFish
    CanChange = True

    while 1:
        if keyboard.is_pressed('q') and AutoFish and CanChange:
            AutoFish = False
            CanChange = False
            print("Authfish is now set to: ", AutoFish)
        if keyboard.is_pressed('q') and not AutoFish and CanChange:
            AutoFish = True
            CanChange = False
            print("Authfish is now set to: ", AutoFish)
        
        if not keyboard.is_pressed('q'):
            CanChange = True

def RunThreads():
    FishThread = threading.Thread(target=AutoFishThread)
    FishThread.start()
    PauseFishThread = threading.Thread(target=ToggleAutoFishThread)
    PauseFishThread.start()
    #SellThread = threading.Thread(target=AutoSellThread)
    #SellThread.start()

RunThreads()