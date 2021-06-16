vector_personajes=["Anakin Skywalker","Yoda","Padmé Amidala","Mace Windu","Darth Maul"]
def barrido_recursivo(vector_personajes):
    if ( vector_personajes== ''):
        print (vector_personajes[0])
#a

#b
def buscaryoda (vector_personajes, posicionyoda):
    if(posicionyoda< len(vector_personajes)):
        if(vector_personajes[posicionyoda] == 'Yoda'):
            return posicionyoda
        else:
            return buscaryoda(vector_personajes= posicionyoda+1)
    else:
        return print("Yoda no se encuentra")
