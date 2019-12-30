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
#getXmlSnapshot()
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
    count=d(resourceId='com.whatsapp:id/message_text').count
    lastmessage=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
    sendMessageOnWhatsApp(" welcome to queen's press : 1,2")
    check_new_msg()

#sendMessageOnWhatsApp(read_message())
def sharee ():
     d(resourceId="com.whatsapp:id/input_attach_button").click()
     d(text="Gallery").click()
     d(text="Download").click()
     count=d(className="android.widget.ImageView").count
     #print(count)
     d(resourceId="com.whatsapp:id/menuitem_select_multiple").click()
     for i in range(1,6):
             d(className="android.widget.ImageView",instance=i).click()
             time.sleep(1)
     d(text="OK").click()
     d(resourceId="com.whatsapp:id/send").click()
def moresharee():
     d(resourceId="com.whatsapp:id/input_attach_button").click()
     d(text="Gallery").click()
     d(text="Download").click()
     count=d(className="android.widget.ImageView").count
     #print(count)
     d(resourceId="com.whatsapp:id/menuitem_select_multiple").click()
     for i in range(7,8):
             d(className="android.widget.ImageView",instance=i).click()
             time.sleep(1)
     d(text="OK").click()
     d(resourceId="com.whatsapp:id/send").click()
    
def kurti ():
     d(resourceId="com.whatsapp:id/input_attach_button").click()
     d(text="Gallery").click()
     d(text="Download").click()
     count=d(className="android.widget.ImageView").count
     d(resourceId="com.whatsapp:id/menuitem_select_multiple").click()
     for i in range(9,14):
         d(className="android.widget.ImageView",instance=i).click()
         time.sleep(1)
     d(text="OK").click()
     d(resourceId="com.whatsapp:id/send").click()
def morekurti():
     d(resourceId="com.whatsapp:id/input_attach_button").click()
     d(text="Gallery").click()
     d(text="Download").click()
     count=d(className="android.widget.ImageView").count
     print(count)
     d(resourceId="com.whatsapp:id/menuitem_select_multiple").click()
     for i in range(15,18):
             d(className="android.widget.ImageView",instance=i).click()
             time.sleep(1)
     d(text="OK").click()
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
     count=d(resourceId='com.whatsapp:id/message_text').count
     lastmessage_1=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
     print(lastmessage_1)
     print(".....")
     while(counter<30):
         count=d(resourceId='com.whatsapp:id/message_text').count
         time.sleep(2)
         lastmessage_2=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
         print(lastmessage_2)
         counter=counter+1
         if lastmessage_1!=lastmessage_2:
             break
     print(counter)
     if counter < 30:
         print("wait..")
         if lastmessage_2== '1':
             sharee()
             sendMessageOnWhatsApp("To see More press 0")
             sendMessageOnWhatsApp("TO buy press the resource id")
             sendMessageOnWhatsApp("To see kurti press 2")
             counter_1=0
             count=d(resourceId='com.whatsapp:id/message_text').count
             lastmessage_1=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
             print(lastmessage_1)
             print("....")    
             while(counter_1<30):
                 time.sleep(2)
                 count=d(resourceId='com.whatsapp:id/message_text').count
                 lastmessage_2=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
                 print(lastmessage_2)
                 counter_1=counter_1+1
                 if lastmessage_1!=lastmessage_2:
                     break
             print(counter_1)
             if counter_1 < 30:
                 print("wait..")
                 print(lastmessage_2)
             if lastmessage_2== "0":
                 moresharee()
             if lastmessage_2 == "2":
                 kurti()
             else:
                sendMessageOnWhatsApp("Thanks For Buying Product")                 
         if lastmessage_2=='2':
             kurti()
             sendMessageOnWhatsApp("To see More press 0")
             sendMessageOnWhatsApp("TO buy press the resource id")
             sendMessageOnWhatsApp("To see sharee press 1")
             counter_1=0
             count=d(resourceId='com.whatsapp:id/message_text').count
             lastmessage_1=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
             print(lastmessage_1)
             print("....")    
             while(counter_1<30):
                 time.sleep(2)
                 count=d(resourceId='com.whatsapp:id/message_text').count
                 lastmessage_2=d(resourceId='com.whatsapp:id/message_text',instance=count-1).text
                 print(lastmessage_2)
                 counter_1=counter_1+1
                 if lastmessage_1!=lastmessage_2:
                     break
             print(counter_1)
             if counter_1 < 30:
                 print("wait..")
                 print(lastmessage_2)
                 if lastmessage_2== "0":
                     morekurti()
                 if lastmessage_2 == "2":
                     sharee()
                 else:
                     sendMessageOnWhatsApp("Thanks For Buying Product")    
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

