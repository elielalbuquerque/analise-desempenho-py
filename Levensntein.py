from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
import json
from statistics import mean
import psutil
import timeit
inicio = timeit.default_timer()


path = "C:/Temp/Dicionario/Lista-de-Palavras.json"

with open(path, 'r', encoding = "utf8") as j:
    dt = json.load(j)
str2Match = "abacaxi"
strOptions = dt
ratio = 0
VETRATIO = []
VETITENS = []
VETthisRatio = []
vetAcuracia = []
vetAcuracia2 = []
totalregistros = 0
acuracia = 0
vetpalavras = []
for item in dt["DICIONARIO"]:
    #thisRatio =  fuzz.ratio(str2Match,item)
    #thisRatio =  fuzz.partial_ratio(str2Match,item)
    #thisRatio =  fuzz.token_sort_ratio(str2Match,item)
    thisRatio =  fuzz.token_set_ratio(str2Match,item)
    
    if thisRatio > ratio:
        totalregistros += 1
        VETRATIO.append(ratio)
        VETthisRatio.append(thisRatio)
        VETITENS.append(item)
        ratio = thisRatio
        vetpalavras.append(item['PALAVRA'])
       
fim = timeit.default_timer() 


# In[69]:
print("min")
print( min(VETthisRatio) )
print("mean")
print( mean(VETthisRatio) )
print("max")
print(max(VETthisRatio))
strLen = len(dt["DICIONARIO"])
print ('Total de Palavras: %.0f' % strLen)
print ('Duracao calculo Ratios: %.2f' % (fim - inicio))



plt.plot(VETRATIO,VETthisRatio)
plt.ylabel('RATIOS')
plt.xlabel('SIMILARIDADE')
plt.show()


# Este gráfico simula a participação dos 5 produtos agrícolas mais produzidos no Brasil

# Definindo os produtos, que vão para o eixo X


# Definindo as participações que formarão o eixo Y
#palavras = ['A-BE-CE', 'A-TOA', 'ABA', 'ABACATE', 'ABACATEIRO', 'ABACAXI']

# Semelhando ao bar() temos o barh()
plt.barh(vetpalavras, VETthisRatio, color='green')

# A partir daqui não muda nada
plt.ylabel("Similaridade")
plt.xlabel("fuzz.ratio")
plt.title("Processamento fuzz.ratio")

plt.show()
