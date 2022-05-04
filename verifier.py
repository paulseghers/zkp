import numpy as np
from random import randint


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
    # fibo and fermat test
    return p > 7 and fibo(p+1, p) == 0 and modpow(2,p-1,p) == 1




import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

send = socket.send_json
recv = socket.recv_json


(A,B,x,p) = recv()


for _ in range(10):
    h = recv()

    b = randint(0,1)    # V choice
    send(b)

    s = recv()

    lhs = modpow(A,s,p)
    rhs = h * modpow(B,b,p) % p
    ok = lhs == rhs

    assert ok

print ('assertion passed')
