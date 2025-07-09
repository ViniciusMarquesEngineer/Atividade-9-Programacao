def maior_numero(a, b, c):
    if a > b and a > c:
        return print(f"O maior número é: {a}")
    elif b > a and b > c:
        return print(f"O maior número é: {b}")
    else:
        return print(f"O maior número é: {c}")

teste = maior_numero(10, 20, 30)
print(teste)