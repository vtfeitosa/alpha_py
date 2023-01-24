#Comissão do Vendedor

vendedor = input("Vendedor: ")
SF = int(input("Salário Fixo: "))
V = int(input("Valor Total de Vendas: "))

comissao = (5*V)/100

total = comissao + SF

print("Comissão: " , round(comissao,2))
print("Total a receber: " , total)
