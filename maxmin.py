def maior_menor(lista):
    if not lista:
        return None, None
    maior = lista[0]
    menor = lista[0]
    for x in lista[1:]:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    return maior, menor