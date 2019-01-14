# Mp4ToGif
The goal of the program is to compress MP4 files. Note that the EXE file... DOESN'T WORK FOR SOME REASON. The files that do work is the zip file with a Pyc and Py file in them. Sorry but that problem was taking too long.

1. It creates images at certain points (User defined)
2. Puts the images together into a GIF (May be bigger than original MP4)
3. (Optional) Turns the GIF into MP4 for less space (Test file does 14 MB to 4 MB)
4. (Optional) Cleans up all the files.
# Testing Notes
There were so many problems on this and I ignored most but some were pretty big.
- If you are wanting top quality don't use it. By converting to GIf making it smaller and compresses the quality
- It can't be that long of a video or the GIF may not create. If it is over 500 frames is iffy. Over 1,000 won't work.
- Make sure the GIF isn't too big for the MP4 conversion
- Also being run with python there are a few softwares that you have to download
  - Opencv-python
  - Imageio
  - ffmpy
  - Moviepy
  - requests (Sub to moviepy)
# WARNINGS
- This is not a professional format as I was writting it quickly. Didn't add an __init__ because I am a Java programmer by heart.
# Improvements
- Create input and output folder targets
- Add a GUI (Python sucks so not going to happen)
- Being able to do the folder option
- Creating a preview beforehand
- Simplifying the modules as there are so many
- Making the software smaller.
