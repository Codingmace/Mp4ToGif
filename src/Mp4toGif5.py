import datetime
import os
import shutil
import sys

from cv2 import imwrite, CAP_PROP_FRAME_COUNT, CAP_PROP_POS_AVI_RATIO, \
    CAP_PROP_POS_MSEC, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
import cv2
import ffmpy
import imageio

import moviepy.editor as mp
import numpy as np


def check(a):  # Checks to see if it is Yes or No
    return "y" in a or "Y" in a


def input_speed():
    print("I need to collect some data about our new file")
    print("If you need any help just enter define and I will print some help")
    initd = input("Do you want to compress The File ('Yes' or 'No') ")
#    initd = "Yes"
    duration = 0
    if not check(initd):  # If you want long videos
        print("Ok so that means its going to be long.")
        su = input("Are you sure about that??? ")
        if not check(su):
            print("Thank the lord. That is really not what this is used for")
            duration = input("How many frames do you want in a second? ")
        else:
            print("Fine be that way")
            duration = input("You want a frame every how many seconds? ")
    else:  # If you want Speed up videos
        print("This is going to be a compression, Fun. I love these")
        duration = input("How many frames do you want in a second? ")
#        duration = 4
    return int(duration)  # Return int for no problems


''' Add a preference input for this one '''


def output_exist(outFold):  # Make sure output folder exists
    try:
        if not os.path.exists(outFold):
            os.makedirs(outFold)
            print("It has been created. Your welcome")
        else:
            print("It already existed you silly")
    except OSError:
        print ('Error: Creating directory of data')
    return outFold


def main():
    secTime = 1000  # Number of MiliSeconds in Second
    videoFiles = []  # Files need to go through
    outFold = output_exist("data1")  # The output folder
    print("WELCOME TO MY MP4 TO GIF TO MP4 PROGRAM")
    print("WE CAN DO MORE THAN ONE FILE IN SPECIFIC CASES \n")
    numbFold = input("Are you doing a folder ('Yes' or 'No'): ")
#    numbFold = "No"
    if check(numbFold):
        print("Yeah we get to have some fun")
        vidfol = input("Input the folder name: ")  # Folder of Videos
        videoFiles = os.listdir(vidfol)
    else:
        print("What a shame not using to full potential. Ok so be it")
        videoFiles.append(input("Enter in the file path:  "))
    for ovfn in videoFiles:
        ovfn = ovfn.strip("\"")  # Takes care of parentheses
        filename, file_extension = os.path.splitext(ovfn)
        print(os.path.basename(filename))
        print(filename + " " + file_extension)
        if(os.path.isdir(ovfn)):  # Is a directory
            print("Well " + ovfn + " is a directory so I'll skip it")
            break
        else:  # is a file
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
        print("Total Number of Frames: ", totFrame)
        print("Now I know videos can be long and only want 2 min of a 10 min video")
        capSec = secLength
        print("Here is your chance. The video is " + str(capSec) + " seconds Long")
        clipped = input("Do you want to make it shorter?\nEnter 'Yes' or 'No': ")
#        clipped = "No"
        if check(clipped):
            print("Ok so shortening it. Good to hear")
            newCapSec = input("How many Seconds long do you want it (up to " + str(capSec) + " seconds")
            if(newCapSec > capSec):
                print("That doesn't work. Your trying to break my program. I'll Let you have one more try")
                newCapSec = input("How many Seconds long do you want it (up to " + str(capSec) + " seconds")
                if(newCapSec > capSec):
                    print("Well that didn't work so I guess it will not be shortened")
                else:
                    print("Good you came around and noticed your mistakes")
                    capSec = newCapSec
            else:
                print("Now just let me enter your new shortened length")
                capSec = newCapSec    
        con = 1  # Seconds Counter of the file
        smo = input("There are some benifits of this program.\nQuestion is would you like the file smoother")
        smoothRate = 1  # Smoothness of the file
        if check(smo):
            print("That is great. Number must be greater than one (I'm not checking)")
            smoothRate = input("How much smoother?")
        else:
            print("You have a lot of faith in a second but have it your way.")
        fileNumb = 0  # The File Number
        while(con < capSec):
#            print(str(capSec) + " "+ str(con))
            vidcap.set(cv2.CAP_PROP_POS_MSEC, (secTime * con))
            success, image = vidcap.read()
            if success:
                cv2.imwrite(outFold + "/frame" + str(fileNumb) + ".jpg", image)  # Save frame as JPG
            else:  # At the end of the file
                break 
            con += 1 / smoothRate
            fileNumb += 1
            
        """ Creating the GIF with the obtained Files """
        images = []  # Files in the folder
        print("Putting together " + str(fileNumb) + " files")
        for i in range(fileNumb):
            filenames = outFold + "/frame" + str(i) + ".jpg"
            images.append(imageio.imread(filenames));
        output_file = filename + ".gif"
        ''' Checking to see that it is a valid File Number '''
        fileWorks = False
        fileCount = 0
        while not fileWorks:
            try:
                if(os.path.exists(output_file)):
                    output_file = filename + str(fileCount) + ".gif"
                    fileCount += 1
                else:
                    fileWorks = True
            except OSError:
                print('Error when Creating the file name or something')

        imageio.mimsave(output_file, images, duration=duration)
        
        print("Now we have an option since the GIF is probably big")
        conback = input("Would you like to convert back to a MP4 File? ")
        if check(conback):  # Convert to MP4
            print("Ok I can convert the GIF to MP4\nJust give me a second")
            clip = mp.VideoFileClip(output_file)
            clip.write_videofile(filename + "_Lapse.MP4")
        else:
            print("OK. Was just trying to help out")
        print("Time to clean up")
        print("Releasing all the lose ends")
        vidcap.release()
        
        print("Destroying all the evidence. MWahhhahha")
        cv2.destroyAllWindows()
        
        print("WARNING: THIS IS GOING TO TAKE UP A LOT OF SPACE")
        cleanRemove = input("Do you want to delete the folder of all the images.")
        if check(cleanRemove):
            print("Cleaning out the files")
            shutil.rmtree(outFold)
            print("They have been removed as requested")
        else:
            print("It helps on space. Please reconsider")
            cleanRemove = input("Do you want to delete the folder of all the images.")
            if check(cleanRemove):
                print("The hard drive thanks you\nCleaning out the files")
                os.removedirs(outFold)
                print("They have been removed as requested")
            else:
                print("That is a shame. I was trying to save you space.")
    
        print("Welp, there we go. We are all done.")
        print("Continue with the rest of your day")
    
    print("Finally we are done")


main()
