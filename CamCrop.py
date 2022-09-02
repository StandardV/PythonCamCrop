# importing the required packages
import pyautogui
import cv2
import numpy as np


print('this is camera')
# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose
# any value and experiment with it
fps = 500.0

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

#*********
# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL);cv2.namedWindow("Live2", cv2.WINDOW_NORMAL);cv2.namedWindow("Live3",cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 50, 150) #Open window size (This is optimal)
cv2.resizeWindow("Live2", 400, 200)
cv2.resizeWindow("Live3", 700,80)
#cv2.resizeWindow("Live3", 500, 100)
#this is simple, just width and height for the window

#*********
ws=True
while ws==True:
	# Take screenshot using PyAutoGUI
	img = pyautogui.screenshot(region=(100,997,70,60));img2= pyautogui.screenshot(region=(1569,1001,265,70));img3=pyautogui.screenshot(region=(170,1025,852,35))#170,1023
    #code work as above,NOTE that region follow order (x,y,width,height)
	#y=1000,1001,1025 if image high
	#y=997,997,1023 if image low
	
	# Convert the screenshot to a numpy array
	frame = np.array(img);frame2 = np.array(img2);frame3 = np.array(img3)
	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB);frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB);frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
	# Write it to the output file
	out.write(frame);out.write(frame2);out.write(frame3)
	# Optional: Display the recording screen
	cv2.imshow('Live', frame);cv2.imshow('Live2', frame2);cv2.imshow('Live3', frame3)
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		ws = False
#*********
# Release the Video writer
out.release()
# Destroy all windows
cv2.destroyAllWindows()
