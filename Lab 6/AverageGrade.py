grades = [[50,90,60],[15,60,75],[99,95,91]]

sum = 0
averages = []
for i in grades:
  length = len(i)
  for j in i:
    sum += j
  average = sum / length
  averages.append(average)
  sum = 0
print(averages)
