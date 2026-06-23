def encontrar_duplicados(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                if lista[i] == lista[j]:
                    if lista[i] not in duplicados:
                        duplicados.append(lista[i])
    return duplicados

def calcular_promedio(numeros):
    suma = 0
    lista_copia = []
    for n in numeros:
        lista_copia.append(n)
    for n in lista_copia:
        suma = suma + n
    resultado = suma / len(lista_copia)
    return resultado

def buscar_elemento(lista, elemento):
    encontrado = False
    posicion = -1
    for i in range(len(lista)):
        if lista[i] == elemento:
            encontrado = True
            posicion = i
    if encontrado:
        return posicion
    else:
        return -1
