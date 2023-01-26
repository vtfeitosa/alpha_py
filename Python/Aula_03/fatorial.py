# Verificação se "numberInput" é fatorial ou não

import math

numberInput = int(input("Insira um Número Inteiro: "))
resultsList = []

if numberInput > 0 :

  for n in range(numberInput + 1):

    if numberInput == math.factorial(n+1):
      resultsList.append(True)

    elif numberInput != math.factorial(n+1):
      resultsList.append(False)

  if True in resultsList:
    print("True")

  else:
    print("False")

elif numberInput == 0:
  print("O Número precisa ser maior que Zero.")

else:
  print("Precisa ser um Número a partir de 1.")