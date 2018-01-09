########################################################################################
# readKeyFile.py
# Read a file, extract and return the key
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################



########################################################################################
# imports
import os
########################################################################################



########################################################################################
# returns the key from the provided file
def getKey(filename):

    # open file
    inputFile = open(filename, mode='r')

    # get file size
    fSize = os.path.getsize(filename) 

    # initialize values
    offset = 0
    step = 2
    key = []

    while(offset <= (fSize - step)):
        key.append(int("0x"+inputFile.read(step),0))    # add the hexadecimal values to the list 
        offset +=step

    return key
########################################################################################