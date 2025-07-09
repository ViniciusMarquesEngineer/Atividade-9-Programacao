def contar_palavras(string):
    palavra = string.split()
    return len(palavra)

frase = contar_palavras(input('Digite uma frase: '))
print(frase)

