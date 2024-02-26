import re

carpeta_nombre="Documentos\\"
archivos_nombre = "ejemplo1.txt"

with open(carpeta_nombre+archivos_nombre, "r") as archivo:
    texto=archivo.read()

expresion_regular=re.compile(r"vaca+") # esta r siginifica que se buscara una expresion regular, para que otras funciones no interfieran
resultado_busqueda= expresion_regular.finditer(texto)

for resultado in resultado_busqueda:
    print(resultado.group(0))

