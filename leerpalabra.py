import os

carpeta_nombre = "Documentos\\"
archivos_nombre = "ejemplo3.txt"

with open(carpeta_nombre+archivos_nombre, "r") as archivo:
    texto=archivo.read()

palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)