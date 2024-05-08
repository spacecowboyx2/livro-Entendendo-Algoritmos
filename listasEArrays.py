#listas encadeadas
# elementos separados e elementos armazenam o endereço do próximo elemento
# inserções e eliminações rapidas 




#array 
#todos os elementos são armazenados um do lado do outro
# leituras rápidas
# todos os elementos do array deve ser do mesmo tipo


def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
 #scroll through the array
    for i in range(1,len(arr)):
        if arr[i]< menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_selecao(arr):#O(n²)
    new_arr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        new_arr.append(arr.pop(menor))
    return new_arr


array = [6,7,3,8,9,20,2,1]
print(ordenacao_selecao(array))
