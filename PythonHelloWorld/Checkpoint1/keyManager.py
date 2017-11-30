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
    # TODO STUFF................
    return key
