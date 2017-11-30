import os
from sbox import *      # sbox list
from sboxInv import *   # Inverted sbox list
from rcon import*       # rcon list
from copy import deepcopy   # to copy list by value, not reference

# keyScheduleCore
# Input: 4 Byte word and Iteration Number 
# Output: 4 Byte word.
#
# expandKey
# Input: 256 bit key 
# Output: extended 240 Byte key

def  keyScheduleCore(word, i):
    
    tmp = deepcopy(word)
    # rotate left (same as shift)

    tmp[0] = word[1]
    tmp[1] = word[2]
    tmp[2] = word[3]
    tmp[3] = word[0]

	# S-Box four bytes:
    tmp[0] = sbox[tmp[0]]; tmp[1] = sbox[tmp[1]]
    tmp[2] = sbox[tmp[2]]; tmp[3] = sbox[tmp[3]]

	# RCon
    tmp[0] ^= rcon[i]
    return tmp

def expandKey(key):

    # The first 32 bytes are the original key:
    expandedKeys = deepcopy(key)

    # Variables:
    bytesGenerated = 32 # We've generated 32 bytes so far
    rconIteration = 1   # RCon Iteration begins as 1
    temp = [0]*4          # Temporary storage
    

    while (len(expandedKeys) < 240):   # b has a value of 240 for 256-bit keys 
        temp = expandedKeys[-4:]
        enBraVariabel = expandedKeys[-32:-28]

        temprCon = keyScheduleCore(temp, rconIteration)
        rconIteration += 1

        tempXOR = [0]*4

        # XOR temp with (bytesGenerates-32), and store in expandedKeys:
        for a in range (0, 4):
           tempXOR[a] = enBraVariabel[a] ^ temprCon[a]
           
        
        if (len(expandedKeys) < 240):                                  
            expandedKeys.extend(tempXOR)

        #print(expandedKeys[-32:8])
        for b in range (0, 3):
            enBraVariabel = expandedKeys[-32:-28]

            temprCon = deepcopy(tempXOR)

            for a in range (0, 4):
                tempXOR[a] = enBraVariabel[a] ^ temprCon[a]
            
            if (len(expandedKeys) < 240):                                  
                expandedKeys.extend(tempXOR)
   



        for z in range(0, 4):
            tempXOR[z] = sbox[tempXOR[z]]
        
        enBraVariabel = expandedKeys[-32:-28]
        temprCon = deepcopy(tempXOR)
        for a in range (0, 4):
            tempXOR[a] = enBraVariabel[a] ^ temprCon[a]
        


        if (len(expandedKeys) < 240):                                  
            expandedKeys.extend(tempXOR)
        



        #print(expandedKeys[-32:8])
        for b in range (0, 3):
            enBraVariabel = expandedKeys[-32:-28]
            #print("")
            #print(expandedKeys)
            temprCon = deepcopy(tempXOR)

            for a in range (0, 4):
                tempXOR[a] = enBraVariabel[a] ^ temprCon[a]
            if (len(expandedKeys) < 240):                                  
                expandedKeys.extend(tempXOR)




    return expandedKeys

def createRoundKey(expandedKey, n):
    return expandedKey[n*16:n*16+16]