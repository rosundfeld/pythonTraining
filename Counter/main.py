from contador import contar_palavras

frase = input("Digite uma frase: ").strip()
wordSizeCount = input("Digite o tamanho mínimo de letras para contar a palvra (vazio para desconsiderar): ").strip() or 0
if not frase:
    print("Erro: Nenhuma frase foi digitada.")
else :
    resutado = contar_palavras(frase, wordSizeCount)
    if resutado:
        print("Contagem de palavras:")
        for palavra, quantidade in resutado.items():
            print(f"{palavra}: {quantidade}")
        print(f"Palavras totais: {len(resutado)}")
    if len(resutado.items()) == 0:
        print("Nenhuma palavra longa foi encontrada no texto. ")
    else:
        print("A frase não contém palavras válidas para contar.")