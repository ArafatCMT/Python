import pyautogui
# pyautogui.write("I love you , Python", interval=0.25)
# pyautogui.write("*", interval=0.25)
n = int(input())
from time import sleep
sleep(4)
for i in range(1,n+1):

    for j in range(1,i+1):

        pyautogui.write("#", interval=0.25)
    pyautogui.press("Enter")






