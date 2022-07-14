"""vamos a hacer una baraja de cartas españolas orientado a objetos.

Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo (espadas, bastos, oros y copas)

La baraja estará compuesta por un conjunto de cartas, 40 exactamente.

Las operaciones que podrá realizar la baraja son:

--barajar: cambia de posición todas las cartas aleatoriamente

--siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no haya más o se haya llegado al final, 
se indica al usuario que no hay más cartas.

--cartasDisponibles: indica el número de cartas que aún puede repartir

--darCartas: dado un número de cartas que nos pidan, le devolveremos ese número de cartas (piensa que puedes devolver). 
En caso de que haya menos cartas que las pedidas, no devolveremos nada pero debemos indicárselo al usuario.

--cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido ninguna indicárselo al usuario

--mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una carta y luego se llama al método, 
este no mostrara esa primera carta."""


import random

class Carta:
    def __init__(self, valor, palo):
        self.valor= valor
        self.palo = palo

    def __str__(self):
        return '[{}-{}]'.format (self.valor,self.palo )

class Baraja : 
    def __init__(self) :
        valores = ['1','2','3','4','5','6','7','10','11','12']
        palos = ['espada','copa','corazon','oro']
        self.baraja = []
        self.barajadas =[]
        for v in valores:
            for p in palos:
                carta = Carta(v,p)
                self.baraja.append(carta)
       
    
    def Barajar (self):
        random.shuffle ( self.baraja)

    def siguente_carta (self):
        if len(self.baraja) !=0:
            primera = self.baraja.pop(0)
            print (primera)
            self.barajadas.append(primera)
        else:
            print ('---------¡Ya no hay mas cartas!-----------')

    def cartas_disponibles (self):
        cartasEnMazo = len(self.baraja)
        print(f'---------Hay {cartasEnMazo} cartas en el mazo!--------')
    
    def darCartas (self,cantidad):
        for i in range (cantidad):
            if len(self.baraja) >= cantidad:
                carta = self.baraja.pop(0)
                print (carta)
                self.barajadas.append(carta)
            else:
                print(' -------No hay suficientes cartas en el mazo---------')
                break
            
    def CartasMonton (self):
        print('-------CARTAS REPARTIDAS--------')
        if len(self.barajadas) != 0:
            for carta in self.barajadas:
                    print(carta)    
        else:
            print('--------Aun no se han repartido cartas--------')

    def mostrar_baraja (self):
        print('----CARTAS DISPONIBLES----')
        for carta in self.baraja:
                print(carta)
    

BarajasEspañolas= Baraja()
BarajasEspañolas.cartas_disponibles()
BarajasEspañolas.Barajar()
BarajasEspañolas.darCartas(4)


BarajasEspañolas.CartasMonton()






