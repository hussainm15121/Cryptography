from Initials import *
from Functions import *
#################################################################################
# Name: Hussain Mehdi                                                           #
# Student ID: 20337270                                                          #
# Purpose: Implementation of DES Algorithm                                      #
#################################################################################

#METHOD: Used For Encryption
def encrypt(key, text, padding):			
    # Padding Check on text
    if padding == True:
        text = pad(text)									
    cipherText = driver(text, key, padding, True)
    return cipherText

#METHOD: Used for Decryption
def decrypt(key, text, padding):	
    plainText = driver(text, key, padding, False)              
    # Padding Check on text
    if padding == True:
        return remPadding(plainText)
    return plainText

#METHOD: Used as Driver Code for implementing DES
def driver(text, key, padding, isEncrypt):
    isDecrypt = not isEncrypt
    keys = keyGen(key)
    plaintext8Block = splitArr(text, 8)
    result = []
    for block in plaintext8Block:
        block = stringBitsConv(block)
        block = permut(block, firstPermutList)
        leftBlock, rightBlock = splitArr(block, 32)
        temp = None
        for i in range(16):
            expandedRightBlock = openE(rightBlock, expandList)
            if isEncrypt == True:
                temp = xorFunc(keys[i], expandedRightBlock)
            elif isDecrypt == True:
                temp = xorFunc(keys[15 - i], expandedRightBlock)
            temp = SboxSub(temp)
            temp = permut(temp, roundPermutList)
            temp = xorFunc(leftBlock, temp)
            leftBlock = rightBlock
            rightBlock = temp
        result += permut(rightBlock + leftBlock, finalPermutList)
    finalResult = bitsStringConv(result)
    return finalResult


#Main Method for Program
def main():
    print("\033[1;37;40m------------------------------------ DES Algorithm --------------------------------------------\033[0;37;40m \n")
    print("Opening DES-test.txt...")
    with open('DES-test.txt', 'r') as f:
        plainText=f.read()
    f.close()
    #key = input("\033[1;32;40mEnter a key (64-bits): \033")        
    key = input("Enter a key (64-bits): ")
    print()
    if len(key) > 8:
        print("Key too long (Shortening Key)..")
        key = key[:8]
        #print(key)
    else:
        print(" Key Length Short (Padding).. ")
        key = key.ljust(8, '0')
        #print(key)
    print(key)
    isPaddingRequired = (len(plainText) % 8 != 0)
    cipherText = encrypt(key, plainText, isPaddingRequired)
    plainText = decrypt(key, cipherText, isPaddingRequired)
    print()
    fw = open("encryptedFile", "w", encoding="utf-8")   #Writing to encryptedFile and using UTF-8 encoding as else error
    fw.write(cipherText)
    fw.close()
    #print("Encrypted Text: %r " % cipherText)  #optional for console printing
    print("Decrypted Text: ", plainText)
    
if __name__ == '__main__':
    main()				