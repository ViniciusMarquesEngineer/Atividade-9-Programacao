import random

def simular_dado(n):
    lista = []
    for i in range (n): #Vou percorrer a quantiade n de vezes que a rolagem do dado irá rolar
        a = random.randint(1, 6)  # Simula a rolagem de um dado de 6 lados
        lista.append(a)
    return lista

resultado = simular_dado(int(input("Digite a quantidade de vezes que deseja rolar o dado: ")))
print("Resultado da simulação:", resultado)