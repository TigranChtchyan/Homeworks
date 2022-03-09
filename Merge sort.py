a = [5,7,8,1,0,3,4,9,10,5]

def merge(lst1, lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    l = list(range(n1+n2))
    pointer1 = 0
    pointer2 = 0
    for i in range(n1+n2):
        if lst1[pointer1]<=lst2[pointer2]:
            l[i] = lst1[pointer1]
            pointer1 += 1
        else:
            l[i] = lst2[pointer2]
            pointer2 += 1

        if pointer1 == n1:
            l[i+1:]=lst2[pointer2:]
            return l
        if pointer2 == n2:
            l[i+1:]=lst1[pointer1:]
            return l


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    arr1 = arr[ : n//2]
    arr2 = arr[n//2 : ]
    return merge(merge_sort(arr1), merge_sort(arr2))

print(merge_sort(a))