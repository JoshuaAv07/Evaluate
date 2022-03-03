import string
from tkinter.messagebox import YES

print('Escribe el numero de casillas que puede recorrer tu pieza: ')

def ajedrez(pieza):
    if pieza == 1:
        return('Peon')
    else:
        if pieza == 2:
            return('Rey')
        else:
            if pieza == 3:
                return('caballo')
            else:
                return('Torre, Ryena o Alfil')

    

pieza = int(input())
print(ajedrez(pieza))