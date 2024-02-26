semana_laboral = ["lunes", "martes", "miercoles", "jueves", "viernes"]
print("semana laboral = ", semana_laboral)
print("dia 5 = ", semana_laboral[4])
semana_laboral[4] = "sabado"
print("semana laboral = ", semana_laboral)
semana_laboral[4] = "viernes"
longitud_lista = len(semana_laboral)
print("longitud = ", longitud_lista)
posicion = semana_laboral.index("miercoles")
print("posicion del miercoles = ", posicion)
semana_laboral.append("sabado")
print("semana laboral = ", semana_laboral)
del semana_laboral[4]
print("semana laboral = ", semana_laboral)