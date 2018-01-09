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
blocks = getBlock("..\\text & test.txt", False)

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
# Encrypt the text and calculate percent 
i = 0.0 # reset percent counter

for block in blocks:
    # encrypt one block at a time and calculate and print the percent completed
    if (i % 100 == 0 and i != 0):
        print ("Status: " + str(int((i / size)*100)) + "%\r"),
    
    # encrypt the current block and save the block as the next iv
    iv = encrypt(block, key, iv)
    i += 1

    encrypted.append(iv) # add the encrypted block to the list
########################################################################################



########################################################################################
# calculated the elapsed time and print the result
elapsedTime = time.time() - start
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("Encryption Time: %d:%02d:%02d" % (h, m, s))
########################################################################################



########################################################################################
# create a file and save the encrypted text
file = open('..\\encrypted.txt', 'wb')
for i in encrypted:
    file.write(bytearray(i))

file.close()
########################################################################################



########################################################################################
# open the encrypted file for decryption and print information
blocks = getBlock("..\\encrypted.txt", True)    # get the size of the encrypted file
print ("\n\ndecrypting...")
print ("Blocksize:" + str(len(blocks)))
########################################################################################



########################################################################################
# Initialize variables and get input text

# create empty list for decrypted data
decrypted = []

# reset the iv value
iv = [42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42]

# reset the timer and percent counter
start = time.time()
########################################################################################



########################################################################################
# decrypt the text and calculate percent 
i = 0.0 # reset percent counter

# decrypt one block at a time and calculate and print the percent completed
for block in blocks:
    if (i % 100 == 0 and i != 0):
        print ("Status: " + str(int((i / size)*100)) + "%\r"),
    
    # decrypt the current block and save it to the decrypted list
    decrypted.append(decrypt(block, key, iv))
    i += 1
    iv = block  # the block is the iv for the next iteration
########################################################################################



########################################################################################
# calculated the elapsed time and print the result
elapsedTime = time.time() - start
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("Decryption Time: %d:%02d:%02d" % (h, m, s))
########################################################################################



# remove the padded information from the end of the file
decrypted[-1] = decrypted[-1][:len(decrypted[-1])-int(decrypted[-1][-1])]




########################################################################################
# create a file and save the decrypted text
file = open('..\\decrypted.txt', 'wb')
for i in decrypted:
    for j in i:
        file.write(chr(j))

file.close()
########################################################################################



########################################################################################
# calculated the total elapsed time and print the result
elapsedTime = time.time() - totalTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("\n\nTotal Time: %d:%02d:%02d" % (h, m, s))
########################################################################################