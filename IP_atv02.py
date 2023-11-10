def calculadora(x, y, operador):
  if (operador == '+'):
    return x + y
  elif (operador == '-'):
    return x - y
  elif (operador == '/'):
    return x / y
  elif (operador == '*') or (operador == 'x'):
    return x * y
  else:
    return "Operador inválido. Apenas soma, subtração, multiplicação e divisão são suportadas."
