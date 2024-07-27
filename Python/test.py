import os
myPath = "/home/huseyin/Documents/Coding/Git/Python/ShellScriptTest.txt"

if os.path.exists(myPath):
    if os.path.isfile(myPath):
        with open(myPath, 'a') as myFile:
            myFile.write("\nThis is appended by ShellScript Python.")
