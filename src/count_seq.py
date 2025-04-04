# Contar secuencias en un archivo usando comprension de listas.

inputfile = "../results/dna_sequences.faa"

with open(inputfile, "r") as infile:
    lineas = infile.readlines() # Guarda cada linea en una posicion de lista

# Recorre lista recien creada buscando el identificador, y guardandolo
lineas_filtradas = [linea for linea in lineas if linea.startswith(">")]
# RESULTADO/Valor a guardar (linea) | Iterable (ciclo for) | Filtrado (linea)
print(f"El total de secuencias es: {len(lineas_filtradas)}")
        