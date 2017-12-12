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

# first iv
iv = [42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42,
      42, 42, 42, 42] #2a, ...

encrypted = []
print ("working encrypt()...")
for block in blocks:
    iv = encrypt(block, key, iv)

    encrypted.append(iv)

print ("working...")
for i in encrypted:
    printHex(i)


