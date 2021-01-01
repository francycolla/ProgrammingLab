#Scrivete una funzione che sommi tutti gli elementi di una lista

def somma_elementi(lista):
    sum=0
    for item in lista:
        sum = sum + item
    print('somma: {}'. format(sum))

somma_elementi([1,4,10])


