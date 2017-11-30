########################################################################################
# columnMixer.py
# fancy decription comming soon... =)
########################################################################################

########################################################################################
# imports 
from mixColTables import *
########################################################################################

def mixColumn(col):
    tmp = [None]*4

    tmp[0] = table_2[col[0]]^table_3[col[1]]^col[2]^col[3]      # 2 3 1 1
    tmp[1] = col[0]^table_2[col[1]]^table_3[col[2]]^col[3]      # 1 2 3 1
    tmp[2] = col[0]^col[1]^table_2[col[2]]^table_3[col[3]]      # 1 1 2 3
    tmp[3] = table_3[col[0]]^col[1]^col[2]^table_2[col[3]]      # 3 1 1 2

    return tmp


def mixColumnInv(col):
    tmp = [None]*4

    tmp[0] = table_14[col[0]]^table_11[col[1]]^table_13[col[2]]^table_9[col[3]]      # 14 11 13 9
    tmp[1] = table_9[col[0]]^table_14[col[1]]^table_11[col[2]]^table_13[col[3]]      # 9 14 11 13
    tmp[2] = table_13[col[0]]^table_9[col[1]]^table_14[col[2]]^table_11[col[3]]      # 13 9 14 11
    tmp[3] = table_11[col[0]]^table_13[col[1]]^table_9[col[2]]^table_14[col[3]]      # 11 13 9 14

    return tmp


def mixColumns(block):
    result = []

    result.extend(mixColumn([ block[0], block[1],   block[2],   block[3]        ]))
    result.extend(mixColumn([ block[4], block[5],   block[6],   block[7]        ]))
    result.extend(mixColumn([ block[8], block[9],   block[10],  block[11]       ]))
    result.extend(mixColumn([ block[12],block[13],  block[14],  block[15]       ]))

    return result


def mixColumnsInv(block):
    result = []

    result.extend(mixColumnInv([ block[0],block[1],block[2],block[3] ]))
    result.extend(mixColumnInv([ block[4],block[5],block[6],block[7] ]))
    result.extend(mixColumnInv([ block[8],block[9],block[10],block[11] ]))
    result.extend(mixColumnInv([ block[12],block[13],block[14],block[15] ]))

    return result

