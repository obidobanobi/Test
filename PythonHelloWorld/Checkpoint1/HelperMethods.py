########################################################################################
# HelperMethods.py
# Helper Methods...
# Created By Leonhard Berg, Olle Montelius (Team programming)
########################################################################################



########################################################################################
# Takes one block and prints the hexadecimal values as chars
def printHex(block):
    string = ""
    for i in block:
        s = hex(i)[2:].rjust(2, '0')
        string += s
    return string
########################################################################################