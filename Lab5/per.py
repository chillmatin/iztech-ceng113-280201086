howmany = int(input("How many numbers?"))
even = 0
for _ in range(0, howmany):
  number = int(input("Enter an integer: "))
  if number % 4 ==0:
    even += 1

percentage = even / howmany * 100

print(percentage, "%")