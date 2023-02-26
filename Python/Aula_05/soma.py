while True:

  N = int(input("Digite um número par: "))

  if N % 2 == 0:
    break
  
  else:
    print("O número inserido é impar, não podemos continuar :(")
    
nList = []

for i in range(N):
  number = int(input("Digite um número: "))
  nList.append(number)

print(nList)

sumList = []

for i in range(int(N/2)):
  sumList.append(nList[i] + nList[N-i-1])

print(sumList)