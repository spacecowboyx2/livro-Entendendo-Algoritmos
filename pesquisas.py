#pesquisa binaria mais rapido, O(log2 N)(base 2
#rapidez não é medido em segundos, é medido por meio de seu crescimento
def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista)-1
    while baixo<=alto:
        meio = (baixo+alto)//2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio-1
        else:
            baixo = meio+1
    return None

def pesquisaSimples(lista,item):
    for c in range(0, (len(lista))):
        if lista[c] == item:
            return c
    return None

lista = [1,2,3,4,5,6,7,8,9,10]
print(pesquisaSimples(lista,10))

print(pesquisaBinaria(lista, 10))