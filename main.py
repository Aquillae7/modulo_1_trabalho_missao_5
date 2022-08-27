import random
from faker import Factory
from wordcloud import WordCloud
import matplotlib.pyplot as plt
fake = Factory.create('pt_BR')
lista_palavras = []
lista_pontos = []
def numeros_em_texto(inteiro):
    if inteiro == '1':
        return "Um"
    elif inteiro == '2':
        return "Dois"
    elif inteiro == '3':
        return "Tres"
    elif inteiro == '4':
        return "Quatro"
    elif inteiro == '5':
        return "Cinco"
    elif inteiro == '6':
        return "Seis"
    elif inteiro == '7':
        return "Sete"
    elif inteiro == '8':
        return "Oito"
    elif inteiro == '9':
        return "Nove"
    elif inteiro == '10':
        return "Dez"
###
for _ in range(0, 30):
    with open("lista_nomes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(fake.first_name() + ":" + str(random.randint(1, 10)) + '\n')
### d
with open("lista_nomes.txt", "r") as arquivo:
    texto = arquivo.readlines()
###
for valores in texto:
    temp = valores.replace("\n", "").split(":")
    lista_palavras.append(numeros_em_texto(temp[1]))
    lista_pontos.append(int(temp[1]))
###
wordcloud = WordCloud().generate(str(lista_palavras).replace("'", ""))
nuvem_palavras = plt
nuvem_palavras.imshow(wordcloud, interpolation='bilinear')
nuvem_palavras.axis("off")
nuvem_palavras.show()
###
histori = plt
histori.hist(lista_pontos, bins=10)
histori.show()