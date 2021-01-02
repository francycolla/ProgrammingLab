#Scrivete uno script che sommi tutti i valori delle vendite degli shampoo del file “shampoo_sales.csv”


def sum_list(the_list):
    total=0
    for item in the_list:
        total=total+item
    return total

#inizializzo una lista vuota per salvare i valori
total_values=[]

#apro il file
my_file=open("shampoo_sales.csv", "r")
for line in my_file:

    #faccio lo split di ogni riga sulla virgola
    elements=line.split(',')

    # Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
        
        # Setto la data e il valore
        date  = elements[0]
        value = elements[1]
        
        # Aggiungo alla lista dei valori questo valore
        total_values.append(float(value))
    
csv_data_sum=sum_list(total_values)
print(csv_data_sum)
