########################################################################################
# readBlockFile.py
# The method getBlock() takes a filename and a boolean (decrypt) as parameters
# and return a block
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################



########################################################################################
# imports 
import os
########################################################################################


########################################################################################
# Takes a filename and a boolean (decrypt) as parameters and return a block
def getBlock(filename, decrypt):

    # open file
    inputFile = open(filename, mode='rb')
    step = 1

    fSize = os.path.getsize(filename) # get the file size
    offset = 0 
    arrayA = []
    blocks = []
    
    while(offset <= (fSize - step)):
    
        # if encryption:
        if (decrypt == False):
            if (offset != 0 and offset % 16 == 0):
                blocks.append(arrayA)
                arrayA = []
            arrayA.append(int(hex(ord(inputFile.read(step))),0))
         
        # if decryption:
        else:
            if (offset != 0 and offset % 16 == 0):
                blocks.append(arrayA)
                arrayA = []
            arrayA.append(int(hex(ord(inputFile.read(step))),0))

        offset +=step

    # if encryption:
    if (decrypt == False):
        if (len(arrayA) == 16):
            blocks.append(arrayA)
            arrayA = []
        if(len(arrayA) > 0):
            padValue = 16-(len(arrayA))
            while(len(arrayA) > 0 and len(arrayA) < 16):
                arrayA.append(padValue)
            blocks.append(arrayA)
        else:
            blocks.append( [16,16,16,16,
                            16,16,16,16,
                            16,16,16,16,
                            16,16,16,16] )

    # if decryption:
    else:
        blocks.append(arrayA)
    
    return blocks