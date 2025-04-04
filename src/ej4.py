# Leer un archivo de entrada, eliminarle los adaptadores (primeras 14 letras) a cada secuencia y guardar este resultado en otro archivo

# Guarda en variables archivos que se emplearan
inputfile = "../data/4_input_adapters.txt" 
outputfile = "../results/4_input_no_adapters.txt"

# Abre y lee ("r") el archivo de entrada 4_input_adapters.txt. A la par que el 4_input_no_adapters.txt para ir escribiendo ("w") en el.
with open(inputfile,"r") as infile, open(outputfile,"w") as outfile: # "infile" y "outfile" nombrados por convencion.
    for linea in infile:
        # Corta lo pedido
        secuencia_limpia = linea.strip()[14:] # Guarda en variable "secuencia_limpia" de la posicion 14 (15) en adelante

        # Guarda en el nuevo archivo lo solicitado
        outfile.write(f"{secuencia_limpia}\n")

        # Otra opcion para la linea 14 seria: 
        # print(secuencia_limpia, file=outfile, end="\n")