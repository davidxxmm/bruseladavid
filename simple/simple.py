# generar numeros aleatorios en un lista de diccionarios, considerando la edad de personas entre 1 y 100.
# ordenar en descendiente la lista, e imprimir la persona de mayor edad y la de menor edad.
# importo los modulos necesarios

import random
from operator import itemgetter
import doctest


# genero el diccionario con datos aleatorios
def generar_lista():

    # diccionario vacio
    sample_dict = {}

    #10 numeros aleatorios
    for w in range(10):

        # el primer campo con edad con el numero del 1 al 10, y en la edad el numero aleataorio entre el 1 y el 100
        edad = random.randint(1,100)
        sample_dict["edad"+str(w)] = edad

    return sample_dict

# proceso el diccionario
def procesar_dic(dic_params):

    # cuando recibo el diccionario lo convierte en lista
    ord_dic = sorted(dic_params.items(), key=itemgetter(1), reverse=True)

    # tomo el primero y el ultimo de la lista
    print("    El mas grande tiene", ord_dic[0][1])
    print("    El mas chico tiene", ord_dic[len(ord_dic)-1][1])

    return

# funcion principal
def llamadas():
    """

    returns an integer between 1 and 10
    >>> random.seed(111)
    >>> llamadas()
        El mas grande tiene 81
        El mas chico tiene 22
    >>> llamadas()
        El mas grande tiene 92
        El mas chico tiene 24
    >>> llamadas()
        El mas grande tiene 99
        El mas chico tiene 5
    >>> llamadas()
        El mas grande tiene 11
        El mas chico tiene 4

    """
    # llamado a las funciones para generar la lista aleateoria y luego imprimir resultado
    dic = generar_lista()
    procesar_dic(dic)

    return

if __name__ == "__main__":
     doctest.testmod()
