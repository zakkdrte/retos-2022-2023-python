numbers = []
introduce_number = input("Da el numero que quieres convertir a binario: ")
number = int(introduce_number)
total_numbers = []

while number > 0:
    
    result = number % 2
    number = int(number / 2)
    total_numbers.append(result)

if len(total_numbers) == 0:
    total_numbers.append(0)

total_numbers.reverse()

print(f"Este es su numero a binario: {total_numbers}")