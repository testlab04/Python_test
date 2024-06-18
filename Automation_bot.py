import pywinauto
from pywinauto.application import Application
from piwinauto import mouse
from piwinauto import keyboard
import time
from pywinauto.keyboard import SendKeys
# If Your Want Something to be Typed, Import SendKey from pywinauto.keyboard
app =Application.start("C:/Program Files (x86)\Google\Chrome\Application\chrome.exe")
#cmd_line is Required to Start the Application !
#backend is necessary to define because if you want to automate desktop application backend is win32
time.sleep(10)#To Wait After The Above Command

pywinauto.mouse.click(button="left", coords=(1302,527))#To Click on Search Bar
time.sleep(2)#To Wait After The Click Command
SendKeys = (https://www.youtube.com/channel/UC-5qgYN77ce7rfgiQ8jidtQ)
time.sleep(1)#To Wait 1 Seconds after Typing the Link
SendKeys('{ENTER}') #To Press Enter after Typing the Link
time.sleep(10) #Depends Upon Your Internet Connection
pywinauto.mouse.click(button="left", coords=(1737,595)) #To Click on SUBSCRIBE