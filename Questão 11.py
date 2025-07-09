def fatorial():
    n = int(input("Digite um número inteiro: "))
    if n == 0 or n == 1:
       return 1
    else:
       return (n * fatorial2(n - 1))
    
def fatorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial2(n - 1)

print("Resultado do fatorial:", fatorial())