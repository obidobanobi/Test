########################################################################################
# AddRoundKey.py
# fancy decription comming soon... =)
########################################################################################

########################################################################################
# imports 
from keyManager import *
from readKeyFile import *
from readBlockFile import *
########################################################################################

key = getKey("..\\testKey")
testBlock = getBlock("..\\testBlock")

expandedKey = expandKey(key)
roundKey0 = createRoundKey( expandedKey, 0)

addedRoundKeyToBlock = addRoundKey(testBlock, roundKey0)
print(addedRoundKeyToBlock)