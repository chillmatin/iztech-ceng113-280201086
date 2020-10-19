a = 2
b = 6
c = -20

nominator1 = -b + (b**2-4*a*c)**0.5
nominator2 = -b - (b**2 - 4 * a * c)**0.5

denominator = 2*a

exp1 = nominator1 / denominator
exp2 = nominator2 / denominator

print(exp1)
print(exp2)