datos=[28,12,34,52,56,72,11]
#ordenamiento eficiente
def quicksort (vector,inicio,fin):
    primero =inicio
    ultimo =fin - 1 #anteultimo elemento ya que uso el pivote con el fin
    pivote =fin
    while (primero<ultimo): #sig que todavia no se cruzaron y no encontre la pos del pivote
        while (vector[primero]<vector[pivote] and primero <= ultimo):
            primero= primero + 1
        while (vector[ultimo]>vector[pivote] and ultimo >=primero):
            ultimo= ultimo -1 

        if (primero<ultimo): #hago intercambio
            vector[primero],vector[ultimo]=vector[ultimo],vector[primero]

        if (vector[pivote]<vector[primero]): #hago intercambio
            vector[primero],vector[pivote]=vector[pivote],vector[primero]

        if (inicio<primero):
            quicksort(vector,inicio,primero-1)
        if (fin>primero):
            quicksort(vector,primero+1,fin)



def busqueda_binaria(vector,buscado,inicio,fin):
    if (inicio<fin): #condicion de fin
        medio= (inicio+fin)//2
        if (vector[medio]==buscado):
            return medio
        elif (vector[medio]<buscado):
            return busqueda_binaria(vector,buscado,medio+1,fin) #va para la derecha 
        else:
            return busqueda_binaria(vector,buscado,inicio,fin-1) #va para la izquierda
    else:
        return -1

quicksort(datos,0,len(datos)-1)
print(datos)
print(busqueda_binaria(datos,72,0,len(datos)-1))












        









