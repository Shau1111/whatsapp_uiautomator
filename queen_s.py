from uiautomator import device as d
from bs4 import BeautifulSoup

import numpy as np
import requests
import os
import time

center = [500, 800]
print("started..")
def getXmlSnapshot():
    xml = d.dump()
    #message_1=d(resourceId="com.whatsapp:id/single_msg_tv" ).text
    soup = BeautifulSoup(xml, 'xml')
    #print(message_1)
    print(xml)

# swiping functions
def fullPageSwipe():
    d.swipe(100, 1400, 100, 150, steps=50)

def miniSwipe():
    d.swipe(100, 1000, 100, 600, steps=50)
print("started..")
def read_message():
    new_message =d(resourceId="com.whatsapp:id/message_text").text
    print(new_message)
    return new_message
#getXmlSnapshot()
print("started..")
def sendMessageOnWhatsApp(msg):
    d(resourceId='com.whatsapp:id/entry').set_text(msg)
    d(resourceId='com.whatsapp:id/send').click()
print("started..")
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
def readLastMsg ():
    count=d(resourceId='com.whatsapp:id/message_text').count
    lastmessage=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
    print(lastmessage)
#read_message()
#readLastMsg()
def openunseenmsg ():
    number=d(resourceId="com.whatsapp:id/conversations_row_message_count").text
    d(resourceId="com.whatsapp:id/conversations_row_message_count").click()
    count=d(resourceId='com.whatsapp:id/message_text').count
    for i in range(int(number)):
        lastmessage=d(resourceId='com.whatsapp:id/message_text',instance=count-i-1).text
        print(lastmessage)    
openunseenmsg()
#sendMessageOnWhatsApp(read_message())


#def downloadImage():
    #message_1=d(resourceId="com.whatsapp:id/single_msg_tv" ).text
    #os.system("adb shell input text " + url)
    #print(message_1)
    #d.press.enter()
    #time.sleep(3)
    #d.long_click(*center)
    # d(text='Download image').click()
    #d(text='Save image').click()


#url = "https://s3.ap-south-1.amazonaws.com/static.queensapp.in/queensSmall.png"
#downloadImage()
#getXmlSnapshot()

