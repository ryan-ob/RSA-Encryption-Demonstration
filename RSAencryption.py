### Simple RSA encryption with trivially small numbers
### 	(Not strong encrypion... at all)

## RSA process
# Choose 2 primes, P and Q
# Calculate N, J(N)
# Find E
# Find D
# Output public and private key


message = "The Quick Brown Fox Jumps Over The Lazy Dog."

def main():

	#Two "random" prime numbers
    P = 19
    Q = 23
    #Other primes to consider: 569, 487
        
	#multiply together for part of key
    N = P*Q
    J = (P-1)*(Q-1) # Number of coprimes between 0 and N

    #Print
    print '  P   Q     N     J'
    print repr(P).rjust(3), repr(Q).rjust(3), repr(N).rjust(5), repr(J).rjust(5)

    ###Determine an encyption key, E
    # E must be greater than 1 and less than J
    # E must be coprime with N and J
    E = 0
    for x in range(3,J,2): #must be odd
		#Check if x is coprime with N and J
			# Can find multiple coprimes,
			# 	but will choose largest
		if coprime(x,N) and coprime(x,J):
			E = x

    ### Determine the decryption key, D
    #Find an integer  D that satisfies (E*D)%J = 1
    #    Also, choose D != E so public and private key are different
    D = 1 # D > 1
    while ((E*D)%J != 1) or (E == D):
        D += 1

    #Output public and private keys
    krj = 3 #right justify value of key values
    print '\nPublic Key: ',repr(E).rjust(krj),repr(N).rjust(krj)
    print   'Private Key:',repr(D).rjust(krj),repr(N).rjust(krj),'\n'

    ###Encrypt the message
    print 'Message:  ',message

	#Easiest to store cipher as numbers, but
	#	encrypted message with unicode text
    #	can look cool
    cipher = []
    cipherText = ''
    for Tchar in message:
    	T = ord(Tchar)
    	#RSA encryption formula
    	C = (T**E)%N
    	cipher.append(C)
    	cipherText += unichr(C)

    print 'Cipher:   ',cipherText

    ##Decrypt the message
    output = ''
    #outputNum = []
    for C in cipher:
        T = (C**D)%N
        output += unichr(T)
        

    #print 'Decrypted:',output
    print 'Decrypted:',output


#Determine if two numbers are coprime using Euclid's algorithm
def coprime(x,y):
	while x != 0 and y != 0:
		if x > y:
			x = x%y
		else:
			y = y%x

	# Coprime if only common factor is 1
	if x == 1 or y == 1:
		return True
	else:
		return False


if __name__ == '__main__':
     main()
