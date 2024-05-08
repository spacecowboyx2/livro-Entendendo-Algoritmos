def quickSort(arr): # O(n log n) log base 2
    if len(arr)<2: #there's no way to order a array with one item, this is base case
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo] #partitioning
        maiores = [i for i in arr[1:] if i > pivo]
        return quickSort(menores) + [pivo]+quickSort(maiores)
#list comprehension 
#syntax
#newList = [expression for item in iterable if condition]



lista= [10,4,7,9,1,0]
print(quickSort(lista))