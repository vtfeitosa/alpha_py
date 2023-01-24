#Desconto do Imposto de Renda

valorHora = int(input("Valor da Hora de Trabalho: "))
horasTrabalhadas = int(input("Horas Trabalhas: "))

salarioB = valorHora*horasTrabalhadas
print("Salário Bruto: ", salarioB)

if salarioB <= 900:
  imposto = 0

elif (salarioB > 900) and (salarioB <= 1500):
  imposto = 5

elif (salarioB > 1500) and (salarioB <= 2500):
  imposto = 10

elif salarioB > 2500:
  imposto = 20

valorIR = (imposto*salarioB)/100
print("Desconto do Imposto de Renda: ", valorIR)

Inss = (10*salarioB)/100
print("INSS: ", Inss)

Fgts = (11*salarioB)/100
print("FGTS: ", Fgts)

D = alorIR + Inss
print("Descontos Totais: ", D)

salarioL = salarioB - D
print("Salário Líquido: ", salarioL)