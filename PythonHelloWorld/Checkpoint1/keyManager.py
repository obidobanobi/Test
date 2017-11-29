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
    
    # rotate left (same as shift)
	t = word[0]
	word[0] = word[1]
	word[1] = word[2]
	word[2] = word[3]
	word[3] = t

	# S-Box four bytes:
	word[0] = sbox[word[0]]; word[1] = sbox[word[1]]
	word[2] = sbox[word[2]]; word[3] = sbox[word[3]]

	# RCon
	word[0] ^= rcon[i]
	return word

def expandKey(key):
    # TODO STUFF................
    return key
