from uiautomator import device as d
from bs4 import BeautifulSoup

import numpy as np
import requests
import os
import time

center = [500, 800]
#new branch - abhishek

def getXmlSnapshot():
  xml = d.dump()
  # message_1=d(resourceId="com.whatsapp:id/single_msg_tv" ).text
  soup = BeautifulSoup(xml, 'xml')
  # print(message_1)
  print(xml)

# swiping functions
def fullPageSwipe():
  d.swipe(100, 1400, 100, 150, steps=50)

def miniSwipe():
  d.swipe(100, 1000, 100, 600, steps=50)

def downloadImage():
  message_1=d(resourceId="com.whatsapp:id/single_msg_tv" ).text
  os.system("adb shell input text " + url)
  print(message_1)
  d.press.enter()
  time.sleep(3)
  d.long_click(*center)
  d(text='Download image').click()
  d(text='Save image').click()

def readLastMsgFromWhatsApp():
  messageElement = d(resourceId='com.whatsapp:id/message_text')
  message = "none"
  while (messageElement and messageElement.exists):
    message = messageElement.text
    print(message)
    messageElement = messageElement.down(resourceId='com.whatsapp:id/message_text')
    # break
  
  print("last_message: ", message)
  return message

def sendMessageOnWhatsApp(msg):
  d(resourceId='com.whatsapp:id/entry').set_text(msg)
  d(resourceId='com.whatsapp:id/send').click()

# sendMessageOnWhatsApp(readMsgFromWhatsApp())
readLastMsgFromWhatsApp()
#url = "https://s3.ap-south-1.amazonaws.com/static.queensapp.in/queensSmall.png"
#downloadImage()
#getXmlSnapshot()

