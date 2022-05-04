import numpy as np
from random import randint

### first functions are just for generating prime numbers ###
bits = 123

def modpow(x,k,mod):
    y = x ** 0
    while k:
        if k % 2: y = x * y % mod
        x = x * x % mod
        k = k // 2
    return y

def fibo(k, mod):
    # arbitrary precision
    x = np.matrix([[0,1],[1,1]], dtype=object)
    y = modpow(x,k,mod)
    return y[0,1]

def isprime(p):
    # discard small primes as well
    # fibo and fermat test from: https://en.wikipedia.org/wiki/Primality_test#Heuristic_tests
    return p > 7 and fibo(p+1, p) == 0 and modpow(2,p-1,p) == 1

cnt = 0
p = 0
while not isprime(p):
    cnt += 1
    p = randint(69, 2**bits)
print(f'{p=} after {cnt} attempts')

### real "ZKP" starts here ###

class prover(x): #P receives an integer in Z\p upon instantiation
    self.x = x
    self.r = None #random value for comittement
    self.A = randint(0,p-1)
    self.B = modpow(A,x,p) # B = A^x

    def communicate(content):
        with open self.logfile as f:

    def gen_r(self):
        return random(0, p-1)



#p has:
x = randint(0,p-1) #don't disclose
A = randint(0,p-1)
B = modpow(A,x,p) # B = A^x

#p says "I know X such that A^x = b mod p"
for test in range(100):
    r = randint(0,p-1)  # private to P, notice r <= p-1

    h = modpow(A,r,p)   # P commits -> disclose h = A^r for hidden r
    #the next check is to make sure P is really creating r.
    b = randint(0,1)    # V choice. 
    s = (r+b*x) % (p-1) # P proof #Donne-moi r+x mod chungus
    if b == 0: #verifier says "please prove you didn't lie for h"
        s = r # (mod p-1)
        lhs = modpow(A, s, p)
        rhs = h
    if b:
        s = r+x #(mod p)
        lhs = modpow(A, r+x, p)
        rhs = h * B#modpow(A, r, p) * B #We want to check h*B == A^x * A^r <=> h
    # V checks
    lhs = modpow(A,s,p) # = A^(r+x)
    rhs = h * modpow(B,b,p) % p
    ok = lhs == rhs

    assert ok
