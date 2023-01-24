# Volume do Paralelepípedo

A = float(input("Lado A: "))
B = float(input("Lado B: "))
C = float(input("Lado C: "))

volume = A*B*C
d = (A**2)+(B**2)+(C**2)

print("Volume: ", round(volume,2))
print("Diagonal Principal: ", round(d,2))