#graphs
#graphs are connection sets. graphs are made up of vertices and edges(arestas).

#undirected graphs: posso ir de A para B ou B para Ana mesma aresta
#directed graph: so posso ir de A para B
from collections import deque

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []
print(grafo)

    

def pessoa_vendedora(nome):
    return nome[-1] == "m"
    
    
def pesquisa():
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_vendedora(pessoa):
                print(pessoa, " é um vendedor de manga")
                return True
            else:
                fila_de_pesquisa+=grafo[pessoa]
                verificadas.append(pessoa)
    return False   


pesquisa()








#breadth-first search (pesquisa em largura)
#1- theres a path from vertice A to vertice B?
#2- which is the minimium path from vertice A to vertice B?



#row are fifo, stack are lifo