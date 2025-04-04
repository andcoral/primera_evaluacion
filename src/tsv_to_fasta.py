# A partir un archivo en formato tsv, crear otro en formato fasta.

inputfile = "../data/dna_sequences.txt"
outputfile = "../results/dna_sequences.faa"

# Abrir y leer el archivo de entrada
with open(inputfile, "r") as infile, open(outputfile, "w") as outfile:
    for linea in infile:
        id, seq = linea.strip().split("\t")
        outfile.write(f">{id}\n{seq.upper()}\n") # El metodo .upper() convierte en mayusculas 