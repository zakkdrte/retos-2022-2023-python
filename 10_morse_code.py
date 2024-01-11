"""
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
    https://es.wikipedia.org/wiki/Código_morse.
"""
morse_iterable = {
    'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..",
    'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
    's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--..",
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}
morse_iterable_1 = {
    ".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd', ".": 'e', "..-.": 'f', "--.": 'g', "....": 'h', "..": 'i',
    ".---": 'j', "-.-": 'k', ".-..": 'l', "--": 'm', "-.": 'n', "---": 'o', ".--.": 'p', "--.-": 'q', ".-.": 'r',
    "...": 's', "-": 't', "..-": 'u', "...-": 'v', ".--": 'w', "-..-": 'x', "-.--": 'y', "--..": 'z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

code = []
def morse_code(word):

    if word[0] == '.' or word[0] == '-':        # Aqui se pone una condicional si el dato que se añade es un codigo morse o no
        word_divided = word.split("  ")
        for i in word_divided:
            i_string = str(i)
            i_split = i_string.split()
            for index in i_split:
                if index in morse_iterable_1:
                    code.append(morse_iterable_1[index])
            code.append(" ")
    else:
        word_divided = list(word)
        for i in word_divided:
            i_lower = i.lower()
            if i_lower in morse_iterable:
                
                code.append(morse_iterable[i_lower])        # Al poner entre corchetes aceden al valor de un diccionario
                code.append(" ")
            else:
                code.append("  ")
    return code
print("si quieres transformar de codigo morse a alfanumerico, escribe 'morse', y si quieres lo contrario, escribe 'alpha'")
def input_morse_or_alpha(inputs):

    
    inputs = inputs.lower()

    if inputs == "morse":
        print("escribe el codigo morse que quieres que se convierta a alpha:")
        result = morse_code(input(''))
        print("".join(result))

    elif inputs == "alpha":
        print("escribe el alfanumerico que quieres convertir a morse:")
        result = morse_code(input(''))
        print("".join(result))
    else:
        print("Ha ourrido un error, no es posible averiguar que oracion quieres convertir, verfica si has ingresado correctamente la palabara clave")
    pass

input_morse_or_alpha(input(""))



