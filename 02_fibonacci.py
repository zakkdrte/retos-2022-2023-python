def fibonacci(number_limit):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < number_limit:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
        
    return fibonacci_sequence[:number_limit]
    

fibonacci_50 = fibonacci(50)
print("Los primeros 50 números de la sucesion de Fibonacci son:")
print(fibonacci_50)
