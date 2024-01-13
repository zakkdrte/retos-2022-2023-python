list1 = ["[","]","(",")","{","}"]

def verificated (str):
    my_expression = []
    for i in str:
        if i in list1:
            my_expression.append(i)
        else:
            pass
            
    if my_expression[:3] == ["{","[","("] and my_expression[-3:] == [")","]","}"]:
        return f"{str} son expresiones equilibradas"
    else:
        return f"{str} no son expresiones equilibradas"

my_expressions = verificated(input("anota el string que verificaras si estan equilibradas sus expreciones: "))
print(my_expressions)