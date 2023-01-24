A = int(input("A: "))
B = int(input("B: "))
X = int(input("x: "))
Y = int(input("y: "))

expressao = (A + (B**X) - (B**2) + ((A + B)/(X - Y)))

print(round(expressao,2))