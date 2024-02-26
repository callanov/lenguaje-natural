carpeta_nombre="documentos\\"
archivo_nombre="ejemplo1.txt"

with open (archivo_nombre, "r") as archivo: #la r significa el modo en que lo abres
    lineas_lista = archivo.readlines()

# print(lineas_lista) para imprimir todo en una misma linea
    
#for linea in lineas_lista:
#    print(linea)
#    print() # esto es una linea vacia
    
num_linea = 0
num_vacios = 0

print()

for linea in lineas_lista:
    if linea.strip() == "":
        num_vacios = num_vacios+1 
        continue
    num_linea=num_linea+1
    print("num_linea ", num_linea, " : ", linea) 
print()
print("numero de lineas con texto: ",num_linea, " y numero de lineas vacias: ", num_vacios)
print()