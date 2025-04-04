# Tansforma secuencias de ADN en ARN. Comprension de listas.

secuencias = input("Dame secuencias de ADN separadas por comas:\n").split(",")

# Uso del metodo .replace()
secuencias_arn = [secuencia.strip().upper().replace("T","U") for secuencia in secuencias]

print(f"Las secuencias en ARN son:\n{secuencias_arn}")