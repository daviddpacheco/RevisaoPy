'''
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    if num%2 == 0:
     pares+= 1
print(pares)

numeros = [70,90,100,324,653,642,754,21,32,99]
for i in range(len(numeros))
    numero[i] = 0
print(numeros)

nomes = ["danilo","david","lucas","pedro","rodrigo","kaique","tozzi"]
ta_ou_nao = False
for i in range(len(nomes)):
    if nomes[i]=="danilo":
        ta_ou_nao = True
        print(f"Danilo é o numero {i}")
if not ta_ou_nao:
    print("nao encontrei")

lista = [12,23,36,41,69]
print(lista)
ultimo = len(lista)-1
for i in range(len(lista)):
    aux = lista[i]
    lista[i] = lista[ultimo-i]
    lista[ultimo-i] = aux
    print(lista)
'''
lista1 = [1,2,3,4,5,6,7]
lista2 = [6,7,12,53,2]
for elem1 in lista1:
    for elem2 in lista2:
        if elem2 == elem1:
            intersect.append(elem1)
print(intersect)
