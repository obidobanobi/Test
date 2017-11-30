########################################################################################
# main.py
# from here, all other methods will be called.
########################################################################################

########################################################################################
# imports
import readKeyFile
import readBlockFile

from sbox import *      # sbox list
from sboxInv import *   # Inverted sbox list
from rcon import*       # rcon list
from RowShifter import* # RowShifter
from SubBytes import*   # SubBytes
from keyManager import *# keyManager
from columnMixer import mixColumns, mixColumnsInv
########################################################################################



########################################################################################
# readKeyFile function calls
key = readKeyFile.getKey("..\\testKey")
print (key)
########################################################################################



########################################################################################
# readBlockFile function calls
print ("\n\n\nTesting column mixer")
block = readBlockFile.getBlock("..\\testBlock")
print(block)

mixColumns(block)


print ("\n\n\n")
########################################################################################



########################################################################################
# shifting rows
shiftedBlock = shiftRows(block)
print ("shiftedBlock:") #debug
print(shiftedBlock)

# inverse
unShiftedBlock = shiftRowsInv(shiftedBlock)
print ("unshiftedBlock:") #debug
print(unShiftedBlock)
########################################################################################



########################################################################################
# sub bytes
substitutedBlock = subBytes(block)
print("substitutedBlock:")
print(substitutedBlock)

# inverse
unsubstitutedBlock = subBytesInv(substitutedBlock)
print("unsubstitutedBlock:")
print(unsubstitutedBlock)
########################################################################################



########################################################################################
word = [ 1 , 2 , 3 , 4 ]
newWord = keyScheduleCore(word ,1)
print("word:")
print(word) 
print("newWord")
print(newWord)

print ("key:")
print (key)
expandedKey = expandKey(key)
print ("expandedKey:")
print (expandedKey)

########################################################################################



########################################################################################
# Sbox and RCon function calls 
print (sbox[0])
print (sboxInv[0])
print (rcon[0])
########################################################################################