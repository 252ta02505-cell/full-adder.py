A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
Cin = int(input("Enter Carry-in (0 or 1): "))

Sum = A ^ B ^ Cin
Cout = (A & B) | (Cin & (A ^ B))

print("Sum =", Sum)
print("Carry =", Cout)
