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
########################################################################################

key = getKey("..\\testKey")
blocks = getBlock("..\\text & test.txt", False)
#blocks = getBlock("..\\lessismore.txt", False)
#blocks = getBlock("..\\yetanothertest.txt", False)

print ("Original men padding size:" + str(len(blocks)))
print ("Original:" + str(blocks[-1]))

# first iv
iv = [42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42] #2a, ...

encrypted = []
print ("working encrypt()...")


size = len(blocks)
i = 0.0

for block in blocks:
    if (i % 100 == 0 and i != 0):
        print ("Status: " + str((i / size)*100) + "%")

    iv = encrypt(block, key, iv)
    i += 1

    encrypted.append(iv)

print ("Encrypted size:" + str(len(encrypted)))
print ("Encrypted: " + str(encrypted[-1]))



file = open('..\\encrypted.txt', 'w')
for i in encrypted:

    file.write(printHex(i))


file.close()


print ("working decryption...")




blocks = getBlock("..\\encrypted.txt", True)

print ("BLocksize:" + str(len(blocks)))
#print ("Decrypted:" + blocks)

decrypted = []
iv = [42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42]


i = 0
for block in blocks:
    if (i % 100 == 0 and i != 0):
        print ("Status: " + str((i / size)*100) + "%")

    # iv = 
    decrypted.append(decrypt(block, key, iv))
    i += 1
    iv = block
    #encrypted.append(iv)

print (int(decrypted[-1][-1]))
decrypted[-1] = decrypted[-1][:len(decrypted[-1])-int(decrypted[-1][-1])]

print ("Decrypted size:" + str(len(decrypted)))
print ("Decrypted: " + str(decrypted[-1]))



file = open('..\\decrypted.txt', 'w')
for i in decrypted:
    for j in i:
        #print (chr(j))
        file.write(chr(j))


file.close()