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

def getBlock(filename, decrypt):
    """
	Takes a block as parameter. Output list of integers.
	"""

    # open file
    if (decrypt == False):
        inputFile = open(filename, mode='rb')
        step = 1
    else:
        inputFile = open(filename, mode='r')
        step = 2

    # get file size
    fSize = os.path.getsize(filename) 
    # print file size
    #print("length of image file: " + str(fSize) + "bytes / " + str(fSize/1048576) + " MB")
    
    #We want the key to be transformed into a list of hexadecimal integers
    offset = 0
    
    arrayA = []
    blocks = []
    

    while(offset <= (fSize - step)):
    
        if (decrypt == False):
            if (offset != 0 and offset % 16 == 0):
                blocks.append(arrayA)
                arrayA = []
            arrayA.append(int(hex(ord(inputFile.read(step))),0))
            
        else:
            #print (len(arrayA))
            if (offset != 0 and offset % 32 == 0):
                blocks.append(arrayA)
                arrayA = []
            arrayA.append(int("0x"+inputFile.read(step),0)) 
            #print (arrayA[-1])
        #if (offset == 920L):
        #    print ("skmsdkm")

        offset +=step

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

    else:
        blocks.append(arrayA)
    #else:
    #    arrayA.append(int("0x"+inputFile.read(step),0))
    #    blocks.append(arrayA)

    #for i in arrayA:
    #    print(int("0x"+i,0))
    #print arrayA
    #print (len(blocks))
    return blocks








#inputFile = raw_input("Enter file name: ")
#getBlock("..\\testBlock")

# if print outside method:
#block = getBlock("..\\testBlock")
#print ("\nPrint outside method:\n")
#print (block)