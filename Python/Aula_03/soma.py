# Soma de "x" números

TN = int(input("Insira um Total de Números para soma: "))
S = 0

if TN > 0:
  for i in range(TN):
    N = float(input("Insira um Número: "))
    S = N + S
    
elif TN == 0:
  print("O Número precisa ser maior que Zero.")

else:
  print("Precisa ser um Número a partir de 1.")


print("Total da soma de ", TN , "números é: ", "%.2f" %S )