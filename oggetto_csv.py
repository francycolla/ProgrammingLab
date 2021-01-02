#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1. venga inizializzato sul nome del file csv, e
#2. abbia un attributo “name” che ne contenga il nome
#3. abbia un metodo “get_data” che torni i dati dal file CSV come numeri di una lista (come abbiamo già visto).


#oggetto CSV file
#-init (name)
#-name
#-get_data
# return dati

#creo l'oggetto con una classe
class CSVFile:
    pass  #oggetto vuoto

    def __init__(self, name): #inizializzo name
        self.name= name #attributo name

    def get_data(self): #metodo get_data

        #inizializzo una lista vuota per salvare i valori
        values=[]

        #apro il file
        my_file=open('shampoo_sales.csv', 'r')
        for line in my_file:

            #faccio lo split di ogni riga sulla virgola
            elements=line.split(',')

            # Se NON sto processando l’intestazione...
            if elements[0] != 'Date':
        
                # Setto la data e il valore
                date  = elements[0]
                value = elements[1]
        
                # Aggiungo alla lista dei valori questo valore
                values.append(float(value))

        return values
    

mio_file=CSVFile(name='shampoo_sales.csv')  #Provatelo sul file “shampoo_sales.csv”

print(mio_file.name)
print(mio_file.get_data())





