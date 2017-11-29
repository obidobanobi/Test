import os

from copy import deepcopy   # to copy list by value, not reference

from sbox import *      # sbox list
from sboxInv import *   # Inverted sbox list


# input block -> output block


def subBytes(block):
    tmp = deepcopy(block)    
    
    for i in range(len(tmp)):
        tmp[i] = sbox[tmp[i]]
       
    return tmp



def subBytesInv(block):
    tmp = deepcopy(block)    

    for i in range(len(tmp)):
        tmp[i] = sboxInv[tmp[i]]
    
    return tmp