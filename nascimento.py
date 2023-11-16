anoInicial = 1922
anoAtual = 2023
anoIncorreto = True

nomeCompleto = input("Digite seu nome completo: ")
while anoIncorreto:
  print("Digite seu ano de nascimento: ")
  try:
    anoNascimento = int(input())
    if(anoNascimento >= anoInicial) and (anoNascimento <= anoAtual):
      idadeAtual = anoAtual - anoNascimento
      print(f"{nomeCompleto}, sua idade atual é: {idadeAtual} anos.")
      anoIncorreto = False
    else:
      print(f"O ano de nascimento precisa estar entre {anoInicial} e {anoAtual}.")
  except:
    print("Valor inválido !")
