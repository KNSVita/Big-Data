import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Planilhas
bitcoin = pd.read_excel('dados_bitcoin.xlsx')
#eurusdl = pd.read_excel('dados_EURUSDL.xlsx')
#usdbrl = pd.read_excel('dados_USDBRL.xlsx')
#petroleo = pd.read_excel('dados_WTI_Petroleo_Cru.xlsx')

#Calculo de correlação
calculo = bitcoin['close(CNY)'].corr(bitcoin['close(USD)'])
print(f"Correlação entre Bitcoin (CNY) e Bitcoin (USD): {calculo}\n")

#Variação percentual
var_pecentual = bitcoin['close(CNY)'].pct_change() * 100
var_pecentual.to_excel(CAMINHO_ARQUIVO, index=False)
print(var_pecentual)

#Grafico
x = bitcoin['close(CNY)']
y = bitcoin['close(USD)']

plt.scatter(x, y, label=f"Correlação: {calculo:.5f}", color='red')

plt.xlabel('Fechamento CNY')
plt.ylabel('Fechamento USD')
plt.title('Gráfico de Correlação do Bitcoin (CNY) e Bitcoin (USD)')

plt.legend()
plt.show()