my_dict = {'[':']', '(':')', '{':'}',}
my_other_dict = { ']':'[', ')':'(', '}':'{'}
my_exprection = []

def verification(exprection):
    exprection = list(exprection)
    for i in exprection:
        if exprection[i] in my_dict:
            my_exprection.append(my_dict[exprection[i]])

        elif exprection[i] in my_exprection:
            my_exprection[i].insert(exprection[i])

        elif exprection[i] not in my_dict and my_other_dict:
            my_exprection[i].insert(exprection[i])

    return my_exprection

expresion_balanceada = "{[ a * ( c + d ) ] - 5}"

print(verification(expresion_balanceada))