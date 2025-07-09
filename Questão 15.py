def analise_lista(lista):
    m = maior(lista)
    me = menor(lista)
    soma = 0
    for i in lista:
        soma += 1
    media = soma/len(lista)
    return m, me, media

def maior(lista):
    m = 0 
    for i in lista:
        if i > m:
            m = i
    return m

def menor(lista):
    m = lista[0]
    for i in lista:
        if i < m:
            m = i
    return m

print(analise_lista([10, 20, 30]))