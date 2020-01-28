#!/usr/bin/env python3

def differentiation(N, lista):
    array = [0] * (N+2)
    for i, j, k in lista:
        array[i] += k
        array[j+1] -= k
    value, result = 0,0
    for i in array:
        value += i
        yield value

def main():
    N, lista = 10, [[1,3,4], [4,7,5], [1,5,6]]
    ll = differentiation(N, lista)
    for i in ll:
        print(i)

if __name__ == "__main__":
    main()
