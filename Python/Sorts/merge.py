#!/usr/bin/env python3

def mergeSort(array):
    if (tam := len(array)) == 1:
        return array
    esq, dire = mergeSort(array[:tam//2]), mergeSort(array[tam//2:])
    return merge(esq, dire)

def merge(array1, array2):
    array3 = []
    while(array1 != [] and array2 != []):
        if array1[0] > array2[0]:
            array3.append(array2.pop(0))
        else:
            array3.append(array1.pop(0))
    if array1 != [] or array2 != []:
        array3.extend(array1 or array2)
    return array3

def main():
    lista = [3,4,1,2,3,1,2,5,6,7,3,92,0,2,1,26,-1,2,4,56,238]
    print(mergeSort(lista))

if __name__ == "__main__":
    main()
