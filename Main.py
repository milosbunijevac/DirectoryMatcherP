import os
import sys
import re
import shutil


####################################################


downpath ='C:/Users/DESKTOP-JSK22/Desktop'
ppath ='D:/P/'

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def numDirs():
    count = 0
    for f in os.listdir(ppath):
        count = count + 1
    return count

dirCount = numDirs()

for entry in os.scandir(downpath):
        finishFlag = 0
        test = entry.name
        pathcount = 0
        if test.lower().endswith(('.avi', '.mp4', '.flv', '.m4v', '.mpg', '.mpeg')):
            while pathcount < dirCount:
                if finishFlag == 1:
                    break
                else:
                    testpath = entry.path
                    test = test.replace("_"," ")
                    test = ("" + test + "")
                    testpatho = entry.path
                    testpath = testpath.replace("_"," ")
                    testpath = ("" + testpath + "")
                for entry2 in os.scandir(ppath):
                    if finishFlag == 1:
                        break
                    else:
                        pname = entry2.name
                        popath = entry2.path
                        wollow = popath + "/" + entry.name
                        if findWholeWord(pname)(test):
                            shutil.move(testpatho, wollow)
                            finishFlag = 1
                        else:
                            pathcount = pathcount + 1
                        if pathcount == dirCount:
                            if finishFlag == 0:
                                UserInput = input("Please enter a folder name for the actor of this file or enter skip to move to next file: \n" + test + "\n")
                                if "skip" not in UserInput:
                                    if os.path.isdir(ppath + "/" + UserInput):
                                        shutil.move(testpatho, ppath + UserInput)
                                    else:
                                        os.makedirs(ppath + "/" + UserInput)
                                        shutil.move(testpatho, ppath + UserInput)
