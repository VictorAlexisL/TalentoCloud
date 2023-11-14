def calculadora():
  operacao = '1'

  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")
  print("0: Sair")

  while operacao != '0':
    operacao = input("Digite a operação:")

    if operacao == '0':
      break

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    if operacao == '1':
      result = num1 + num2
    elif operacao == '2':
      result = num1 - num2
    elif operacao == '3':
      result = num1 * num2
    elif operacao == '4':
      if num2 != 0:
        result = num1 / num2
      else:
        print("Erro: divisão por zero")
        continue

    print("Resultado:", result)

calculadora()
