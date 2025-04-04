# Invierte secuencias de ADN con comprension de listas.

secuencias = input("Dame secuencias de ADN separadas por comas:\n").split(",")

# Crea una lista despes de eliminar espacios, invertir
secuencias_invertidas = [secuencia.upper().strip()[::-1] for secuencia in secuencias]
print(f"Tus secuencias invertidas son:\n{secuencias_invertidas}")