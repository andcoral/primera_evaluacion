# Contar nucleotidos en cada secuencia (4 salidas).

secuencias = input("Dame secuencias de ADN separadas por comas:\n").split(",")

# Uso de metodo .count(), genera una posicion contadora en la lista por nuecleotido
conteo = [[secuencia.count('A'), secuencia.count('T'), secuencia.count('C'), secuencia.count('G')] for secuencia in secuencias]


print(f"Dentro de cada una de tus secuencias tuviste la sig cantidad de [A,T,C,G]:\n{conteo}")