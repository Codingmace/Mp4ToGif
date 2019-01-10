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
tinify.key = "6QP9ymBx7CRyw6sWB1HFyBQC7Q9Z2jGQ"  # Create API Key to compress images

# Compressing the video using Tinify
''' Check as may run into problems overriding a file '''


def tinyComp(filepath):
    source = tinify.from_file(filepath)
    source.to_file(filepath)

''' Number of Frames in a second '''
def input_speed():
    print("I need to collect some data about our new file")
    print("If you need any help just enter define and I will print some help")
    initd = input("Do you want to compress The File ('Yes' or 'No') ")
    duration = 0
    if ("n" in initd):  # If you want long videos
        print("Ok so that means its going to be long.")
        su = input("Are you sure about that??? ")
        if("n" in su):
            print("Thank the lord. That is really not what this is used for")
            duration = input("How many frames do you want in a second? ")
        else:
            print("Fine be that way")
            duration = input("You want a frame every how many seconds? ")
    else:  # If you want Speed up videos
        print("This is going to be a compression, Fun. I love these")
        duration = input("How many frames do you want in a second? ")
    return int(duration) # Return int for no problems

''' Add a preference input for this one '''
def output_exist(outFold): # Make sure output folder exists
    try:
        if not os.path.exists(outFold):
            os.makedirs(outFold)
            print("It has been created. Your welcome")
        else:
            print("It already existed you silly")
    except OSError:
        print ('Error: Creating directory of data')
        
    return outfold


def main():
    secTime = 1000 # Number of MiliSeconds in Second
    videoFiles = [] # Files need to go through
    outFold = output_exist("data1") # The output folder
    print("WELCOME TO MY MP4 TO GIF TO MP4 PROGRAM")
    print("WE CAN DO MORE THAN ONE FILE IN SPECIFIC CASES \n")
    numbFold = input("Are you doing a folder ('Yes' or 'No'): ")
    if "n" in numbFold:
        print("What a shame not using to full potential. Ok so be it")
        videoFiles = input("Enter in the file path:  ")
    else:
        print("Yeah we get to have some fun")
        vidfol = input("Input the folder name: ") # Folder of Videos
        videoFiles = os.listdir(vidfol)
#        print(str(videoFiles)[1:-1])
    for ovfn in videoFiles:
        filename, file_extension = os.path.splitext(ovfn)
        if(os.path.isdir(ovfn)): # Is a directory
            print("Well " + ovfn + " is a directory so I'll skip it")
            break;
        else: # is a file
            vidcap = cv2.VideoCapture(ovfn)
            if (not vidcap.read()[0]):  # Is it able to read the file
                print("Your a failure at life. That is not a readable file")
                print("Onward we go")
                break
        duration = 1 / input_speed()
        print("Now it is time for some properties")
        framerate = vidcap.get(5)
        framecount = vidcap.get(7)
        totFrame = framerate * framecount
        secLength = framecount / framerate
        print("Video Length (Seconds): ", secLength)
        print("Frame Rate: ", framerate)
        print("Frame Count: ", framecount)
        print("Frame Height: ", vidcap.get(CAP_PROP_FRAME_HEIGHT))
        print("Frame Width: ", vidcap.get(CAP_PROP_FRAME_WIDTH))
        print("Number of Frames: ", vidcap.get(CAP_PROP_FRAME_COUNT))
        print("Total Number of Frames: \n", totFrame)
        print("Now I know videos can be long and only want 2 min of a 10 min video")
        capSec = totFrame / secTime
        print("Here is your chance. The video is " + str(capSec) + " seconds Long")
        clipped = input("Do you want to make it shorter?\nEnter 'Yes' or 'No': ")
        if "y" in clipped:
            print("Ok so shortening it. Good to hear")
            newCapSec = input("How many Seconds long do you want it (up to "+ str(capSec) + " seconds")
            if(newCapSec > capSec):
                print("That doesn't work. Your trying to break my program. I'll Let you have one more try")
                newCapSec = input("How many Seconds long do you want it (up to "+ str(capSec) + " seconds")
                if(newCapSec > capSec):
                    print("Well that didn't work so I guess it will not be shortened")
                else:
                    print("Good you came around and noticed your mistakes")
                    capSec = newCapSec
            else:
                print("Now just let me enter your new shortened length")
                capSec = newCapSec    
        con = 1 # Seconds Counter of the file

        smoothRate = 1 # Smoothness of the file
        fileNumb = 0 # The File Number
        while(con < capSec):
            vidcap.set(cv2.CAP_PROP_MSEC, (secTime * smoothRate))
            success, image = vidcap.read()
            if success:
                cv2.imwrite(outFold+ "/frame"+str(fileNumb) + ".jpg", image) # Save frame as JPG
            else: # At the end of the file
                break 
            con+= 1
            fileNumb += 1
            
            
        """ Creating the GIF with the obtained Files """
        images = []  # Files in the folder
        print("Putting together " +str(fileNumb)+ " number of files")
        for i in range(fileNumb):
            filename = outFold + "/frame" + str(i) + ".jpg"
            images.append(imageio.imread(filename));
        output_file = filename + ".gif"
        
        
        
        
        
        
    '''
    # Editting this for speedrate
    con = 1  # Counter of the file
    fileNumb = 0  # The file Number
    while con < capSec:
     #   print("CON " + str(con))
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (secTime * con))
        if con > 130:  # For the longer files cut off
            print("You trying to break this. I'm cutting you off")
            break
        success, image = vidcap.read()
        if success:
            cv2.imwrite(outFold + "/frame" + str(fileNumb) + ".jpg", image)  # save frame as JPEG file
        else:  # At the end of the file
            break
        con += 1
        fileNumb += 1  # Next frame
        '''
    """ Creating the GIF with the obtained Files """
    '''
    images = []  # Files in the folder
    print(fileNumb)
    for i in range(fileNumb):
        filename = outFold + "/frame" + str(i) + ".jpg"
        images.append(imageio.imread(filename));
    output_file = ovfn + ".gif"  # Lazy But Doesn't Work
    '''
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
    
    imageio.mimsave(output_file, images, duration=duration)
    print("Time to clean up")
    print("Releasing all the lose ends")
    vidcap.release()
    print("Destroying all the evidence. MWahhhahha")
    cv2.destroyAllWindows()
    print("Welp, there we go. We are all done.")
    print("Continue with the rest of your day")
    
    ''' Converting the file back to mp4 '''
    clip = mp.VideoFileClip(output_file)
    clip.write_videofile("testout.mp4")
    
    print("WARNING: THIS IS GOING TO TAKE UP A LOT OF SPACE")
    cleanRemove = input("Do you want to delete the folder of all the images.")
    os.removedirs(outFold)



''' This May not work '''
def cleanup():
    os.removedirs(outFold)

main()
