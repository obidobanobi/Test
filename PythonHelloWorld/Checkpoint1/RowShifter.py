import os
from copy import deepcopy   # to copy list by value, not reference

# input block -> output block jaha


def shiftRows(block):

    tmp = deepcopy(block)  
    

	# shift to the left
	# 0
	# <
	# <<
	# <<<

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

def shiftRowsInv(block):
    tmp = deepcopy(block)    

	# shift to the left
	# 0
	# <
	# <<
	# <<<

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