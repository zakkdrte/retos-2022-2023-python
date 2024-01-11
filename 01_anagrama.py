def validate_anagram(first_word, second_word):
    if len(first_word) != len(second_word) or first_word.lower() == second_word.lower():
        return False
    else:
        return sorted(first_word.lower()) == sorted(second_word.lower())
    
first_word = input("La palabra será: ")
second_word = input("La otra palabra será: ")

result = validate_anagram(first_word, second_word)

if result:
    print(f"{first_word} y {second_word} son anagramas")
else:
    print(f"{first_word} y {second_word} no son anagramas")