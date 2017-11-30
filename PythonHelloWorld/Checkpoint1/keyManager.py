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

    expandedKeys = []
    # The first 32 bytes are the original key:
    for j in key:
        expandedKeys.append(j)

    # Variables:
    bytesGenerated = 32 # We've generated 32 bytes so far
    rconIteration = 1   # RCon Iteration begins as 1
    temp = [0]*4          # Temporary storage for core

    while (bytesGenerated < 208):   # b has a value of 176 for 128-bit keys, 208 for 192-bit keys, and 240 for 256-bit keys 
        # Read 4 bytes for the core
        for k in range(0, 4):
            temp[k] = expandedKeys[k + bytesGenerated - 4]

        # Perform the core once for each 32 byte key:
        if (bytesGenerated % 16 == 0):
            keyScheduleCore(temp, rconIteration)
            rconIteration += 1


        # XOR temp with (bytesGenerates-16), and store in expandedKeys:
        for a in range (0, 4):
            expandedKeys[bytesGenerated] = expandedKeys[bytesGenerated -16] ^ temp[a];
            bytesGenerated +=1



    # TODO STUFF................
    return expandedKeys




#void KeyExpansion(unsigned char* inputKey, unsigned char* expandedKeys)
#{
#	// The first 16 bytes are the original key:
#	for (int i = 0; i < 16; i++)
#		expandedKeys[i] = inputKey[i];

#	// Variables:
#	int bytesGenerated = 16;	// We've generated 16 bytes so far
#	int rconIteration = 1;		// RCon Iteration begins as 1
#	unsigned char temp[4];		// Temporary storage for core

#	while (bytesGenerated < 176)
#	{
#		// Read 4 bytes for the core:
#		for (int i = 0; i < 4; i++)
#			temp[i] = expandedKeys[i + bytesGenerated - 4];

#		// Perform the core once for each 16 byte key:
#		if (bytesGenerated % 16 == 0)
#		{
#			KeyExpansionCore(temp, rconIteration);
#			rconIteration++;
#		}

#		// XOR temp with (bytesGenerates-16), and store in expandedKeys:
#		for (unsigned char a = 0; a < 4; a++)
#		{
#			expandedKeys[bytesGenerated] =
#				expandedKeys[bytesGenerated - 16] ^ temp[a];
#			bytesGenerated++;
#		}
#	}
#}


#The first n bytes of the expanded key are simply the encryption key.
#The rcon iteration value i is set to 1
#Until we have b bytes of expanded key, we do the following to generate n more bytes of expanded key: 

#We do the following to create 4 bytes of expanded key: 
#We create a 4-byte temporary variable, t

#We assign the value of the previous four bytes in the expanded key to t

#We perform the key schedule core (see above) on t, with i as the rcon iteration value
#We increment i by 1

#We exclusive-OR t with the four-byte block n bytes before the new expanded key. This becomes the next 4 bytes in the expanded key
#We then do the following three times to create the next twelve bytes of expanded key: 
#We assign the value of the previous 4 bytes in the expanded key to t
#We exclusive-OR t with the four-byte block n bytes before the new expanded key. This becomes the next 4 bytes in the expanded key
#If we are processing a 256-bit key, we do the following to generate the next 4 bytes of expanded key: 
#We assign the value of the previous 4 bytes in the expanded key to t
#We run each of the 4 bytes in t through Rijndael's S-box
#We exclusive-OR t with the 4-byte block n bytes before the new expanded key. This becomes the next 4 bytes in the expanded key.
#If we are processing a 128-bit key, we do not perform the following steps. If we are processing a 192-bit key, we run the following steps twice. If we are processing a 256-bit key, we run the following steps three times: 
#We assign the value of the previous 4 bytes in the expanded key to t
#We exclusive-OR t with the four-byte block n bytes before the new expanded key. This becomes the next 4 bytes in the expanded key
