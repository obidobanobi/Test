import AES256
import binascii
from readKeyFile import *
from readBlockFile import *
from keyManager import *
from AddRoundKey import *
from SubBytes import *
from RowShifter import *
from columnMixer import *
from HelperMethods import printHex

def encrypt(block, key):
    expandedKey = expandKey(key)

    roundKey = createRoundKey(expandedKey, 0)
    block = addRoundKey(roundKey, block)
    #print ("Round 0")
    #printHex (block)

    for i in range(1, 14):
        roundKey = createRoundKey(expandedKey, i)
        block = subBytes(block)
        block = shiftRows(block)
        block = mixColumns(block)
        block = addRoundKey(block, roundKey)
        #print ("Round:", i)
        #printHex (block)

    roundKey = createRoundKey(expandedKey,14)
    block = subBytes(block)
    block = shiftRows(block)
    block = addRoundKey(block, roundKey)
    
    #print ("Round 14")
    #printHex (block)

    return block

key = getKey("..\\testKey")
block = getBlock("..\\testBlock")

printHex (block)
print (block)
encryptedBlock = encrypt(block, key)
printHex (encryptedBlock)
print (encryptedBlock)
print ("\n\n\n")


