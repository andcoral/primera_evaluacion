# Identifica secuencias que contienen codones de paro (TAA, TAG, TGA).

secuencias = input("Dame secuencias separadas por comas:\n").split(",")

# RESULTADO/Valor a guardar (secuencia) | Iterable (ciclo for) | Filtrado (if)
secuencias_stop = [secuencia for secuencia in secuencias if "TAA" in secuencia or "TAG" in secuencia or "TGA" in secuencia]

print(f"Las secuencias que contuvieron codones de paro fueron:\n{secuencias_stop}")