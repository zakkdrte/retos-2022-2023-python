# Escribe una función que calcule si un número dado es un número de Armstrong
# (o también llamado narcisista).

def armstrong(num:int):
    num_list = list(str(num)) 
    potencia = len(num_list) 
    numeros = []
    numeros_potenciales = []
    sumatoria_de_numeros = 0
    for i in num_list:
        numeros.append(int(i) ** potencia)
        numeros_potenciales.append(f"{i} elevado a {potencia}")        
    for index in numeros:
        sumatoria_de_numeros += index
    
    if num == sumatoria_de_numeros:
        return f"EL NUMERO {num} ES UN NUMERO NARCISISTA DEBIDO A QUE LA SUMATORIA\nDE CADA UNO DE SUS DIGITOS ELEVADOS A LA POTENCIA DE LA CANTIDAD\nDE LOS DIGITOS {numeros_potenciales}\nES IGUAL A EL MISMO NUMERO {num}\n\n"
    else:
        return f"EL NUMERO {num} NO ES UN NUMERO NARCISISTA, DEBIDO A QUE LA SUMATORIA\nDE CADA UNO DE SUS DIGITOS ELEVADOS A LA POTENCIA DE LA CANTIDAD\nDE LOS DIGITOS {numeros_potenciales}\nNO ES IGUAL AL MISMO NUMERO {num}"
print(armstrong(153))
print(armstrong(152))
