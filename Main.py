from Correlacao import grafico_correlacao
from Variacao_percentual import variacao_pct

while True:
      print("Escolha uma operação abaixo:\n")
      print("(1) Correlação com gráfico.\n" +
            "(2) Variação percentual, exportada em uma planilha.\n" +
            "(3) Parar programa.\n")
      operacao = input("Escolha uma das opções acima: ")

      if operacao == '1':
            grafico_correlacao()
      elif operacao == '2':
            variacao_pct()
      elif operacao == '3':
            exit()
      else:
            print("Opção inválida. Tente novamente!")