#Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
#números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
#final.

# NOTA de David:  si hacemos una matriz de 5 x 5 con numeros aleatorios es casi imposible lograr encontrar 4 numeros
# consecutivos. Con lo cual vamos a hacer esto: generamos una lista de 10 x 10, con numeros aletaorios entre el 0 y el 2
# y por cada linea y columnas contamos cuantos numeros consecutivos encontramos.
# solo matrix s
# new change

import numpy as np
import doctest
import random

def detectar_consecutivos( matriz):

    c = 0
    # recorro el array por filas
    for row  in matriz:

         c = 0
         # por cada valor pregunto por la posicion actual mas 1, si es igual a la posicion siguiente.
         for x in range(0, len(row)-2):
             if (row[x]+1 ==  row[x + 1]):
                    c = c + 1

         print("En esta fila", row, "hay esta cantidad de consecutivos", c)

    c = 0
    # hago lo mismo por columnas
    for col1 in range(0, len(matriz[0])):

        c = 0
        for columna in range(0,len(matriz[0])-2):

            if (matriz[columna,col1]+1 == matriz[columna+1,col1]):
                c = c + 1

        print("En esta Columna", col1, "hay esta cantidad de consecutivos", c)


def principal():

    """


    >>> random.seed(111)
    >>> principal()
        En esta fila [2 0 1 0 0 1 2 0 1 1] hay esta cantidad de consecutivos 2
        En esta fila [2 1 2 2 2 1 0 0 1 2] hay esta cantidad de consecutivos 2
        En esta fila [0 0 1 2 0 1 0 2 0 2] hay esta cantidad de consecutivos 4
        En esta fila [0 1 0 2 2 0 1 0 1 1] hay esta cantidad de consecutivos 2
        En esta fila [0 2 0 1 0 2 2 1 0 0] hay esta cantidad de consecutivos 3
        En esta fila [2 2 2 1 0 0 0 0 0 0] hay esta cantidad de consecutivos 3
        En esta fila [0 1 1 1 2 0 2 1 0 2] hay esta cantidad de consecutivos 2
        En esta fila [0 1 0 1 2 0 0 0 0 2] hay esta cantidad de consecutivos 1
        En esta fila [1 1 2 1 1 1 1 0 2 0] hay esta cantidad de consecutivos 2
        En esta fila [0 0 0 0 1 1 2 2 2 1] hay esta cantidad de consecutivos 1
        En esta Columna 0 hay esta cantidad de consecutivos 2
        En esta Columna 1 hay esta cantidad de consecutivos 2
        En esta Columna 2 hay esta cantidad de consecutivos 2
        En esta Columna 3 hay esta cantidad de consecutivos 2
        En esta Columna 4 hay esta cantidad de consecutivos 2
        En esta Columna 5 hay esta cantidad de consecutivos 4
        En esta Columna 6 hay esta cantidad de consecutivos 1
        En esta Columna 7 hay esta cantidad de consecutivos 1
        En esta Columna 8 hay esta cantidad de consecutivos 0
        En esta Columna 9 hay esta cantidad de consecutivos 2



    """



    array = np.random.randint(3, size=(10, 10))

    print(array)

    detectar_consecutivos(array)

    return


if __name__ == "__main__":

    doctest.testmod()