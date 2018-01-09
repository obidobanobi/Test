########################################################################################
# RowShifter.py
# The method getBlock() takes a filename and a boolean (decrypt) as parameters
# and return a block
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################



########################################################################################
# imports 
import os
from copy import deepcopy   # to copy list by value, not reference
########################################################################################


########################################################################################
# shiftRows is a static block-operator. Meaning that it performs the same action
# every time it is called. It simply shifts each row to the left the same number of
# steps as the current row number. As seen below:
# a b c d       a b c d
# e f g h   →   f g h e
# i j k l       k l i j
# m n o p       p m n o
def shiftRows(block):

    tmp = deepcopy(block)  

    tmp[0] = block[0]
    tmp[1] = block[5]
    tmp[2] = block[10]
    tmp[3] = block[15]

    tmp[4] = block[4]
    tmp[5] = block[9]
    tmp[6] = block[14]
    tmp[7] = block[3]

    tmp[8] = block[8]
    tmp[9] = block[13]
    tmp[10] = block[2]
    tmp[11] = block[7]

    tmp[12] = block[12]
    tmp[13] = block[1]
    tmp[14] = block[6]
    tmp[15] = block[11]

    return tmp
########################################################################################


########################################################################################
# shift to the right instead of to the left
# a b c d       a b c d
# f g h e   →   e f g h
# k l i j       i j k l
# p m n o       m n o p
def shiftRowsInv(block):

    tmp = deepcopy(block)    

    tmp[0] = block[0]
    tmp[5] = block[1]
    tmp[10] = block[2]
    tmp[15] = block[3]

    tmp[4] = block[4]
    tmp[9] = block[5]
    tmp[14] = block[6]
    tmp[3] = block[7]

    tmp[8] = block[8]
    tmp[13] = block[9]
    tmp[2]  = block[10]
    tmp[7] = block[11]

    tmp[12] = block[12]
    tmp[1] = block[13]
    tmp[6] = block[14]
    tmp[11] = block[15]

    return tmp
########################################################################################
