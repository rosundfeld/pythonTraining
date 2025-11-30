def limpart_texto(frase):
    texto = frase.lower()
    caracteres = ",.!|?:;/'\"(){}[]"
    for c in caracteres:
        texto = texto.replace(c, "")
    return texto

def contar_palavras(frase, wordSizeCount):
    frase = limpart_texto(frase)
    if not frase.strip():
        return {}
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        if wordSizeCount == 0:
            add_word(contagem, palavra)
        else:
            if len(palavra) >= int(wordSizeCount):
                add_word(contagem, palavra)
    return contagem

def add_word(contagemDict, palavra):
    contagemDict[palavra] = contagemDict.get(palavra, 0) + 1