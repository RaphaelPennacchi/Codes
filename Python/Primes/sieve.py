#!/usr/bin/env python3
from math import sqrt


def bitMaskSieve(n):
    #A sieve with the bitMask on the list initiation
    #Cuts the time for setting the even numbers out
    sieve = [False, False, True, True] + [False, True] * ((n - 2) // 2)
    sieve = sieve[:n+1]

    #Just verify the odd numbers
    for i in range(3, int(sqrt(n) + 1), 2):
        if sieve[i]:
            for j in range(pow(i, 2), n+1, 2 * i):
                sieve[j] = False

    #Faster output with yield
    for i in range(3):
        if sieve[i]:
            yield i

    for i in range(3, n+1, 2):
        if sieve[i]:
            yield i

def betterSieve(n):
    sieve = [False] * 2 + [True] * (n-1)
    for i in range(4, n+1, 2):
        sieve[i] = False
    for i in range(3, int(sqrt(n)+1), 2):
        if sieve[i]:
            for j in range(pow(i, 2), n+1, i):
                sieve[j] = False
    return sieve

def classicalSieve(n):
    sieve = [False] * 2 + [True] * (n-1)
    for i in range(2, int(sqrt(n))+1):
        if sieve[i]:
            j, tot = pow(i, 2), n+1
            while j < n+1:
                sieve[j] = False
                j += i
    return sieve

def main():
    size = 100
    sieve = bitMaskSieve(size)
    for i in sieve:
        print(i)

if __name__ == "__main__":
    main()
