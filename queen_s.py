from uiautomator import device as d
from bs4 import BeautifulSoup

import numpy as np
import requests
import os
import time
def setAndroidHome():
    os.environ["ANDROID_HOME"] = "/Users/abg/Library/Android/sdk"
    os.environ["PATH"] = "${PATH}:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools"
#setAndroidHome()
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
def readLastMsg ():
    count=d(resourceId='com.whatsapp:id/message_text').count
    lastmessage=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
    print(lastmessage)
#readLastMsg()
#readLastMsg()
def openunseenmsg ():
    number=d(resourceId="com.whatsapp:id/conversations_row_message_count").text
    d(resourceId="com.whatsapp:id/conversations_row_message_count").click()
    print(number)
    count=d(resourceId='com.whatsapp:id/message_text').count
    lastmessage=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
    print(lastmessage)
    sendMessageOnWhatsApp(" welcome to queen's press : 1,2")
    check_new_msg()

#sendMessageOnWhatsApp(read_message())
def media (category):
     d(resourceId="com.whatsapp:id/input_attach_button").click()
     d(text="Gallery").click()
     d(text=category).click()
     count=d(className="android.widget.ImageView").count
     print(count)
     d(className="android.widget.ImageView",instance=count-count).click()
     d(resourceId="com.whatsapp:id/send").click()
#media ("Kurti")
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
    bounds =soup.find(lambda tag:tag.name == "node" and tag["package"] == "com.whatsapp")["bounds"]
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
#sendMedia(3)
def read_inside_msg():
    a=d.dump()
    count_1=d(resourceId='com.whatsapp:id/message_text').count
    time.sleep(30)
    count_2=d(resourceId='com.whatsapp:id/message_text').count
    b=d.dump()
    if  a != b and count_1!=count_2:
        sendMessageOnWhatsApp("Hi")
def check_new_msg():
     counter=0
     while(counter<15):
         count=d(resourceId='com.whatsapp:id/message_text').count
         lastmessage_1=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
         time.sleep(2)
         lastmessage_2=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
         counter=counter+1
         if lastmessage_1!=lastmessage_2:
             break
     print(counter)
     if counter < 15:
         print("wait..")
         if lastmessage_2== '1':
             media("Sharee")
         if lastmessage_2=='2':
             media("Kurti")
             
openunseenmsg()   
#read_inside_msg()
#keepCheckingForNewMessage()
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

