# Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
index=[1]
def factorial(num):
    contador = 1
    while contador < num:
        contador +=1
        index.append(index[-1]*contador)
        print(index)
        
    result = index[-1]
    return result

print(factorial(50))