#In the file testBlock, a test block is provided. testBlock is in plain text but
#represents bytes. Since all versions of AES operates on blocks with the fix size
#of 128 bit it corresponds to a block that is 128/8 bytes long. That is, the block
#is 16 byte long, where each byte is encoded as two characters in hex-decimals.
#That is, the 128 bit block is represented as a string of length 32.
#In reality blocks have the format of a 4x4 matrix. My implementation uses
#a virtual matrix that is simply a list. Where the first 4 values are represented
#as the first column, the next 4 as the second column and so on. You can decide
#your format of the block yourselves.

import os

def getBlock(filename):
    """
	Takes a block as parameter. Output list of integers.
	"""
    print (filename)

    # open file
    inputFile = open(filename, mode='r')
    # print file
    #print inputFile.read()
    print ("\n")

    # get file size
    fSize = os.path.getsize(filename) 
    # print file size
    print("length of image file: " + str(fSize) + "bytes / " + str(fSize/1048576) + " MB")
    
    #We want the key to be transformed into a list of hexadecimal integers
    offset = 0
    step = 2
    arrayA = []
    while(offset <= (fSize - step)):
        arrayA.append(int("0x"+inputFile.read(step),0))      
        offset +=step

    #for i in arrayA:
    #    print(int("0x"+i,0))
    print arrayA
    #return arrayA #if print is outside method

inputFile = raw_input("Enter file name: ")
getBlock("..\\testBlock")

# if print outside method:
#block = getBlock("..\\testBlock")
#print ("\nPrint outside method:\n")
#print (block)