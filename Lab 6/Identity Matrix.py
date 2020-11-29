n = int(input("Matrix number: "))
string = ''
column = []
line = []
string = ''
for i in range(n):
    for j in range(n):
        if i == j:
            string = string + " 1"
        else:
            string = string + " 0"
        if j == n - 1:
            string = string + "\n"

print(string)
