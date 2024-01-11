def es_primo(numero= None):
    if numero is None or numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

for i in range(0, 101):
    if es_primo(i):
        print(i)
