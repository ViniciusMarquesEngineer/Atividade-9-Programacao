def numero_par(a):
    resultado = a % 2
    if resultado == 0:
        return True
    else:
        return False

resultado1 = numero_par(3)
print(resultado1)