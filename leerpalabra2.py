carpeta_nombre="Documentos\\"
archivos_nombre = "ejemplo4.txt"

with open(carpeta_nombre+archivos_nombre, "r") as archivo:
    texto=archivo.read()

simbolos=["(",")",",",".",";",":","\""]

for simbolo in simbolos:
    texto=texto.replace(simbolo," " + simbolo + "")

palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)