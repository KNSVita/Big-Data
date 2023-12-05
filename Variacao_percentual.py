def variacao_pct():
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

    print("Escolha com qual planilha será feita a variação percentual.\n")
    print(f"(0)-{opcao1}", 
            f"(1)-{opcao2}", 
            f"(2)-{opcao3}",
            f"(3)-{opcao4}\n")
    escolha = int(input("Digite sua opção: "))

    if escolha > 3 or escolha < 0:
        print('Não existe a opção escolhida, escolha uma válida!')
        variacao_pct()
    else:
        operador = dadosPlanilha[escolha]
        nomeOperador = opcoes[escolha]

        var_percen = operador.pct_change() * 100
        var_percen.to_excel(f"Variação percentual de {nomeOperador}.xlsx",index=False)
        print(var_percen)

        mediaVariacao = dadosPlanilha[escolha].mean()
        maxVariacao = dadosPlanilha[escolha].max()
        minVariacao = dadosPlanilha[escolha].min()

        print(f"\nMédia de variação percentual: {mediaVariacao:.2f}%\n")
        print(f"Máxima de variação percentual: {maxVariacao:.2f}%\n")
        print(f"Minima de variação percentual: {minVariacao:.2f}%\n")

        if mediaVariacao > 0:
                print("O investimento foi bom. Houve retorno")
        elif mediaVariacao < 0:
                print("O investimento foi ruim. Houve perda.")
        else:
                ("O investimento é estável.")