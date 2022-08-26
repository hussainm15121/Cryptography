import re
#################################################################################
# Name: Hussain Mehdi                                                           #
# Student ID: 20337270                                                          #
# Purpose: Bruteforce Affine Cipher                                             #
#################################################################################

#Pending: Search file and print decoded line
#def decoded():
#    file = open('result.txt', 'r') 
#    filedata = file.read()
#    word = 'the'
#    for line in filedata:
#        if re.search(word, line):
#            print('Cipher Decoded..')
#            print('Writing to Decoded.txt')
#            print('Line: ', line)          
                         
#Brute-Force Affine Cipher (Main Method)
def main():
    f =open("cipher.txt", "r")          #Opening Readers for both files
    df=open('result.txt','w')
    data = f.read()
    data = ''.join(data.split())        #removing spaces from cipher.txt file (gets rid of 'k')
    f.close()
    print("File Content: ", data)       #Printing Read content to Screen
    
    data = data.lower()                 #Lowercase the content (Uppercase results in different results)
    string_lenght=len(data)                                    
    i=0                                 #Initializing Vars 
    keyA=2
    mod=int(26)                         #Setting Mod to 26 (Alphabets)      
    while keyA<mod:
        keyB=0
        tempVar=keyA                                         #Temporary holding value of Key A 
        alpha=1                                           #setting for key alpha
        temp_mod=mod                                      
        while temp_mod != 0:                                          
            tempVar%=temp_mod                                          
            (tempVar,temp_mod)=(temp_mod,tempVar)                       
        if (tempVar == 1):                                             
            while (alpha*keyA%mod) !=1:                                       
                alpha += 1                                                 
            while keyB < mod:
                i=0
                print("Key(A & B): ", keyA, keyB)           #Display both A & B on console
                df.write(" ")
                df.write("\n")
                df.write("Key (A & B):")
                df.write(str(keyA))                         #Write to file
                df.write(" ")
                df.write(str(keyB))
                df.write(" ")

                while i < string_lenght:
                    character=data[i]                                     
                    y= ord(character) - 97                                 
                    x= (alpha*(y-keyB)) %mod                                      
                    plaintext=chr(x + 97)                                    
                    df.write(plaintext)
                    i+=1                                                  
                print()
                keyB += 1
        keyA += 1
    df.close()
 #   decoded()

if __name__ == '__main__':
    main()