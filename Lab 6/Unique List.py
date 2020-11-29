checklist = []
while True:
  giris = input("Input the element, write quit to quit.")
  checklist.append(giris)
  if giris == "quit":
    del checklist[-1]
    break
  
result = []

for i in checklist:
  if not i in result:
    result.append(i)


print(result)
