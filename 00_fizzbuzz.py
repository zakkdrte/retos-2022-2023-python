# Primera forma de conseguirlo

for element in range(1, 101):

    if element % 3 == 0 and element % 5 == 0:
        print("fizzbuzz")
    elif element % 3 == 0:
        print("fizz")
    elif element % 5 == 0:
        print("buzz")
    else:
        print(element)

# Segunda forma de conseguirlo

my_variable = 1

while my_variable < 101:
    if my_variable % 3 == 0 and my_variable % 5 == 0:
        print("fizzbuzz")
    elif my_variable % 3 == 0:
        print("fizz")
    elif my_variable % 5 == 0:
        print("buzz")
    else:
        print(my_variable)
    my_variable += 1