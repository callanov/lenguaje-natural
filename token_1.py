import nltk
nltk.download('punkt')

carpeta_nombre="Documentos\\"
archivo_nombre="ejemplo5.txt"

with open(carpeta_nombre+archivo_nombre, "r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto, "aguja")

for token in tokens:
    tokens_conjunto=set(tokens)
    total_palabras=len(tokens)
    palabras_diferentes=len(tokens_conjunto)
    riqueza_lexica=palabras_diferentes/total_palabras
    print(riqueza_lexica)
    print("el total de palabras es: ", total_palabras)
    print(token)