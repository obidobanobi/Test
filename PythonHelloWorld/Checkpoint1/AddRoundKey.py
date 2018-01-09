########################################################################################
# AddRoundKey.py
# addRoundKey() simply XOR each element of a roundkey with a block.
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################

########################################################################################
# imports 
from keyManager import *
from readKeyFile import *
from readBlockFile import *
########################################################################################

def addRoundKey(roundKey, block):   
    result = [None]*16
    for i in range(16):
        result[i] = roundKey[i] ^ block[i]
    return result