# Lista de Números
# O programa deve informar se há números repetidos na lista, e se sim, mostrar a posição deles

nNumbers = int(input("Digite a quantidade de números para adicionar à lista: "))
numbersList = []

for i in range(0,nNumbers):
  number = int(input("Digite um número: "))
  numbersList.append(number)

for i in range(len(numbersList)-1):
  if numbersList[i] == numbersList[i+1]:
    print(f'Pos {i-1} e {i}')