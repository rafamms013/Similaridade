import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter as MyCounter

def custom_preprocess(text):  
    tokenizer = RegexpTokenizer(r'\b[A-Za-zÀ-ú]+\b')
    tokens = tokenizer.tokenize(text)

    stop_words = set(stopwords.words('portuguese'))
    tokens = [word.lower() for word in tokens if word.lower() not in stop_words and word.isalpha()]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


def get_synonyms_custom(word): 
    synonyms = []
    for syn in wordnet.synsets(word, lang='por'):
        for lemma in syn.lemmas('por'):
            synonyms.append(lemma.name())
    return synonyms


def calcular_overlap_percent_custom(text1_keywords, text2_keywords): 
    overlap_count = sum((text1_keywords & text2_keywords).values())
    total_terms = sum((text1_keywords | text2_keywords).values())

    if total_terms == 0:
        return 0
    else:
        return (overlap_count / total_terms) * 100


def calcular_occlusion_percent_custom(occlusion_count, total_keywords): 
    if total_keywords == 0:
        return 0
    else:
        return (occlusion_count / total_keywords) * 100


def custom_get_keywords(file_path, n_kw): 
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = custom_preprocess(text) 

    keywords = MyCounter(tokens) 

    keywords = keywords.most_common(n_kw)

    return [keyword[0] for keyword in keywords]


def custom_main(): 
    print("------------Inserindo o caminho dos arquivos:-------------------")
    file_path1 = input("Digite o nome do Primeiro arquivo txt: ")
    file_path2 = input("Digite o nome do Segundo arquivo  txt: ")
    
    n_keywords = int(input("Qual o número de palavras-chave que deseja: "))

    keywords1 = custom_get_keywords(file_path1, n_keywords)  
    keywords2 = custom_get_keywords(file_path2, n_keywords) 

    occlusions_count = len(set(keywords1) & set(keywords2))

    consider_synonyms = input("Usar sinônimos? (S/N): ").lower()
    if consider_synonyms == 's':
        for word in set(keywords1):
            synonyms = get_synonyms_custom(word)
            for synonym in synonyms:
                if synonym in set(keywords2):
                    keywords2.append(synonym)
                    occlusions_count += 1

    total_keywords = len(set(keywords1 + keywords2))
    occlusion_percentage = calcular_occlusion_percent_custom(occlusions_count, total_keywords)

    print("|--------------------------------------------------------------------|")
    print("\nPalavras-chave do Texto 1:", keywords1)
    print("|--------------------------------------------------------------------|")
    print("\nPalavras-chave do Texto 2:", keywords2)
    print("|--------------------------------------------------------------------|")
    print("\nOclusões entre os Textos:", occlusions_count)
    print("|--------------------------------------------------------------------|")
    print("Calculando a Oclusão dos termos...")
    print("\nPercentual numérico:", occlusion_percentage, "%")
    print("|--------------------------------------------------------------------|")


if __name__ == "__main__":
    custom_main() 


