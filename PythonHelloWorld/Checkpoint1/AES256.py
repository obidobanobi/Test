########################################################################################
# AES256.py
# Implements encrypt and decrypt functions
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################



########################################################################################
# imports
import binascii
from readKeyFile import *
from readBlockFile import *
from keyManager import *
from AddRoundKey import *
from SubBytes import *
from RowShifter import *
from columnMixer import *
from HelperMethods import printHex
########################################################################################




########################################################################################
# encrypts one block at a time and returns the encrypted block
def encrypt(block, key, iv):
    expandedKey = expandKey(key)    # expand the provided key

    for i in range(16):             # XOR the block with the provided IV
        block[i] = block[i] ^ iv[i]
    
    roundKey = createRoundKey(expandedKey, 0)   # create Roundkey 0 from the expanded key
    block = addRoundKey(roundKey, block)        # and add the RoundKey to the block

    for i in range(1, 14):                            
        roundKey = createRoundKey(expandedKey, i)   # create RoundKey 1 - 13
        block = subBytes(block)                     # and do subByte, 
        block = shiftRows(block)                    # shiftRows,
        block = mixColumns(block)                   # mixColumns 
        block = addRoundKey(block, roundKey)        # and addRoundKey for each

    roundKey = createRoundKey(expandedKey,14)   # create the last RoundKey (14) and
    block = subBytes(block)                     # do subBytes,
    block = shiftRows(block)                    # shiftRows
    block = addRoundKey(block, roundKey)        # and addRoundKey.
    
    return block
########################################################################################



########################################################################################
# decrypts one block at a time and returns the encrypted block
def decrypt(block, key, iv):
    expandedKey = expandKey(key)    # expand the provided key

    roundKey = createRoundKey(expandedKey,14)   #create the last RoundKey (14) and
    block = addRoundKey(block, roundKey)        # do addRoundKey,
    block = shiftRowsInv(block)                 # shiftRowsInv
    block = subBytesInv(block)                  # and subBytesInv.

    for i in range(13,0,-1): # 13 -> 1          
        roundKey = createRoundKey(expandedKey, i)   # create RoundKey 13 - 1
        block = addRoundKey(block, roundKey)        # and do addRoundKey,
        block = mixColumnsInv(block)                # mixColumnsInv,
        block = shiftRowsInv(block)                 # shiftRowsInv
        block = subBytesInv(block)                  # and subBytesInv for each

    roundKey = createRoundKey(expandedKey,0)    # create Roundkey 0 from the expanded key
    block = addRoundKey(block, roundKey)        # and add the RoundKey to the block

    for i in range(16):
        block[i] = block[i] ^ iv[i] # XOR the block with the provided IV

    return block
########################################################################################