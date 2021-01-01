<<<<<<< HEAD
#Scrivete una funzione che sommi tutti gli elementi di una lista

def somma_elementi(lista):
    sum=0
    for item in lista:
        sum = sum + item
    print('somma: {}'. format(sum))

somma_elementi([1,4,10])


=======
def list_sum(the_list):
    sum=0;
    for item in the_list:
        sum=sum+item
    print("Somma: {}" .format(sum))

list_sum([1,4,10])

#soluzione con return 
def list_sum(the_list): 
    sum=0
    for item in the_list: 
        sum = sum + item
    return sum

print("Somma: {}".format(list_sum([1,4,10])))
>>>>>>> a05740e0ffcbac50c90ba1aba32d673ea1a67e5f
