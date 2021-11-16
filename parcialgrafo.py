from grafo import Grafo

grafo = Grafo(dirigido=False)

grafo.insertar_vertice("manjaro",data={"tipo":"PC"})
grafo.insertar_vertice("parrot",data={"tipo":"PC"})
grafo.insertar_vertice("Fedora",data={"tipo":"PC"})
grafo.insertar_vertice("Mint",data={"tipo":"PC"})
grafo.insertar_vertice("Ubuntu",data={"tipo":"PC"})
grafo.insertar_vertice("guarani",data={"tipo":"Servidor"})
grafo.insertar_vertice("mongoDB",data={"tipo":"Servidor"})
grafo.insertar_vertice("Impresora",data={"tipo":"impresora"})
grafo.insertar_vertice("Router1",data={"tipo":"Router"})
grafo.insertar_vertice("Router2",data={"tipo":"Router"})
grafo.insertar_vertice("Router3",data={"tipo":"Router"})
grafo.insertar_vertice("red hat",data={"tipo":"notebook"})
grafo.insertar_vertice("debian",data={"tipo":"notebook"})
grafo.insertar_vertice("arch",data={"tipo":"notebook"})
grafo.insertar_vertice("switch1",data={"tipo":"switch"})
grafo.insertar_vertice("switch2",data={"tipo":"switch"})

grafo.insertar_arista(12,"switch2","parrot")
grafo.insertar_arista(40,"switch2","manjaro")
grafo.insertar_arista(5,"switch2","mongoDB")
grafo.insertar_arista(56,"switch2","arch")
grafo.insertar_arista(3,"switch2","Fedora")
grafo.insertar_arista(61,"switch2","Router3")
grafo.insertar_arista(50,"Router3","Router2")
grafo.insertar_arista(43,"Router3","Router1")
grafo.insertar_arista(29,"Router1","switch1")
grafo.insertar_arista(9,"Router2","guarani")
grafo.insertar_arista(25,"Router2","red hat")
grafo.insertar_arista(17,"switch1","debian")
grafo.insertar_arista(80,"switch1","Mint")
grafo.insertar_arista(22,"switch1","Impresora")
grafo.insertar_arista(80,"switch1","Ubuntu")

#2
posiciondebian = grafo.buscar_vertice("debian")
grafo.barrido_profundidad(posiciondebian)
grafo.barrido_amplitud(posiciondebian)
print()

posicionRedHAT = grafo.buscar_vertice("red hat")
grafo.barrido_profundidad(posicionRedHAT)
grafo.barrido_amplitud(posicionRedHAT)
print()

posicionArch = grafo.buscar_vertice("arch")
grafo.barrido_profundidad(posicionArch)
grafo.barrido_amplitud(posicionArch)
print()



#4
def expansionMinima(grafo):
    arbol = []
    ExpancionMinima = grafo.prim();

    for i in expansionMinima:
        print(i)



#5
grafo.eliminar_vertice("Impresora")
grafo.barrido_profundidad(0)
