########################################################################################
# main.py
# from here, all other methods will be called.
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################

########################################################################################
# imports
from HelperMethods import printHex
from AES256 import *
from readBlockFile import *
from readKeyFile import *
import time
########################################################################################


########################################################################################
# Initialize variables and get input text

# input text 
key = getKey("..\\testKey")
#blocks = getBlock("..\\text & test.txt", False)
blocks = getBlock("..\\lessismore.txt", False)
#blocks = getBlock("..\\yetanothertest.txt", False)

# first iv
iv = [42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42] 

# create empty list for encrypted data
encrypted = []

# reset timers
start = time.time()
totalTime = time.time()

# save the size of the file
size = len(blocks)
########################################################################################



########################################################################################
# print information
print ("Encrypting...")
print ("Blocksize:" + str(len(blocks)))
########################################################################################



########################################################################################
# Calculate percent 
# ...
########################################################################################
i = 0.0 # reset percent counter

for block in blocks:
    if (i % 100 == 0 and i != 0):
        print ("Status: " + str(int((i / size)*100)) + "%\r"),

    iv = encrypt(block, key, iv)
    i += 1

    encrypted.append(iv)
########################################################################################


elapsedTime = time.time() - start
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("Encryption Time: %d:%02d:%02d" % (h, m, s))


file = open('..\\encrypted.txt', 'wb')
for i in encrypted:
    file.write(bytearray(i))


file.close()


print ("\n\ndecrypting...")




blocks = getBlock("..\\encrypted.txt", True)

print ("Blocksize:" + str(len(blocks)))

decrypted = []
iv = [42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42]

start = time.time()
i = 0.0
for block in blocks:
    if (i % 100 == 0 and i != 0):
        print ("Status: " + str(int((i / size)*100)) + "%\r"),

    # iv = 
    decrypted.append(decrypt(block, key, iv))
    i += 1
    iv = block

elapsedTime = time.time() - start
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("Decryption Time: %d:%02d:%02d" % (h, m, s))


decrypted[-1] = decrypted[-1][:len(decrypted[-1])-int(decrypted[-1][-1])]





file = open('..\\decrypted.txt', 'wb')
for i in decrypted:
    for j in i:
        file.write(chr(j))

elapsedTime = time.time() - totalTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("\n\nTotal Time: %d:%02d:%02d" % (h, m, s))

file.close()