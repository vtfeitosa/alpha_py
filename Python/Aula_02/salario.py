#Organizações Tabajara - Reajuste Salarial

S = int(input("Salário: "))

print("Salário sem Reajuste:" , S)

if S <= 280:
  bonus = 20

elif (S > 280) and (S <=700):
  bonus = 15

elif (S > 700) and (S <=1500):
  bonus = 10

else:
  bonus = 5

extra = (bonus*S)/100
newS = S + extra

print("O bonus do salário é de ", bonus, "%")
print("O aumento será de ", round(extra), "reais")
print("Salário com Reajuste: ", newS)
