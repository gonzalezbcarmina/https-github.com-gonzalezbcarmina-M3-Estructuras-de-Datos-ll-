velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
import math
import time

def promedio(lista):
    """Este método obtiene el promedio de las velocidad de la lista"""
    return sum(lista)/len(lista)

def filtrar(lista):
    """Este método retorna una lista con la posición de cada elemento que este por sobre 
    el promedio de la lista
    
    Parameters
    ----------
    lista (list): lista con los valores que se desean filtrar.
    
    Returns
    -------
    list: Lista con los valores que cumplen el criterio del filtro
    """
    velocidad_promedio = promedio(lista)
    listaCorreasVeloces = []
    '''
    for i in range(len(lista)):
        if (lista[i] > velocidad_promedio):
            listaCorreasVeloces.append(i)
    '''
    
    listaCorreasVeloces = [i for i,v in enumerate(lista) if v > velocidad_promedio ]
    return listaCorreasVeloces    
    

print(promedio(velocidad))
print(filtrar(velocidad))

#__doc__ permite imprimir la documentación de un método.
print(filtrar.__doc__)

print(math.__doc__)


#help(math)
help(filtrar)
#help(time)

