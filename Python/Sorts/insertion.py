#!/usr/bin/env python3


def insertion(lista):
    tam = len(lista)
    for i in range(1, tam):
        key, j = lista[i], i-1
        while j >= 0 and lista[j] > key:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    print(lista)
    return lista

def main():
    lista = [4,3,0,1,-1,2,3,1,4]
    insertion(lista)

if __name__ == "__main__":
    main()
