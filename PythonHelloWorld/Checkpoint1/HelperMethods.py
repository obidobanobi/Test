
def printHex(block):
    string = ""
    for i in block:
        s = hex(i)[2:].rjust(2, '0')
        string += s
    return string
