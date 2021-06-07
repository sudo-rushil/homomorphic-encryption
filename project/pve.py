#!/usr/bin/env python

import math
import random

import numpy as np


def _ext_euc_alg(a, b):
    '''
    Performs Extended Euclidean Algorithm on two integers

            Parameters:
                    a : An integer
                    b : Another integer

            Returns:
                    (gcd, x, y) : tuple of GCD of (a,b) and (x,y) orthogonal to (a,b)
    '''
    if a == 0:
        return b, 0, 1
             
    gcd,x1,y1 = _ext_euc_alg(b % a, a) 
     
    # Update x and y using results of recursive call 
    x = y1 - (b // a) * x1 
    y = x1 
     
    return gcd,x,y

def _inv_mult(a, m):
    '''
    Find modular inverses using EEA

            Parameters:
                    a : Inverse to be found
                    m : Modulus – must have (a, m) == 1

            Returns:
                    inv : Modular inverse of a mod m
    '''
    gcd, x, _ = _ext_euc_alg(a, m)
    
    if gcd == 1:
        return (x + m) % m
    

def _mod_pow(a, e, m):
    '''
    Compute modular exponentation under modular arithmetic
    
            Parameters:
                    a : Base
                    e : Exponent
                    m : Modulus
            
            Returns:
                    b : Value of a^e % m
    '''
    a, b = a % m, 1
    
    if a == 0: return 0
    
    while e > 0:
        if (e & 1) == 1:
            b = (a * b) % m
        
        e >>= 1
        a = (a * a) % m
    
    return b


def RSA_setup(p,q):
    '''
    Sets up parameters for RSA algorithm

            Parameters:
                    p : Large prime
                    q : Another large prime

            Returns:
                    (n, e, d) : RSA modulus, public key, and private key
    '''
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # select public key s.t. (e, phi_n) == 1
    found = False
    
    while not found:
        e = random.randint(1, phi_n)
        if math.gcd(e, phi_n) == 1:
            found = True
    
    d = _inv_mult(e, phi_n)
    
    return n, e, d


def RSA_encrypt(m, e, n):
    '''
    Encrypts messages with RSA algorithm

            Parameters:
                    m : Integer representation of message – must be between 1 and n
                    e : Public key – selected as per RSA_setup
                    n : Modulus – selected as per RSA_setup

            Returns:
                    M : Encrypted message
    '''
    return _mod_pow(m, e, n)


def RSA_decrypt(M, d, n):
    '''
    Decrypts messages with RSA algorithm

            Parameters:
                    M : Encrypted message – calculated as per RSA_encrypt
                    d : Private key – selected as per RSA_setup
                    n : Modulus – selected as per RSA_setup

            Returns:
                    m : Plaintext message
    '''
    return _mod_pow(M, d, n)


class PairValEnc:
    def __init__(self, p, q):
        '''
        Initializes Pair Value Encryption class – performs same setup as RSA algorithm

                Parameters:
                        p : Large prime
                        q : Another large prime 

                Returns:
                        None
        '''
        n = p * q
        phi_n = (p - 1) * (q - 1)

        found = False

        while not found:
            e = random.randint(1, phi_n)
            if math.gcd(e, phi_n) == 1:
                found = True

        d = _inv_mult(e, phi_n)

        self.n = n
        self.phi_n = phi_n
        self.e = e
        self.d = d
        
        
    def load(self, values, mapping):
        '''
        Store problem space and mapping from problem to plaintext space in object

                Parameters:
                        values : list equal to problem space
                        mapping : dict object converting values in problem space to plaintext space

                Returns:
                        None
        '''
        self.values = values
        self.mapping = mapping
        self.inv_mapping = {v:k for k, v in mapping.items()}
        
        
    def encrypt(self, x):
        '''
        Map an input from the problem space to the plaintext space, and encrypt it

                Parameters:
                        x : Value in problem space

                Returns:
                        <enc> : Encrypted value of input
        '''
        if x in self.values:
            return _mod_pow(self.mapping[x], self.e, self.n)
    
    
    def compare(self, x, y):
        '''
        Compare pairs of encrypted values

                Parameters:
                        x : Encrypted value
                        y : Another encrypted value

                Returns:
                        <cmp> : Binary comparison, returning True if the inputs are matchable and False if not
        '''
        return ((x * y) % self.n) == 1
        
    
    def decrypt(self, x, d):
        '''
        Verify the decryption key and decrypt a value from the encryption space to the problem space

                Parameters:
                        x : Encrypted value
                        d : Private key

                Returns:
                        <dec> : Decrypted value of input
        '''
        if d == self.d:
            return self.inv_mapping[_mod_pow(x, self.d, self.n)]    



def prep_example():
	'''
	Create the problem space and problem to plaintext mapping necessary for example in paper

			Parameters:
					None
			
			Returns:
					(X, X_to_Z) : Problem space as <list>, and problem to plaintext mapping as <dict>
	'''
	X = list(range(16)) 
	match = lambda x, y: int(x ^ y == 15)

	n = 33

	# Step 1, find a list of matches in X/~
	X_matches = []
	x = len(X)
	for i in range(x):
	    for j in range(i,x):
	        if match(i,j):
	            X_matches.append((i,j))

	# Step 2, find |X/~| pairs of modular inverses from Z/33Z
	Z_matches = []

	i = 1
	while len(Z_matches) < len(X_matches):
	    j = _inv_mult(i,n)
	    
	    if j is None:
	        i += 1
	        continue
	        
	    Z_matches.append((i,j))
	    i += 1

	# Step 3, map values over
	X_to_Z = {}

	for i, (x,y) in enumerate(X_matches):
	    X_to_Z[x] = Z_matches[i][0]
	    X_to_Z[y] = Z_matches[i][1]

	return X, X_to_Z
