nList = []

N = 0

while True:
  N = int(input("Digite uma quantidade de números a serem listados: "))

  if N <= 0:
    print("O número inserido deve ser positivo.")

  if N % 2 == 0:
    break
  
  else:
    print("O número inserido é impar, não podemos continuar :(")

for i in range(N):
  nList.append(int(input("Insira um número: ")))

print(nList)