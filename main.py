import pyautogui 
from threading import Thread
from pynput.mouse import Controller, Button
from time import sleep
from pynput.keyboard import KeyCode,Listener
import tkinter as tk  
import pyscreeze

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

delay=0.5
mouse=Controller()

class AutoClicker(Thread):
    clicking = False

    def run(self):
        try: 
            while True:
                    if AutoClicker.clicking:
                        res = pyautogui.locateOnScreen("image.png",confidence=0.8)
                        print(res)
                        if res is not None:
                            break
                        mouse.click(Button.left)

                    sleep(delay)
        except KeyboardInterrupt:
            pass

def keypress(key):
    if key == KeyCode(char="k"):
        AutoClicker.clicking=not AutoClicker.clicking


AutoClicker().start()

with Listener(on_press=keypress) as listener:
    listener.join()