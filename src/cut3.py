# Extraer primeros 3 nucleotidos de secuencias dadas. Comprension de listas

secuencias = input("Dame secuencias separadas por comas:\n").split(",")

# Encerrar en corchetes lo vuelve lista
codones_inicio = [secuencia.strip()[:3] for secuencia in secuencias]

print(codones_inicio)