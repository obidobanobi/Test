########################################################################################
# main.py
# from here, all other methods will be called.
########################################################################################

########################################################################################
# imports
import readKeyFile
import readBlockFile
import RowShifter
import SubBytes
import keyManager

from sbox import *      # sbox list
from sboxInv import *   # Inverted sbox list
from rcon import*       # rcon list
from RowShifter import* # RowShifter
from SubBytes import*   # SubBytes
from keyManager import *# keyManager
########################################################################################



########################################################################################
# readKeyFile function calls
key = readKeyFile.getKey("..\\testKey")
print (key)
########################################################################################



########################################################################################
# readBlockFile function calls
block = readBlockFile.getBlock("..\\testBlock")
print(block)
########################################################################################



########################################################################################
# shifting rows
shiftedBlock = RowShifter.shiftRows(block)
print ("shiftedBlock:") #debug
print(shiftedBlock)

# inverse
unShiftedBlock = RowShifter.shiftRowsInv(shiftedBlock)
print ("unshiftedBlock:") #debug
print(unShiftedBlock)
########################################################################################



########################################################################################
# sub bytes
substitutedBlock = SubBytes.subBytes(block)
print("substitutedBlock:")
print(substitutedBlock)

# inverse
unsubstitutedBlock = SubBytes.subBytesInv(substitutedBlock)
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
########################################################################################



########################################################################################
# Sbox and RCon function calls 
print (sbox[0])
print (sboxInv[0])
print (rcon[0])
########################################################################################