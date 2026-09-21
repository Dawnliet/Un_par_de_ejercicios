# La idea de la solución es encontrar la columna n que tenga más elementos al inicio
# Para cualquier columna con menos elementos vamos a usar menos pasos moviendo 
# sus elementos a n

# En caso de tener otra columna con la misma cantidad de elementos que n retornamos la menor
# Esto último ya por especificaciones del ejercicio

def Alinear(mapa:list):
    # Para saber la cantidad de columnas encontramos cuantos elementos tiene una fila cualquiera
    cantidad_columnas = len(mapa[0])
    # Luego guardamos el índice de las columnas con mayor cantidad de elementos 
    # y cuantos elementos tiene
    columnas_mayores = []
    max_de_elementos = 0
    
    for i in range(cantidad_columnas):
        columna_i = []
        for fila in mapa:
            # Esto para trabajar con cada columna independientemente 
            columna_i.append(fila[i])
            
            cantidad_elementos = sum(columna_i)
            # En caso de que la columna actual tenga más elementos que las anteriores
            # actualizamos el máximo, limpiamos la lista de columnas mayores y agregamos el
            # índice de esta nueva lista
            if cantidad_elementos > max_de_elementos:
                max_de_elementos = cantidad_elementos
                columnas_mayores = []
                columnas_mayores.append(i)
            elif cantidad_elementos == max_de_elementos:
                columnas_mayores.append(i)
    
    # Finalmente retornamos la columna con menor índice
    columna_final = min(columnas_mayores)
    return columna_final    

caso_prueba = Alinear([
    [0,1,1],
    [0,1,1],
    [0,1,1]])
print(f"Columna esperada: 1 \nColumna retornada:{caso_prueba}\n")

caso_prueba = Alinear([
    [0,0,0],
    [0,0,0],
    [0,0,1],
    [0,0,0]])
print(f"Columna esperada: 2 \nColumna retornada:{caso_prueba}\n")

caso_prueba = Alinear([
    [0,1,1,0,1],
    [0,1,1,1,0],
    [0,1,1,0,0],
    [1,0,0,1,1]])
print(f"Columna esperada: 1 \nColumna retornada:{caso_prueba}\n")