def vowel_counter(phase):
    vowels = 'aeiouáéíóúâêîôûãõàèìòùäëïöü'
    count = 0
    totalVowels = {}
    for char in phase.lower():
        if char in vowels:
            totalVowels[char] = totalVowels.get(char, 0) + 1
            count += 1
    return totalVowels # retorna um iterador de tuplas (vogal, quantidade)
           

