sqrsNumber = int(input("Insira uma quantidade de espaços para o tabuleiro: "))
lNum = 0

if sqrsNumber > 0 :

  for l in range(sqrsNumber):

    line = ""
    lNum += 1

    if lNum % 2 == 0:

      for p in range(sqrsNumber):

        if (p % 2 == 0):
          line += "x"

        else:
          line += "o"
      
    else:

      for p in range(sqrsNumber):

        if (p % 2 == 0):
          line += "o"

        else:
          line += "x"

    print(line)

elif sqrsNumber == 0:
  print("O Número precisa ser maior que Zero.")

else:
  print("Precisa ser um Número a partir de 1.")


