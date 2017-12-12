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
#blocks = getBlock("..\\text & test.txt")
blocks = getBlock("..\\lessismore.txt")
#blocks = getBlock("..\\yetanothertest.txt")


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

print ("working...")


j = 0
file = open('..\\encrypted.txt', 'a')
for i in encrypted:

    file.write(printHex(i))
    j += 1

    if (j % 16 == 0 and j != 0):
        file.write("\n")

file.close()

