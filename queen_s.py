from uiautomator import device as d
from bs4 import BeautifulSoup

import numpy as np
import requests
import os
import time
import re

center = [500, 800]
print("started..")
def getXmlSnapshot():
    xml = d.dump()
    #message_1=d(resourceId="com.whatsapp:id/single_msg_tv" ).text
    soup = BeautifulSoup(xml, 'xml')
    #print(message_1)
    print(xml)

def read_message():
    new_message =d(resourceId="com.whatsapp:id/message_text").text
    print(new_message)
    return new_message

def sendMessageOnWhatsApp(msg):
    d(resourceId='com.whatsapp:id/entry').set_text(msg)
    d(resourceId='com.whatsapp:id/send').click()

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

def readLastMsg():
    count=d(resourceId='com.whatsapp:id/message_text').count
    lastmessage=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
    print(lastmessage)

def openunseenmsg():
    number=d(resourceId="com.whatsapp:id/conversations_row_message_count").text
    d(resourceId="com.whatsapp:id/conversations_row_message_count").click()
    d.wait.idle()
    count=d(resourceId='com.whatsapp:id/message_text').count
    for i in range(int(number)):
        lastmessage=d(resourceId='com.whatsapp:id/message_text',instance=count-1-i).text
        print(lastmessage)

def getCoordinatesFromMatrix(index):
    d.wait.idle()
    soup = BeautifulSoup(d.dump(), 'xml')
    w, h = getWindowSize(soup)
    w0, h0, y0 = getItemSizeAndStartY(soup)
    print("w0, h0, y0 : ", w0, h0, y0)
    m = int(w/w0) #no of pics in a row
    print("m: ", m)
    x_req = ((index % m) - 0.5) * w0
    y_req = y0 + (int(index/m) + 0.5) * h0
    return [x_req, y_req]

def getWindowSize(soup):
    bounds = soup.find(lambda tag:tag.name == "node" and tag["package"] == "com.whatsapp")["bounds"]
    x, y, w, h = getCornersFromBounds(bounds)
    print(w, " - ", h)
    return [w, h]

def getItemSizeAndStartY(soup):
    # soup = BeautifulSoup(d.dump(), 'xml')
    bounds = soup.find(lambda tag:tag.name == "node" and "ImageView" in tag["class"] and tag["package"] == "com.whatsapp")["bounds"]
    x, y, w, h = getCornersFromBounds(bounds)
    return [w-x, h-y, y]

def getCornersFromBounds(bounds):
    corners = bounds.replace('][',',').replace(']','').replace('[','').split(',')
    x, y, w, h = [int(corner) for corner in corners]
    return [x,y,w,h]

def sendMedia(index):
    d(resourceId="com.whatsapp:id/input_attach_button").click()
    d(text="Gallery").click()
    d.wait.idle()
    # d(resourceId="com.whatsapp:id/title").click()
    d(text="All media").click()
    d.wait.update()
    count=d(className="android.widget.ImageView").count 
    # d(className="android.widget.ImageView").click()
    clickOnImage(index)
    #print(count)
    d.wait.idle()
    d(resourceId="com.whatsapp:id/send").click()

def clickOnImage(index):
    print("here")
    d.click(*getCoordinatesFromMatrix(index))

def keepCheckingForNewMessage():
    while(not d(resourceId="com.whatsapp:id/conversations_row_message_count").exists):
      time.sleep(2)
    openunseenmsg()

keepCheckingForNewMessage()
# sendMedia(18)



