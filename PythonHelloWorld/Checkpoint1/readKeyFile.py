##########
#Method: getKey(filename)
#Create method that does the following:
#� File name: readKeyFile.py
#� Method name: getKey()
#� Input: String filename
#� Output: List of integers
#Code:
#import r e a d K e y F i l e
#key = getKey (�� t e s t K e y ��)
#print ( key )

import os





def getKey(filename):
    print (filename)

    # open file
    inputFile = open(filename, mode='r')
    # print file
    #print inputFile.read()
    print ("\n")

    # get file size
    fSize = os.path.getsize(filename) 
    # print file size
    print("length of image file: " + str(fSize/1048576) + " MB")
    
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

    #print (arrayA)








inputFile = raw_input("Enter file name: ")
getKey("..\\testKey")
#getKey("C:\\pythonprojects\\test.txt")
#print ("bye!")