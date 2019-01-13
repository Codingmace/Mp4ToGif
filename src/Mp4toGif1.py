import datetime
import os
import sys

from cv2 import imwrite, CAP_PROP_FRAME_COUNT, CAP_PROP_POS_AVI_RATIO, \
    CAP_PROP_POS_MSEC
import cv2
import ffmpy
import imageio

import numpy as np
import tinify 


tinify.key = "6QP9ymBx7CRyw6sWB1HFyBQC7Q9Z2jGQ"

''' First version with all the code. RAW and it sucks ''' 

def create_gif(filenames , duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename));
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)

"""
Splitting video into images
"""
    
vidcap = cv2.VideoCapture('./Buizel (12-3).MP4')
success,image = vidcap.read()
print(success)
#cv2.imwrite("frame.jpg", image) 

"""
Inputting what the information for compression details
"""
print("Now it is time for some compression input")
#input("Do you want to")
speedRate =  float(input("Input a number: "))

count = 0
framerate = vidcap.get(5)
print("framerate:", framerate)
framecount = vidcap.get(7)
print("framecount:", framecount)
vidcap.set(5,1)
newframerate = vidcap.get(5)
print("newframerate:", newframerate)
print("NUMBER OF FRAMES: ",vidcap.get(CAP_PROP_FRAME_COUNT))
framenumb = framecount * framerate

secTime = 1000 # Miliseconds in a second
#secTime = 100
pos = CAP_PROP_POS_AVI_RATIO
con = 0
fileNumb = 0 #File number count
while framenumb > (con * secTime):
#while CAP_PROP_POS_AVI_RATIO < 10:
    vidcap.set(cv2.CAP_PROP_POS_MSEC, (secTime * con))
#    vidcap.set(cv2.CAP_PROP_POS_MSEC,20000)      # just cue to 20 sec. position
    success,image = vidcap.read()
    print("RATIO TO END: ", vidcap.get(CAP_PROP_POS_AVI_RATIO))
    print("Position in video: ",vidcap.get(CAP_PROP_POS_MSEC))
    if success:
        cv2.imwrite("data6/frame" + str(fileNumb) + ".jpg", image)     # save frame as JPEG file
    # Compressing it now 6QP9ymBx7CRyw6sWB1HFyBQC7Q9Z2jGQ
#        source = tinify.from_file("data5/frames" + str(fileNumb) + ".jpg")
#        source.to_file("data5/frame" +str(fileNumb) + ".jpg")
        
    else:   # AT THE END OF THE FILEw
        break;
#    cv2.imshow("20sec",image)                # Shows the images
#    cv2.waitKey()                           # Waits for closing of window to continue
#    print(type(speedRate))
    con += 1 / speedRate;
    fileNumb+= 1
imagee = int(con * speedRate) # Number of last file using
print(str(imagee))
print(fileNumb)
#    create_gif(imagee ,2)
''' 
Creating the gif
'''
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
# ior = imageio.get_reader("./Buizel (12-3).MP4",mode='I')





outFold = 'data'
try:
    if not os.path.exists(outFold):
        os.makedirs(outFold)
except OSError:
    print ('Error: Creating directory of data')

if (True): # Used to save space
    exit();
currentFrame = 0
while(currentFrame < 10):
    # Capture frame-by-frame
#    for x in range(30000):
#        ret, frame = cap.read()
#    q = cap.get(currentFrame)

#    cap.grab()
#    for x in range(10000):
#        ret, frame = cap.read()
#    cap.get(currentFrame * 10000)
#        cap.read()
#    cap.set(1, currentFrame)
#        print(x)
    ret, frame = cap.read()
    
    # Saves image of the current frame in jpg file
    name = './data4/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1 # Added to 1 because want it to do less than max number of frames


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




"""
Turning the mp4 into images
"""
"""
images = []
filename = 'filename.mp4'
with imageio.get_writer('/path/to/movie.gif', mode='I') as writer:
    for filename in images:
        image = imageio.imread(filename)
        writer.append_data(image)
        
"""




"""
Converts the Gif into a MP4
"""
"""
startGif = 'input.gif'
outputFile = 'm.mp4'
ff = ffmpy.FFmpeg(inputs={startGif:None},outputs={outputFile:None})
ff.run()
"""