# Dada una lista retorna una una nueva lista ordenada de mayor a menor

lista = [1,10,5,15,2]
for recorrer in range (1,len(lista)):
    for posicion in range (len(lista)-recorrer):
        if lista[posicion] > lista[posicion + 1]:
            temp = lista[posicion]
            lista[posicion] = lista[posicion + 1]
            lista[posicion + 1]= temp
lista.reverse()
print(lista)

