#Punto 2
from cola import Cola
from pilaflaco import Pilaflaco

Cola_notificaciones=Cola()
Cola_aux=Cola()
Pila_almacenar=Pilaflaco()


class Notif(object):
    def __init__(self,hora_notif, aplicacion_emitio, mensaje):
        self.hora_notif = hora_notif
        self.aplicacion_emitio = aplicacion_emitio
        self.mensaje=mensaje


Cola_notificaciones.arribo(Notif(12,"Twitter","Hola mundo"))
Cola_notificaciones.arribo(Notif(3,"Facebook","Estoy rindiendo"))
Cola_notificaciones.arribo(Notif(4,"Facebook","Todo bien"))
Cola_notificaciones.arribo(Notif(12,"Twitter","Python"))
Cola_notificaciones.arribo(Notif(12,"Instagram","Como estas"))

#A
while(not Cola_notificaciones.cola_vacia()):
    aux = Cola_notificaciones.atencion()
    if (aux.aplicacion_emitio =='Facebook'):
        aux.mensaje.pop
    Cola_aux.arribo(aux)

    print(Cola_aux)

while(not Cola_aux.cola_vacia()):
    Cola_notificaciones.arribo(Cola_aux.atencion())

#B
while(not Cola_notificaciones.cola_vacia()):
    aux = Cola_notificaciones.atencion()
    if (aux.aplicacion_emitio =='Twitter' and aux.mensaje=="Python"):
        print('Las notificaciones de Twitter son : '+ aux.mensaje) 
    Cola_aux.arribo(aux)

#C
while(not Cola_aux.cola_vacia()):
    Cola_notificaciones.arribo(Cola_aux.atencion())
    Pila_almacenar.apilar(Cola_notificaciones.atencion)


while (not Pila_almacenar.pila_vacia()):
    x= Pila_almacenar.desapilar()
    print(x)



  
