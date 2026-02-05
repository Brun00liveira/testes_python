def contar_palavras(frase):
    frase = limpar_texto(frase)
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem

def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ".,!?:;\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto