"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.

"""
my_dict = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ü': 'u', 'Ü': 'U', 'ñ': 'n', 'Ñ': 'N'
    }
my_test_palindromo = []

def function(text):
    for i in text:
        if i in my_dict:
            my_test_palindromo.append(my_dict[i])
        elif i == " ":
            pass
        else:
            my_test_palindromo.append(i)
    my_str = "".join(my_test_palindromo)
    my_str = my_str.lower()
    
    if my_str == my_str[::-1]:
        return (f"el string: [{text}] es un palindromo😎😎😎")
    elif my_str != my_str[::-1]:
        return (f"El string: [{text}] no es un palindromo😕😕😕")

my = function("amor junto con noc otnuj roma")
print(my)