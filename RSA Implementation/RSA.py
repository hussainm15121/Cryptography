#################################################################################
# Name: Hussain Mehdi                                                           #
# Student ID: 20337270                                                          #
# Purpose: Implementation of RSA Algorithm                                      #
#################################################################################
import random
import json
import primeGen


# METHOD: Euclid's algorithm function for GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# METHOD: Euclid's extended algorithm function for multiplicative inverse
def multi_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


# METHOD: Key pair generator (Public & Private)
def gen_key_pair(p, q):
    if p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    # Totient of n
    phi = (p-1) * (q-1)
   
    # Choose an integer e 
    e = random.randrange(1, phi)
    
    # Verify that e & phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Call Extended Euclid's Algorithm to generate private key
    d = multi_inverse(e, phi)

    # Public key = (e, n) & private key = (d, n)

    # Writing public key to "public_keys.txt" file
    f_public = open('public_keys.txt', 'w')
    f_public.write(str(n) + '\n')
    f_public.write(str(e) + '\n')
    f_public.close()

    # Writing private key to "private_keys.txt" file
    f_private = open('private_keys.txt', 'w')
    f_private.write(str(n) + '\n')
    f_private.write(str(d) + '\n')
    f_private.close()

    return ((e, n), (d, n))

# METHOD: RSA Encryption Function
def encryption(plaintext):
    # Reading public key from file
    try:
        fo = open("public_keys.txt", 'r')
    # File not found exception
    except FileNotFoundError:
        print('public_keys.txt file is not found. Generate Keys again.')
    # Load data into variables
    else:
        n = int(fo.readline())
        e = int(fo.readline())
        fo.close()

        # Convert each letter in the plaintext to numbers based on the char (a^b mod m)
        cipher = [pow(ord(char), e, n) for char in plaintext]
        # Return array of bytes
        return cipher


# METHOD: RSA Decryption Function
def decryption(cipherText):
    # Reading private key from file
    try:
        fo = open('private_keys.txt', 'r')
        n = int(fo.readline())
        d = int(fo.readline())
        fo.close()
    # File not found exception
    except FileNotFoundError:
        print('private_keys.txt file is not found. Generate Keys again.')
    # Load data into variables
    else:
        # Generate the plaintext based on the cipherText (a^b mod m)
        aux = [str(pow(char, d, n)) for char in cipherText]
        # Return array of bytes as a string
        plain = [chr(int(char2)) for char2 in aux]
        return ''.join(plain)

# Main Method for running the Python Script
if __name__ == '__main__':
    print("\033[1;37;40m------------------------------------ RSA Algorithm --------------------------------------------\033[0;37;40m \n")
    print("Choose one of the following: ")
    option = int(input("Enter (1) for Encrypt or (2) for Decrypt: "))
    if(option == 1):
        n = int(input("Please enter number of bits to generate primes (greater than 2^64= (20 digits)): "))
        if(n < 20):
            print("Bits entered too low, weak keys... ABORT!")
        # Prime Number generation (Source: GeeksForGeeks)
        else: 
            while True:
                prime_candidate = primeGen.getLowPrime(n)
                prime_candidate2 = primeGen.getLowPrime(n)
                if not primeGen.millerPass(prime_candidate):
                    continue
                if not primeGen.millerPass(prime_candidate2):
                    continue
                else:
                    print("First Prime:", prime_candidate)
                    print("Second Prime: ", prime_candidate2)
                    break
            # Read file to encrypt (Input: Plaintext)
            fileEncrypt = (input("Enter Filename to Encrypt from: "))
            with open(fileEncrypt, 'r') as f:
                plainText=f.read()
            f.close()
            print(" ")
            print("Generating Prime Numbers: ")
            p = prime_candidate
            q = prime_candidate2
            print(p)
            print(q)

            print("Generating your public / private key-pairs now . . .")
            # Call Key Gen Function
            public, private = gen_key_pair(p, q)

            print("Your public key is: ", public, " and your private key is: ", private)
            print("Keys loaded to files...")

            print("Encrypting File entered using keys... ")
            encrypted_message = encryption(plainText)

            # File to output encrypted text
            outEncypted = input("Enter filename to output encrypted data to: ")
            with open(outEncypted, 'w') as filehandle:
                json.dump(encrypted_message, filehandle)
            
            print("Your message has been encrypted")
            print("Decrypt message with private key: ", private)
    
    # Decryption section
    if(option == 2):
        inEncypted = input("Enter filename to decrypt data from: ")
        print("Opening encrypted file for decryption: ", inEncypted)
        with open(inEncypted, 'r') as filehandle:
            encryptedList = json.load(filehandle)
        print(" ")
        print("Loading Keys from file...")
        print(" ")
        # Decryption Function call
        decrypted_message = decryption(encryptedList)

        with open('decrypted.txt', 'w') as f:
            decryptedFile=f.write(decrypted_message)

        print("File has been decrypted!")

    print(" ")
    print("============================================ END ==========================================================")
    print("===========================================================================================================")
