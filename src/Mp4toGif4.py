import datetime
import os
import sys
from cv2 import imwrite, CAP_PROP_FRAME_COUNT, CAP_PROP_POS_AVI_RATIO, \
    CAP_PROP_POS_MSEC, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
import cv2
import ffmpy
import imageio
import numpy as np
import moviepy.editor as mp

import tinify 
tinify.key = "6QP9ymBx7CRyw6sWB1HFyBQC7Q9Z2jGQ" # Create API Key to compress images

# Compressing the video using Tinify
''' Check as may run into problems overriding a file '''
def tinyComp(filepath):
    source = tinify.from_file(filepath)
    source.to_file(filepath)

def main():
    secTime = 1000
    ovfn = input("Enter in the file path:  ") # Original Video Filename
    vidcap = cv2.VideoCapture(ovfn)
    """ THIS PART DOESN"T WORK """
    print(vidcap.read()[0]) # Figured out that the first one is the boolean
    if (not vidcap.read()[0]): # Is it able to read the file
        print("Your a failure at life. That is not a readable file")
        exit()
    # Inputting speed
    print("I need to collect some data about our new file")
    print("If you need any help just enter define and I will print some help")
    initd =input("Do you want to compress The File ('Yes' or 'No') " )
#    initd = input("Do you want more than a frame every second ('Yes' or 'No'): ")
    duration = 0
    if ("n" in initd): # If you want long videos
        print("Ok so that means its going to be long.")
        duration = input("You want a frame every how many seconds? ")
    else: # If you want Speed up videos
        print("This is going to be a compression, Fun. I love these")
        duration = input("How many frames do you want in a second? ")
     #   duration = 1.0 / int(duration)
    duration = 1/ int(duration)
    print("Now we must consider the power of the software and Each Videos Properties")
    ''' Printing the properties of the video file '''
    framerate = vidcap.get(5)
    framecount = vidcap.get(7)
    totFrame = framerate* framecount
#    secLength = vidcap.get(CAP_PROP_POS_MSEC) / secTime #not right at all
    secLength = framecount / framerate
    print("Video Length (Seconds): ", secLength)
    print("Frame Rate: ", framerate)
    print("Frame Count: ", framecount)
    print("Frame Height: ", vidcap.get(CAP_PROP_FRAME_HEIGHT))
    print("Frame Width: ", vidcap.get(CAP_PROP_FRAME_WIDTH))
    print("Number of Frames: ", vidcap.get(CAP_PROP_FRAME_COUNT))
    print("Total Number of Frames: ", totFrame)
    ''' Creating the output folder if it doesn't exist '''
    outFold = 'data1' # Outputting folder
    try:
        if not os.path.exists(outFold):
            os.makedirs(outFold)
    except OSError:
        print ('Error: Creating directory of data')
    
    
#    secTime = 1000
    # Speed rate is duration so change to file number
#    speedRate = int(input("Input the number of frames you want: "))
  #  """ Need to add here the speed rate checking to see if it is a number"""
#    print(type(speedRate))
 #   speedRate = float(speedRate)
#    print(type(speedRate))

#    ''' NEED TO MODIFY PAST THIS POINT '''
    print("Do you want to have it shorter than usual")
    print("Example A 10 min file that you only want 2 min of")
    clipped = input("Enter 'Yes' or 'No'")
    capSec = totFrame / secTime
    if "y" in clipped:
        print("OK Clipping")
        print("Clipping")
        for i in range(10):
            print("Clipping.........")
        print("Plot Twist I can't do that right now")
        print("Come back later when this will actually work")
        exit()
    else:
        print("Awesome that makes it easier on me")
        print("Well on we go")
    
    # Editting this for speedrate
    con = 1 # Counter of the file
    fileNumb = 0 # The file Number
#    breakNumb = int(input("Input the number of frames you want: ")) # Number of frames
    while con  < capSec:
        print("CON " + str(con))
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (secTime * con))
        if con > 130: # For the longer files cut off
            print("You trying to break this. I'm cutting you off")
            break
        success, image = vidcap.read()
        if success:
            cv2.imwrite(outFold+"/frame" + str(fileNumb) + ".jpg", image)  # save frame as JPEG file
        else: # At the end of the file
            break
#        con+= 1 / speedRate # Adding time to next frame
#        con+= duration # Adding time to next frame
        con += 1
#        con+= 1 / speedRate # Adding time to next frame
        fileNumb += 1 # Next frame
    """ Creating the GIF with the obtained Files """
    images = []
    print(fileNumb)
    for i in range(fileNumb):
        filename = outFold+ "/frame" + str(i) + ".jpg"
        images.append(imageio.imread(filename));
#    print(images)
    output_file = ovfn + ".gif" # Lazy But Doesn't Work
    fileWorks = False
    fileCount = 0
    
    ''' Check to see if file Exists '''
    while not fileWorks:
        try:
            if os.path.exists(output_file):
                output_file = ovfn + str(fileCount) + ".gif"
                fileCount = fileCount + 1
            else:
                fileWorks = True
        except OSError:
            print ('Error: Creating directory of data')
    
    #output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)
    print("Time to clean up")
    print("Releasing all the lose ends")
    vidcap.release()
    print("Destroying all the evidence. MWahhhahha")
    cv2.destroyAllWindows()
    print("Welp, there we go. We are all done.")
    print("Continue with the rest of your day")

#clip = mp.VideoFileClip("mygif.gif")
#clip.write_videofile("myvideo.mp4")

main()
