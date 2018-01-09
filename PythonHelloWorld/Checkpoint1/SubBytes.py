########################################################################################
# SubBytes.py
# Implements subBytes and subBytesInv
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################



########################################################################################
# imports
import os
from copy import deepcopy   # to copy list by value, not reference
from sbox import *          # sbox list
from sboxInv import *       # Inverted sbox list
########################################################################################



########################################################################################
# Does subBytes on one block at a time using sbox, and returns the result
def subBytes(block):
    tmp = deepcopy(block)    
    
    for i in range(len(tmp)):
        tmp[i] = sbox[tmp[i]]
       
    return tmp
########################################################################################



########################################################################################
# Does subBytesInv on one block at a time using sboxInv, and returns the result
def subBytesInv(block):
    tmp = deepcopy(block)    

    for i in range(len(tmp)):
        tmp[i] = sboxInv[tmp[i]]
    
    return tmp
########################################################################################