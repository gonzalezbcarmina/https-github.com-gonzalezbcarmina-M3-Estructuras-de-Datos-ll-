def factorial(n):
    valor = 1
    for i in range(1,n+1):
        valor *= i
    return valor

def productoria(lista):
    valor = 1
    for i in lista:
        valor *= i
    return valor    
    
def calcular(**kwargs):
    for k,v in kwargs.items():
        if 'fact' in k:
            print(f"El factorial de {v} es: {factorial(v)}")
        else:
            print(f"La productoria de {v} es: {productoria(v)}")



