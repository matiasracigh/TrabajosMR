from lista import Lista

lista_personajes = Lista()
lista_personajes_2 = Lista()
posicionthor=0
personajes = [
    {'name':'Iron man'},
    {'name':'Thor'},
    {'name':'Scalet Witch'},
    {'name':'Black Widow'},
    {'name':'Hulk'},
    {'name':'Rocket Racoonn'},
    {'name':'Loki'},
]

for elementos in personajes:
    lista_personajes.insertar(elementos,'name')


#a
posicionthor = lista_personajes.busqueda('Thor','name')
if (posicionthor != -1):
    print ('Thor esta en la posicion ',posicionthor)
else:
    print ('Thor no esta en la lista')
    

#b
posScalet= lista_personajes.busqueda('Scalet Witch','name')
lista_personajes.obtener_elemento(posScalet)['name']= 'Scarlet Witch'



#d Ascendente
lista_personajes.barrido()
print("----------------------------------")
lista_personajes.barrido_Descendente()
print('------------------------------------')

#e
while(not lista_personajes.lista_vacia()):
    print(lista_personajes.(lista_personajes.obtener_elemento(7))
#f
for i in range(0,lista_personajes.tamanio()):
    x = lista_personajes.obtener_elemento(i)
    if (x['name'][0]=="C" or x['name'][0]=="S"):
        print('Los nombres que empiezan con la letra C o S son: ',x['name'])


personajes_2 = [
    {'name':'Iron man','año de aparicion':2001, 'V_H':True},
    {'name':'Thor','año de aparicion':2000, 'V_H':True},
    {'name':'Scalet Witch','año de aparicion':2006, 'V_H':True},
    {'name':'Black Widow','año de aparicion':2009, 'V_H':True},
    {'name':'Hulk','año de aparicion':2003, 'V_H':True},
    {'name':'Rocket Racoonn','año de aparicion':2012, 'V_H':True},
    {'name':'Loki','año de aparicion':1998, 'V_H':True},
]

for elementos in personajes_2:
    lista_personajes_2.insertar(elementos,'name')
    lista_personajes_2.insertar(elementos,'año de aparicion')
    lista_personajes_2.insertar(elementos,'V_H')

lista_personajes_2.barrido()
