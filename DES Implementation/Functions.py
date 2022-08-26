from Initials import *
#################################################################################
# Name: Hussain Mehdi                                                           #
# Student ID: 20337270                                                          #
# Purpose: Function File containing majority relevant functions                 #
# Reference (Certain Functions): https://github.com/sarahashraf200/DES-Cipher   #
#################################################################################

#METHOD: Used for generating Keys for each round
def keyGen(key):

    keys = []
    key = stringBitsConv(key)

    key = permut(key, keyPermutList1)

    leftBlock, rightBlock = splitArr(key, 28)
    for i in range(16):
        leftBlock, rightBlock = shiftLeft(leftBlock, rightBlock, NEXTSHIFT[i])
        temp = leftBlock + rightBlock
        keys.append(permut(temp, keyPermutList2))
    return keys

#METHOD: Used to substitute bytes (Sbox)
def SboxSub(bitArray):													
    blocks = splitArr(bitArray, 6)
    result = []

    for i in range(len(blocks)):
        block = blocks[i]

        row = int( str(block[0]) + str(block[5]), 2 )

        column = int(''.join([str(x) for x in block[1:-1]]), 2)
        sboxValue = SboxList[i][row][column]
        binVal = binaryConv(sboxValue, 4)
        result += [int(bit) for bit in binVal]

    return result

#METHOD: Add Padding to text
def pad(text):
    paddingLength = 8 - (len(text) % 8)
    text += chr(paddingLength) * paddingLength
    return text

#METHOD: Remove Padding from Data
def remPadding(data):					
    paddingLength = ord(data[-1])
    return data[ : -paddingLength]

#METHOD: Open Array
def openE(array, table):
    openRray = [array[element - 1] for element in table]
    return openRray

#METHOD: For conducting Permutations
def permut(array, table):
    permuted = [array[element - 1] for element in table]
    return permuted

#METHOD: For Shifting Array Left 
def shiftLeft(list1, list2, n):
    shiftedL = list1[n:] + list1[:n], list2[n:] + list2[:n]
    return shiftedL

#METHOD: Splitting Array into pieces  
def splitArr(list, n):
    splitedArray = [ list[i : i + n] for i in range(0, len(list), n)]
    return splitedArray

#METHOD: Implementing XOR Function  
def xorFunc(list1, list2):
    xorImp = [element1 ^ element2 for element1, element2 in zip(list1,list2)] 
    return xorImp

#METHOD: Binary Conversion of a given string  
def binaryConv(val, bitSize):
    binVal = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    while len(binVal) < bitSize:
        binVal = "0" + binVal
    return binVal

#METHOD: Converting String to Bits 
def stringBitsConv(text):
    bitArray = []
    for letter in text:
        binVal = binaryConv(letter, 8)
        binValArr = [int(x) for x in list(binVal)]
        bitArray += binValArr
    return bitArray

#METHOD: Converting Bits to String
def bitsStringConv(array):
    byteChunks = splitArr(array, 8)
    stringBytesList = []										
    stringResult = ''
    for byte in byteChunks:
        bitsList = []
        for bit in byte:
            bitsList += str(bit)
        stringBytesList.append(''.join(bitsList))
    result = ''.join([chr(int(stringByte, 2)) for stringByte in stringBytesList])
    return result
