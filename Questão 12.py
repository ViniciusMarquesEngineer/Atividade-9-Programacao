def contar_vogais(palavra):
    palavra = palavra.lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais('Python'))