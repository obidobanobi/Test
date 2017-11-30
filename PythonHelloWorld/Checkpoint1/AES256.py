import AES256
import binascii
from readKeyFile import *
from readBlockFile import *
from keyManager import *
from AddRoundKey import *
from SubBytes import *
from RowShifter import *
from columnMixer import *

def encrypt(block, key):
    expandedKey = expandKey(key)

    roundKey = createRoundKey(expandedKey, 0)
    block = addRoundKey(roundKey, block)

    for i in range(1, 14):
        roundKey = createRoundKey(expandedKey, i)
        subBytes(block)
        shiftRows(block)
        mixColumns(block)
        addRoundKey(block, roundKey)

    roundKey = createRoundKey(expandedKey,14)
    subBytes(block)
    shiftRows(block)
    addRoundKey(block, roundKey)

    return block

key = getKey("..\\testKey")
block = getBlock("..\\testBlock")

print (block)
encryptedBlock = encrypt(block, key)
print (encryptedBlock)