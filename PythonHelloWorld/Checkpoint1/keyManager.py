########################################################################################
# keyManager.py
# The Key Schedule Core relies on both sbox[] and rcon[]
#
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################


########################################################################################
# imports 
import os
from sbox import *      # sbox list
from sboxInv import *   # Inverted sbox list
from rcon import*       # rcon list
from copy import deepcopy   # to copy list by value, not reference
########################################################################################


########################################################################################
# This method takes a 4 byte word and iteration number as input
# and outputs a 4 byte word.
# This operation is used as an inner loop in the key schedule.
def  keyScheduleCore(word, i):
    
    tmp = deepcopy(word)
    
    # rotate left (same as shift)
    tmp[0] = word[1]
    tmp[1] = word[2]
    tmp[2] = word[3]
    tmp[3] = word[0]

	# S-Box 4 bytes:
    tmp[0] = sbox[tmp[0]]; tmp[1] = sbox[tmp[1]]
    tmp[2] = sbox[tmp[2]]; tmp[3] = sbox[tmp[3]]

	# RCon
    tmp[0] ^= rcon[i]

    return tmp
########################################################################################


########################################################################################
# The round keys are created from the original key via an extension.
# The original key is 256 bit (32 bytes) but needs to be expanded to a 240 Byte key.
# This extension is done using Rijndael key schedule.
# This method takes a 256 bit key as input
# and outputs an extenden 240 byte key.
def expandKey(key):

    # Initialize variables:
    expandedKeys = deepcopy(key)        # The first 32 bytes are the original key
    bytesGenerated = 32                 # We've generated 32 bytes so far
    rconIteration = 1                   # RCon Iteration begins as 1
    temp = [0]*4                        # Temporary storage
    
    while (len(expandedKeys) < 240):    # 240 is the value for 256-bit keys 
        temp = expandedKeys[-4:]
        enBraVariabel = expandedKeys[-32:-28]

        temprCon = keyScheduleCore(temp, rconIteration)
        rconIteration += 1

        tempXOR = [0]*4

        # XOR temp with (bytesGenerates-32), and store in expandedKeys:
        for a in range (0, 4):
           tempXOR[a] = aHelpfulVariable[a] ^ temprCon[a]
           
        if (len(expandedKeys) < 240):                                  
            expandedKeys.extend(tempXOR)

        for b in range (0, 3):
            aHelpfulVariable = expandedKeys[-32:-28]

            temprCon = deepcopy(tempXOR)

            for a in range (0, 4):
                tempXOR[a] = aHelpfulVariable[a] ^ temprCon[a]
            
            if (len(expandedKeys) < 240):                                  
                expandedKeys.extend(tempXOR)
   
        for z in range(0, 4):
            tempXOR[z] = sbox[tempXOR[z]]
        
        aHelpfulVariable = expandedKeys[-32:-28]
        temprCon = deepcopy(tempXOR)
        for a in range (0, 4):
            tempXOR[a] = aHelpfulVariable[a] ^ temprCon[a]
        
        if (len(expandedKeys) < 240):                                  
            expandedKeys.extend(tempXOR)
        
        for b in range (0, 3):
            aHelpfulVariable = expandedKeys[-32:-28]
            temprCon = deepcopy(tempXOR)

            for a in range (0, 4):
                tempXOR[a] = aHelpfulVariable[a] ^ temprCon[a]
            if (len(expandedKeys) < 240):                                  
                expandedKeys.extend(tempXOR)

    return expandedKeys
########################################################################################


########################################################################################
# This method samples the expanded key.
def createRoundKey(expandedKey, n):
    return expandedKey[n*16:n*16+16]
########################################################################################
