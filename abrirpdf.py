import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

nltk.download('punkt')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

def analyze_text(text):
    words = word_tokenize(text)
    
    total_words = len(words)
    
    fdist = FreqDist(words)
    
    single_occurrence_words = len(fdist.hapaxes())
    
    print("Palabras más comunes:")
    print(fdist.most_common(20))
    
    fdist.plot(20, cumulative=False)
    plt.show()
    
    return total_words, single_occurrence_words, fdist

pdf_path = "Documentos\ejemplo1.docx"

text = extract_text_from_pdf(pdf_path)

total_words, single_occurrence_words, fdist = analyze_text(text)

print(f"Total de palabras: {total_words}")
print(f"Palabras que aparecen una sola vez: {single_occurrence_words}")
