########################################################################################
# main.py
# from here, all other methods will be called.
########################################################################################

########################################################################################
# imports
from AES256 import *
from readBlockFile import *
from readKeyFile import *
########################################################################################

key = getKey("..\\testKey")
block = getBlock("..\\text & test.txt")

encrypted = encrypt(block, key)
print (encrypt)


