#####################################################################################################################
# Name: Hussain Mehdi                                                                                               #
# Student ID: 20337270                                                                                              #
# Purpose: Prime Number Generation for RSA                                                                          #
# Source: GeeksForGeeks (https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/)      #
#####################################################################################################################

import random

# Pre-generated primes
prePrimeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
					31, 37, 41, 43, 47, 53, 59, 61, 67,
					71, 73, 79, 83, 89, 97, 101, 103,
					107, 109, 113, 127, 131, 137, 139,
					149, 151, 157, 163, 167, 173, 179,
					181, 191, 193, 197, 199, 211, 223,
					227, 229, 233, 239, 241, 251, 257,
					263, 269, 271, 277, 281, 283, 293,
					307, 311, 313, 317, 331, 337, 347, 349]

# METHOD: Random n Bit Generator
def nRandomBit(n):
	return random.randrange(2**(n-1)+1, 2**n - 1)

# METHOD: Getting lower prime and testing 
def getLowPrime(n):
	while True:
		# Get random number
		pc = nRandomBit(n)
		# Test divisibility by prePrimeList
		for divisor in prePrimeList:
			if pc % divisor == 0 and divisor**2 <= pc:
				break
		else: return pc

# METHOD: Miller Rabin Primality Test for prime
def millerPass(mrc):
	maxDivisionsByTwo = 0
	ec = mrc-1
	while ec % 2 == 0:
		ec >>= 1
		maxDivisionsByTwo += 1
	assert(2**maxDivisionsByTwo * ec == mrc-1)

	def trialComposite(round_tester):
		if pow(round_tester, ec, mrc) == 1:
			return False
		for i in range(maxDivisionsByTwo):
			if pow(round_tester, 2**i * ec, mrc) == mrc-1:
				return False
		return True

	# Number of trials to run: 20
	numberOfRabinTrials = 20
	for i in range(numberOfRabinTrials):
		round_tester = random.randrange(2, mrc)
		if trialComposite(round_tester):
			return False
	return True


