import time
import pyautogui as pg
import webbrowser as wb

msg = input("Enter Message To Be Spammed: ")
x = int(input("Enter How Many Times You Have To Spam: "))

wb.open("https://web.whatsapp.com")

time.sleep(20)

for i in range(x):
    pg.typewrite(msg)
    pg.press('enter')