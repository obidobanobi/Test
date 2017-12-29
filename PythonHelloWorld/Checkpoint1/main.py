########################################################################################
# main.py
# from here, all other methods will be called.
########################################################################################

########################################################################################
# imports
from HelperMethods import printHex
from AES256 import *
from readBlockFile import *
from readKeyFile import *
import time
########################################################################################

key = getKey("..\\testKey")
blocks = getBlock("..\\text & test.txt", False)
#blocks = getBlock("..\\lessismore.txt", False)
#blocks = getBlock("..\\yetanothertest.txt", False)

#print ("Original men padding size:" + str(len(blocks)))
#print ("Original:" + str(blocks[-1]))


# first iv
iv = [42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42] #2a, ...

encrypted = []
print ("encrypting...")
print ("Blocksize:" + str(len(blocks)))

start = time.time()
totalTime = time.time()


size = len(blocks)
i = 0.0

for block in blocks:
    if (i % 100 == 0 and i != 0):
        print ("Status: " + str(int((i / size)*100)) + "%\r"),

    iv = encrypt(block, key, iv)
    i += 1

    encrypted.append(iv)

elapsedTime = time.time() - start
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("Encryption Time: %d:%02d:%02d" % (h, m, s))
#print ("Encryption Time: " + str(elapsedTime))
#print ("Encrypted size:" + str(len(encrypted)))
#print ("Encrypted: " + str(encrypted[-1]))


file = open('..\\encrypted.txt', 'wb')
for i in encrypted:

    file.write(printHex(i))


file.close()


print ("\n\ndecrypting...")




blocks = getBlock("..\\encrypted.txt", True)

print ("Blocksize:" + str(len(blocks)))
#print ("Decrypted:" + blocks)

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
    #encrypted.append(iv)

elapsedTime = time.time() - start
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("Decryption Time: %d:%02d:%02d" % (h, m, s))
#print ("Encryption Time: " + str(elapsedTime))

#print (int(decrypted[-1][-1]))
decrypted[-1] = decrypted[-1][:len(decrypted[-1])-int(decrypted[-1][-1])]

#print ("Decrypted size:" + str(len(decrypted)))
#print ("Decrypted: " + str(decrypted[-1]))



file = open('..\\decrypted.txt', 'wb')
for i in decrypted:
    for j in i:
        #print (chr(j))
        file.write(chr(j))

elapsedTime = time.time() - totalTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print ("\n\nTotal Time: %d:%02d:%02d" % (h, m, s))

file.close()