#programa 3

'''José Ramón Castañeda Figueroa'''
import nltk_prog1
print("José Ramón Castañeda Figueroa")
carpeta_nombre="Documentos\\"
archivo_nombre = "ejemplo5.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
print("----------------------------------------------------------------------")
palabras_funcionales=nltk_prog1.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    '''print(palabras_funcional)'''
print("----------------------------------------------------------------------")
tokens=nltk_prog1.word_tokenize(texto,"spanish")
tokens_limpios=[]
for token in tokens:
    if token not in palabras_funcionales:

        tokens_limpios.append(token)
'''print(tokens_limpios)'''
print(len(tokens))
print(len(tokens_limpios))
texto_limpio_nltk=nltk_prog1.Text(tokens_limpios)
distribucion_limpia=nltk_prog1.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)