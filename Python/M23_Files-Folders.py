import os
myPath = "C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\MyFile.txt"

if os.path.exists(myPath):
    print("I found it!")
    if os.path.isfile(myPath):
        print("This is a file!")
        with open(myPath) as myFile: #Second argument is 'r' by default.
            print(myFile.read())
            print(myFile.closed)
        print(myFile.closed)

        with open(myPath, 'a') as myFile: #Use w to overwrite a file. Use a to append a text to an existing text.
            myFile.write("\nThis is appended by Python.")
    elif os.path.isdir(myPath):
        print("This is a directory!")
    else:
        print("This is not a file or directory.")
else:
    print("I couldn't found it :(.")

import shutil
# copyfile()    = copies contents of a file
# copy()        = copyfile() + permission mode + destination can be a directory
# copy2()       = copy() + copies metadata (file’s creation and modification times)
# All of these have 2 arguments.(source,destination)
shutil.copyfile("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\WebSite\\Batman - Lego Movie - First try(720P_HD).mp4","C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\SampleVideo.mp4")

#---------------------------------------------------------------------------------------------------------------------#
source = "C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\Java\\.vscode"
destination = "C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\.vscode"

if os.path.exists(source):
    if os.path.exists(destination):
        print("This directory exist in the destination location.")
    else:
        os.replace(source,destination)
else:
    if os.path.exists(destination):
        os.replace(destination,source)
    else:
        print("This file doesn't exist.")
try:
    os.mkdir("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\EmptyFolder")
    os.mkdir("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\non-EmptyFolder")
except Exception:
    pass
try:
    with open("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\non-EmptyFolder\\MyText.txt","x") as myFile:
        myFile.write("This file was created by Python.")
        print("MyText.txt has been created.")
except Exception:
    print("This file already exists.")
from time import sleep
sleep(5)
if os.path.exists("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\SampleVideo.mp4"):
    os.remove("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\SampleVideo.mp4")
else:
    print("This file does not exist.")

os.rmdir("EmptyFolder") #Cannot remove non-Empty ones.
shutil.rmtree("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\non-EmptyFolder") 

