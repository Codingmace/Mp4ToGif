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
    '''
    if not (Path(ovfn.exists())): # Check to see if the file exist
        print("You nincompoop. That doesn't exist. Stupid you")
        exit()
    '''
    """ THIS PART DOESN"T WORK """
    if (not vidcap.read()): # Is it able to read the file
        print("Your a failure at life. That is not a readable file")
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
        duration = 1.0 / int(duration)
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
    outFold = 'data1' # Outputting folder
    try:
        if not os.path.exists(outFold):
            os.makedirs(outFold)
    except OSError:
        print ('Error: Creating directory of data')
    
    
    secTime = 1000
    speedRate = input("Input the number of frames you want")
    """ Need to add here  the speed rate checking to see if it is a number"""
    print(type(speedRate))
    speedRate = float(speedRate)
    ''' The Actual process of breaking up the MP4 '''
    con = 0 # Counter of the file
    fileNumb = 0 # The file Number
    while fileNumb > (con * secTime):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (secTime * con))
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
        filename = outFold+ "/frame" + str(i) + ".jpg"
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
