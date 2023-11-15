def calculadora_idade():
  nome = input("Digite o nome completo:")
  ano_de_nascimento = input("Digite o ano de nascimento:")

  try:
    ano_de_nascimento = int(ano_de_nascimento)
    if ano_de_nascimento < 1922 or ano_de_nascimento > 2023:
      raise Exception("Digite um ano de nascimento válido entre 1922 e 2023.")
    else:
      idade = 2023 - ano_de_nascimento      
      print(f"Nome completo: {nome}")
      print(f"Idade: {idade}")
  except:
    print("Digite um ano de nascimento válido entre 1922 e 2023.")

calculadora_idade()
