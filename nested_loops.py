# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []

    for i in matrix:
        lista = lista + i
    return lista




def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """

    lista = []
    total = 0

    for i in matrix:
        total = 0
        for num in i:
            total = total + int(num)

        lista.append(total)
    return lista



def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """

    resultados = []

    for j in range(len(matrix[0])):
        suma_actual = 0

        for i in range(len(matrix)):
            suma_actual += matrix[i][j]

        resultados.append(suma_actual)
    return resultados
