#programa 2

import nltk_prog1
import matplotlib.pyplot as plt
carpeta_nombre="Documentos\\"
archivo_nombre = "ejemplo5.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
print("----------------------------------------------------------------------")
tokens=nltk_prog1.word_tokenize(texto, "spanish")

tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)
print(palabras_totales)
print(palabras_diferentes)
texto_nltk=nltk_prog1.Text(tokens)
distribucion=nltk_prog1.FreqDist(texto_nltk)
print("----------------------------------------------------------------------")
hapaxes=distribucion.hapaxes()
for hapax in hapaxes:
    print(hapax)
from matplotlib import rcParams
rcParams.update({"figure.autolayout": True})
distribucion.plot(cumulative=True)
distribucion.plot(40,cumulative=True)