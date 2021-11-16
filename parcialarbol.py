from arbol_binario import Arbol 
dinos_nombre = Arbol()
dinos_cod = Arbol()
dic={}
DINOS =[
    {'nombre':'Raptores', 'cod':'123A', 'zona_ubic':'Isla'}
    {'nombre':'Diplodocus', 'cod':'792', 'zona_ubic':'Peru'}
    {'nombre':'Raptores', 'cod':'829C', 'zona_ubic':'Isla'}
    {'nombre':'Spinosaurus', 'cod':'938P', 'zona_ubic':'Bolivia'}
    {'nombre':'Dilophosaurus', 'cod':'8291U', 'zona_ubic':'Argentina'}
    {'nombre':'Diplodocus', 'cod':'093L', 'zona_ubic':'Colombia'}
    {'nombre':'T-Rex', 'cod':'123M', 'zona_ubic':'Estados Unidos'}
    {'nombre':'T-Rex', 'cod':'684K', 'zona_ubic':'Estados Unidos'}
    {'nombre':'Alosaurio', 'cod':'Z00', 'zona_ubic':'Estados Unidos'}
    {'nombre':'Alosaurio', 'cod':'12Ñ', 'zona_ubic':'Estados Unidos'}
    {'nombre':'Sgimoloch', 'cod':'H9', 'zona_ubic':'Estados Unidos'}
    {'nombre':'T-Rex', 'cod':'1Y', 'zona_ubic':'Estados Unidos'}
    {'nombre':'Amargasaurio', 'cod':'1Ñ', 'zona_ubic':'Estados Unidos'}
    {'nombre':'Amargasaurio', 'cod':'980P', 'zona_ubic':'Estados Unidos'}
    {'nombre':'Albertosaurus', 'cod':'2183D', 'zona_ubic':'Estados Unidos'}  
]


#2
for dinosaurio in DINOS:
    dinos_nombre = dinos_nombre.insertar_nodo(dato['nombre'],dato)
    dinos_cod = dinos_cod.insertar_nodo(dato['cod'],dato)


#3
print("Barrido de dinosaurios inorden:") 
dinos_nombre.inorden()
print()


#4
buscado = "792"
pos = dinos_cod.busqueda(buscado)
if pos:
    print ("Informacion del dinosaurio 792:",buscado," ",pos.datos)
print()


#5
dinos_nombre.busqueda_proximidad('T-Rex')

#6
buscado = "Sgimoloch"
pos = dinos_nombre.busqueda(buscado)
if pos:
    nuevo_dinosaurio = input("Cambio del nombre de Sgimoloch")
    buscado, DINOS = dinos_nombre.eliminar_nodo(buscado)
    DINOS ["nombre"] = 'Stygimoloch'
    dinos_nombre = dinos_nombre.insertar_nodo(buscado, DINOS)
print()

#7
print("La ubicacion de los raptores es: ")
dinos_nombre.busqueda_proximidad('Raptores')


#8
arbol.conta_Diplodocus(dic)

def ordenar(item):
    return item[1]

lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)
print("Cantidad de Diplodocus")
print()
