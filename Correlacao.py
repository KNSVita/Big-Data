def grafico_correlacao():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    bitcoin = pd.read_excel('dados_bitcoin.xlsx')
    eurosdl = pd.read_excel('dados_EURUSDL.xlsx')
    usdbrl = pd.read_excel('dados_USDBRL.xlsx')

    Bitcoin_CNY = bitcoin['close(CNY)']
    Bitcoin_USD = bitcoin['close(USD)']
    EuroSdl= eurosdl['close']
    UsdBrl = usdbrl['close']

    dadosPlanilha = [Bitcoin_CNY,Bitcoin_USD,EuroSdl,UsdBrl]

    opcao1 = "Bitcoin(CNY)"
    opcao2 = "Bitcoin(USD)"
    opcao3 = "EUROSDL"
    opcao4 = "USDBRL"

    opcoes = [opcao1,opcao2,opcao3,opcao4]

    print("Escolha com quais dados será feita a correlação.\n")
    print(f"(0)-{opcao1}", 
            f"(1)-{opcao2}", 
            f"(2)-{opcao3}",
            f"(3)-{opcao4}\n")

    planilha1 = int(input("Primeira escolha: "))
    planilha2 = int(input("Segunda escolha: "))

    if planilha1 > 3 or planilha1 < 0 or planilha2 > 3 or planilha2 < 0:
        print("Escolha uma opção válida!")
        grafico_correlacao()
    elif planilha1 == planilha2:
        print("Você não pode selecionar os memos dados!!")
        grafico_correlacao()
    else:
        operador1 = dadosPlanilha[planilha1]
        operador2 = dadosPlanilha[planilha2]

        calculo = operador1.corr(operador2)
        print(f"\nO resultado da correlação é: {calculo}")

        plt.scatter(operador1, operador2, label=f"Correlação: {calculo:.5f}", color='red')

        eixo_x = opcoes[planilha1]
        eixo_y = opcoes[planilha2]

        plt.title(f"Gráfico de correlação do {eixo_x} e {eixo_y}")
        plt.xlabel(eixo_x)
        plt.ylabel(eixo_y)

        plt.legend()
        plt.show()