"""

Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

"""

def word_repetitve(text):
    text = text.lower()
    text = "".join(c if c.isalnum() or c.isspace() else "" for c in text)   # Esto hace que a text lo iguala a un string vacio y que le une la letra si es un alfanumerico o un espacio por medio de un for en el text
    # En si aqui se hace una condicional dentro del valor de una variable y se agrega la letra que se ubica con la iteracion que se hace con el loop for
    palabras = text.split()

    recuento_palabras = {}

    for palabra in palabras:
        recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

    print("Recuento final de palabras:")
    for palabra, frecuencia in recuento_palabras.items():
        print(f"{palabra}: {frecuencia}")

texto_ejemplo = """
Este es un ejemplo de programa que cuenta cuántas veces se repite cada palabra.
Los signos de puntuación no forman parte de la palabra.
Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
No se pueden uti.lizar funci.......................................................ones propias del lenguaje que lo resuelvan automáticamente.
"""

word_repetitve(texto_ejemplo)

