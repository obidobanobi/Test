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
from sbox import *      # sbox list
from sboxInv import *   # Inverted sbox list
from rcon import*       # rcon list
from RowShifter import* # RowShifter
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
# Sbox and RCon function calls 
print (sbox[0])
print (sboxInv[0])
print (rcon[0])
########################################################################################