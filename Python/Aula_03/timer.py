# Timer

import time

tInput = int(input("Insira um tempo em segundos para iniciar o timer: "))
interval = 0
tSobra = tInput

if tInput > 0:

  while tSobra <= tInput:

    print("Tempo restante: ", tSobra, " segundos." )

    interval += 2
    time.sleep(interval)
    tSobra -= interval

    if tSobra <= 0:
      print("Tempo Acabou!")
      break
  

elif tInput == 0:
  print("O Número precisa ser maior que Zero.")

else:
  print("Precisa ser um Número a partir de 1.")

