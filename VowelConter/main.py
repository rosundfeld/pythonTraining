from vowel_counter import vowel_counter

def main():
    phase = input("Digite uma frase: ")
    result = vowel_counter(phase)
    total_= 0
    for vowel, qtd in result.items():
        print(f"{vowel}: {qtd}")
        total_ += qtd
    print(f"Número de vogais na frase: {total_}")

main()