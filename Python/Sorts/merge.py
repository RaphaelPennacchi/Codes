#!/usr/bin/env python3

def mergeSort(array):
    if (tam := len(array)) == 1:
        return array
    l1, l2 = array[:tam//2], array[tam//2:]
    l1, l2 = mergeSort(l1), mergeSort(l2)
    return merge(l1, l2)

def merge(array1, array2):
    array3 = []
    while(array1 != [] and array2 != []):
        if array1[0] > array2[0]:
            array3.append(array2[0])
            del array2[0]
        else:
            array3.append(array1[0])
            del array1[0]
    while(array1 != []):
        array3.append(array1[0])
        del array1[0]
    while(array2 != []):
        array3.append(array2[0])
        del array2[0]
    return array3

def main():
    lista = [3,4,1,2,3,1,2,5,6,7,3,92,0,2,1,26,-1,2,4,56,238]
    lista.sort()
    print(lista)
    print(mergeSort(lista))

if __name__ == "__main__":
    main()
