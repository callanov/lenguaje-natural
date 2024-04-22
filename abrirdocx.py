from docx import Document

def contar_palabras_y_lineas(texto):
    palabras = texto.split()
    lineas = texto.split('\n')
    return len(palabras), len(lineas)

def contar_apariciones_palabra(texto, palabra):
    return texto.lower().count(palabra.lower())

def guardar_texto_en_archivo(texto, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

def analizar_documento(docx_file):
    doc = Document(docx_file)
    texto = ""
    for para in doc.paragraphs:
        texto += para.text + '\n'

    # Guardar el texto en un archivo de texto
    guardar_texto_en_archivo(texto, "texto_pagina.txt")

    # Contar palabras y líneas
    num_palabras, num_lineas = contar_palabras_y_lineas(texto)

    # Contar apariciones de una palabra específica
    palabra_a_contar = "palabra"
    apariciones_palabra = contar_apariciones_palabra(texto, palabra_a_contar)

    print("Número de palabras:", num_palabras)
    print("Número de líneas:", num_lineas)
    print(f"Número de veces que aparece la palabra '{palabra_a_contar}':", apariciones_palabra)

# Guardar el texto extraído en un archivo de texto
if guardar_texto_en_archivo:
    with open("texto_pagina.txt", "w", encoding="utf-8") as archivo:
        archivo.write(guardar_texto_en_archivo)

# Cargar el texto del archivo
archivo_nombre = "texto_pagina.txt"
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(20)

if __name__ == "__main__":
    archivo_docx = "Documentos\ejemplo1.docx"  
    analizar_documento(archivo_docx)

