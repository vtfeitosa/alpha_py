
#Calcular Céulas

valor = int(input("Que valor você deseja contar? R$"))

resto = valor
ced = 200
qtCed = 0

while True: 
  if resto >= ced:
    resto -= ced
    qtCed = qtCed + 1
  else:
    if qtCed > 0:
      print("-", qtCed, "cédulas de R$", ced, ",00 reais")
      qtCed = 0

    if ced == 200:
      ced = 100
    elif ced == 100:
      ced = 50
    elif ced == 50:
      ced = 20
    elif ced ==20:
      ced = 10
    elif ced == 10:
      ced = 5
    elif ced == 5:
      ced = 2
    elif ced == 2:
      ced = 1
    elif ced == 1:
      ced = 0

    if resto == 0:
      break

