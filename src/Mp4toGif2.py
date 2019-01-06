import datetime
import os
import sys
from cv2 import imwrite, CAP_PROP_FRAME_COUNT, CAP_PROP_POS_AVI_RATIO, \
    CAP_PROP_POS_MSEC, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
import cv2
import ffmpy
import imageio
import numpy as np


import tinify 
tinify.key = "6QP9ymBx7CRyw6sWB1HFyBQC7Q9Z2jGQ" # Create API Key to compress images

# Compressing the video using Tinify
''' Check as may run into problems overriding a file '''
def tinyComp(filepath):
    source = tinify.from_file(filepath)
    source.to_file(filepath)






def main():
    ovfn = input("Enter in the file path:  ") # Original Video Filename
    vidcap = cv2.VideoCapture(ovfn);
    if (not vidcap.read()): # Is it able to read the file
        exit()
    # Inputting speed
    print("I need to collect some data about our new file")
    print("If you need any help just enter define and I will print some help")
    initd = input("Do you want more than one frame per second ('Yes' or 'No'): ")
    duration = 0
    if ("y" in initd): # If you want long videos
        print("Ok so that means its going to be long.")
        duration = input("You want a frame every how many seconds? ")
    else: # If you want Speed up videos
        print("This is going to be a compression, Fun. I love these")
        duration = input("How many frames do you want in a second? ")
        duration = 1 / duration
    duration = float(duration)
    print("Now we must consider the power of the software and Each Videos Properties")
    ''' Printing the properties of the video file '''
    framerate = vidcap.get(5)
    framecount = vidcap.get(7)
    print("Frame Rate: ", framerate)
    print("Frame Count: ", framecount)
    print("Frame Height: ", vidcap.get(CAP_PROP_FRAME_HEIGHT))
    print("Frame Width: ", vidcap.get(CAP_PROP_FRAME_WIDTH))
    print("Number of Frames: ", vidcap.get(CAP_PROP_FRAME_COUNT))
    print("Total Number of Frames: ", framecount * framerate)
    ''' Creating the output folder if it doesn't exist '''
    outFold = 'data6' # Outputting folder
    try:
        if not os.path.exists(outFold):
            os.makedirs(outFold)
    except OSError:
        print ('Error: Creating directory of data')
    
    
    
    speedRate = input("Input the number of frames you want")
    """ Need to add here  the speed rate checking to see if it is a number"""
    print(type(speedRate))
    speedRate = float(speedRate)
    ''' The Actual process of breaking up the MP4 '''
    con = 0 # Counter of the file
    fileNumb = 0 # The file Number
    while fileNumb < (con * secTime):
        if con > 200: # For the longer files cut off
            print("You trying to break this. I'm cutting you off")
            break
        success, image = vidcap.read()
        if success:
            cv2.imwrite(outFold+"/frame" + str(fileNumb) + ".jpg", image)  # save frame as JPEG file
        else: # At the end of the file
            break
        con+= 1/ speedRate # Adding time to next frame
        fileNumb += 1 # Next frame
    """ Creating the GIF with the obtained Files """
    images = []
    for i in range(fileNumb):
        filename = "data6/frame" + str(i) + ".jpg"
        images.append(imageio.imread(filename));
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)
    print("Time to clean up")
    print("Releasing all the lose ends")
    vidcap.release()
    print("Destroying all the evidence. MWahhhahha")
    cv2.destroyAllWindows()
    print("Welp, there we go. We are all done.")
    print("Continue with the rest of your day")

main()





'''    
"""
Splitting video into images
"""
vidcap = cv2.VideoCapture('./Buizel (12-3).MP4')

print(vidcap.read())

"""
Inputting what the information for compression details
"""
print("Now it is time for some compression input")
speedRate = float(input("Input a number: "))

count = 0


secTime = 1000  # Miliseconds in a second
pos = CAP_PROP_POS_AVI_RATIO
con = 0
fileNumb = 0  # File number count
while framenumb > (con * secTime):
# while CAP_PROP_POS_AVI_RATIO < 10: # Used when breaking for big files
    vidcap.set(cv2.CAP_PROP_POS_MSEC, (secTime * con))
    success, image = vidcap.read()
    print("RATIO TO END: ", vidcap.get(CAP_PROP_POS_AVI_RATIO))
    print("Position in video: ", vidcap.get(CAP_PROP_POS_MSEC))
    if success:
        cv2.imwrite("data6/frame" + str(fileNumb) + ".jpg", image)  # save frame as JPEG file
    # Compressing it now 6QP9ymBx7CRyw6sWB1HFyBQC7Q9Z2jGQ
#        source = tinify.from_file("data5/frames" + str(fileNumb) + ".jpg")
#        source.to_file("data5/frame" +str(fileNumb) + ".jpg")
        
    else:  # AT THE END OF THE FILEw
        break;
    con += 1 / speedRate;
    fileNumb += 1
imagee = int(con * speedRate)  # Number of last file using
print(str(imagee))
print(fileNumb)
'''
''' 
Creating the gif
'''
"""
duration = .1
images = []
for i in range(fileNumb):
    filename = "data6/frame" + str(i) + ".jpg"
    images.append(imageio.imread(filename));
output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
imageio.mimsave(output_file, images, duration=duration)

vidcap.release()
cv2.destroyAllWindows()

'''
Using OpenCV takes a mp4 video and produces a number of images.

Requirements
----
You require OpenCV 3.2 to be installed.

Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py

Which will produce a folder called data with the images. There will be 2000+ images for example.mp4.
'''

# Playing video from file:

cap = cv2.VideoCapture('./Buizel (12-3).MP4')

outFold = 'data'
try:
    if not os.path.exists(outFold):
        os.makedirs(outFold)
except OSError:
    print ('Error: Creating directory of data')

if (True):  # Used to save space
    exit();
currentFrame = 0
while(currentFrame < 10):
    ret, frame = cap.read()
    
    # Saves image of the current frame in jpg file
    name = './data4/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1  # Added to 1 because want it to do less than max number of frames

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
"""
