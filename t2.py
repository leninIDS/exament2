import random


def crear_matriz(n):
    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(99, 999))
        matriz.append(fila)

    return matriz



def mostrar_matriz(matriz):
    print("\nMATRIZ GENERADA:\n")

    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:4}", end=" ")
        print()



def contar_multiplos(matriz, fila_inicio, fila_fin,
                     col_inicio, col_fin):

    
    if fila_inicio == fila_fin and col_inicio == col_fin:

        valor = matriz[fila_inicio][col_inicio]

        if valor % 5 == 0 or valor % 7 == 0:
            return 1
        else:
            return 0

    
    fila_media = (fila_inicio + fila_fin) // 2
    col_media = (col_inicio + col_fin) // 2

    total = 0

    
    if fila_inicio <= fila_media and col_inicio <= col_media:
        total += contar_multiplos(
            matriz,
            fila_inicio,
            fila_media,
            col_inicio,
            col_media
        )

    
    if fila_inicio <= fila_media and col_media + 1 <= col_fin:
        total += contar_multiplos(
            matriz,
            fila_inicio,
            fila_media,
            col_media + 1,
            col_fin
        )

    
    if fila_media + 1 <= fila_fin and col_inicio <= col_media:
        total += contar_multiplos(
            matriz,
            fila_media + 1,
            fila_fin,
            col_inicio,
            col_media
        )

    
    if fila_media + 1 <= fila_fin and col_media + 1 <= col_fin:
        total += contar_multiplos(
            matriz,
            fila_media + 1,
            fila_fin,
            col_media + 1,
            col_fin
        )

    return total



n = int(input("Ingrese el tamaño de la matriz NxN: "))

matriz = crear_matriz(n)

mostrar_matriz(matriz)

cantidad = contar_multiplos(
    matriz,
    0,
    n - 1,
    0,
    n - 1
)

print("\nCantidad de números múltiplos de 5 o 7:", cantidad)