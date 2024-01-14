'''
*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */

'''


def cadena(str1,str2):
    out1 = ""
    out2 = ""
    for i in str1:
        if not(i in str2):
            out1 += i
            
    for i in str2:
        if not(i in str1):
            out2 += i
    print(f"""
          Este es el primer output:     [{out1}]\n\n
          
          Este es el segundo output:    [{out2}]\n\n
          
          """)
            

string1 = input("escribe tu primer string:\n")
string2 = input("escribe tu segundo string:\n")

cadena(string1, string2)