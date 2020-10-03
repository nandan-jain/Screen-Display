from django.shortcuts import render
from django.http.response import StreamingHttpResponse
import numpy as np
import cv2
from mss import mss
import pyautogui
import json
from. import read_position

# Create your views here.

def index(request):
	return render(request, 'screenshare/index.html')

def video_feed(self):
    return StreamingHttpResponse(generate(), content_type= 'multipart/x-mixed-replace; boundary=frame')

def generate():

    
    bounding_box = read_position.json_co_ordinates

    sct = mss()

    while True:
        sct_img = sct.grab(bounding_box)
        output_frame = np.array(sct_img) 
        output_frame = cv2.putText(output_frame,'A',(pyautogui.position().x,pyautogui.position().y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
 
        ret, jpeg = cv2.imencode('.jpg', output_frame)        
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'+ bytearray(jpeg) + b'\r\n')
        # return StreamingHttpResponse(gen,content_type='multipart/x-mixed-replace; boundary=frame')
        