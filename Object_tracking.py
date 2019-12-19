import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time


class Colour(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (480, 320)
        self.camera.framerate = 30
        self.rawCapture = PiRGBArray(self.camera, size=(480, 320))

    def detect_red(self):
        time.sleep(0.5)
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            #Red Color Range
            low=np.array([140,150,0])
            high=np.array([180,255,255])
            mask=cv2.inRange(hsv,low,high)
            count=0
            left=0
            right=0
            for i in range(320): #searching white pixels in the mask
                for j in range(480):
                    if np.all(mask[i, j] == (255, 255, 255)):
                        count +=1
                        if j<160:
                            right +=1 #reverse
                        elif j>320:
                            left +=1
            middle=count-(left+right)
    
            if count>200:
                if left>right:
                    if left>middle:
                        self.rawCapture.truncate(0)
                        return ["red","left"]
                    else:
                        self.rawCapture.truncate(0)
                        return ["red","middle"]
                else:
                    if right>middle:
                        self.rawCapture.truncate(0)
                        return ["red","right"]
                    else:
                        self.rawCapture.truncate(0)
                        return ["red","middle"]
            self.rawCapture.truncate(0)
            return [0,0]
            
        cv2.destroyAllWindows()

    def detect_blu(self):
        time.sleep(0.5)
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            #Blue Color Range
            low=np.array([94,80,2])
            high=np.array([126,255,255])
            mask=cv2.inRange(hsv,low,high)
            count=0
            left=0
            right=0
            for i in range(320):
                for j in range(480):
                    if np.all(mask[i, j] == (255, 255, 255)):
                        count +=1
                        if j<160:
                            right +=1
                        elif j>320:
                            left +=1
            middle=count-(left+right)
    
            if count>100:
                if left>right:
                    if left>middle:
                        self.rawCapture.truncate(0)
                        return ["blue","left"]
                    else:
                        self.rawCapture.truncate(0)
                        return ["blue","middle"]
                else:
                    if right>middle:
                        self.rawCapture.truncate(0)
                        return ["blue","right"]
                    else:
                        self.rawCapture.truncate(0)
                        return ["blue","middle"]
            self.rawCapture.truncate(0)
            return [0,0]
            
        cv2.destroyAllWindows()


    def detect_grn(self):
        time.sleep(0.5)
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            #Green Color Range
            low=np.array([25,125,72])
            high=np.array([100,255,255])
            mask=cv2.inRange(hsv,low,high)
            count=0
            left=0
            right=0
            for i in range(320):
                for j in range(480):
                    if np.all(mask[i, j] == (255, 255, 255)):
                        count +=1
                        if j<160:
                            right +=1
                        elif j>320:
                            left +=1
            middle=count-(left+right)
    
            if count>200:
                if left>right:
                    if left>middle:
                        self.rawCapture.truncate(0)
                        return ["green","left"]
                    else:
                        self.rawCapture.truncate(0)
                        return ["green","middle"]
                else:
                    if right>middle:
                        self.rawCapture.truncate(0)
                        return ["green","right"]
                    else:
                        self.rawCapture.truncate(0)
                        return ["green","middle"]
            self.rawCapture.truncate(0)
            return [0,0]
            
        cv2.destroyAllWindows()
