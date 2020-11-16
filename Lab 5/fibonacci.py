howmany = int(input("How many numbers in fibonacci gardash: "))

a = 1
b = 1
fi = []

for i in range(howmany):
  fi.append(a)
  ex = b
  b = a + b
  a = ex
  
print(fi)