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
socket.bind("tcp://*:%s" % port)

send = socket.send_json
recv = socket.recv_json


bits = 123
cnt = 0
p = 0
while not isprime(p):
    cnt += 1
    p = randint(69, 2**bits)

x = randint(0,p-1)
A = randint(0,p-1)
B = modpow(A,x,p)
send((A,B,x,p))

while 1:
    r = randint(0,p-1)  # private to P
    h = modpow(A,r,p)   # P commit
    send(h)

    b = recv()

    s = (r+b*x) % (p-1) # P proof
    send(s)

