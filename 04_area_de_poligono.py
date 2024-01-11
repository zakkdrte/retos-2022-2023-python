from math import sqrt

def area_poligonos (base, *perimetro):
    if len(perimetro) == 2:
        datos = list(perimetro)
        dt = (datos[0] + datos[1] + base) / 2
        altura = (2 * sqrt(dt * (dt - datos[0]) * (dt - datos[1]) * (dt - base) )) / base
        area = altura * base / 2
        return area
    elif len(perimetro) == 3:
        datos = list(set(perimetro))
        if len(datos) == 1:
            area = base * datos[0]
            return area
        elif len(datos) == 2:
            altura = min(datos)
            area = altura * base 
            return area
        else:
            return "**No es posible con esos tipos de datos**"
    else:
        return  "**Datos insuficientes**" 

tríangulo = area_poligonos(5, 9, 7)
cuadrado = area_poligonos(4, 8, 8, 4)
rectángulo = area_poligonos(9, 8, 9, 8)
print("area de triángulo")
print(tríangulo)
print("area de cuadrado")
print(cuadrado)
print("area de rectángulo")
print(rectángulo)