def palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

texto = input("Digite uma palavra: ")

if palindromo(texto):
    print("True")
else:
    print("False")

''' NÃO CONSEGUI FAZER, USEI IA, MAS NÃO ENTENDI MUITO BEM!'''
