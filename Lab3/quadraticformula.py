from math import sqrt

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = b**2 - 4 * a * c
denominator = 2*a #will be used
if d < 0:
  print('no real roots')

elif d == 0:
  x1 = (-b) / denominator
  print("x1 =", x1)

else:
  x1_nominator = -b + sqrt(d)
  x2_nominator = -b - sqrt(d)

  x1 = x1_nominator / denominator
  x2 = x2_nominator / denominator
  
  print("x1 =",x1)
  print("x2 =",x2)

  

  