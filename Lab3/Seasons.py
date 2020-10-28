#THIS PROGRAM ASSUMES THAT ALL REQUESTED INPUTS ARE TRUE AND VALID. 

month = input("Month (all letters should be LOWERCASE): ")
day = int(input("Day (input should be integer value): "))

spring = (month == "march" and day >= 20) or (month == "april") or (month == "may") or (month == "june" and day < 21)  #this will be true if the input shows a date in spring

summer = (not spring) and ((month == "june") or (month == "july") or (month == "august") or (month == "september" and day < 22))

fall = not (summer or spring) and   ((month == "september") or (month == "october") or (month == "november") or (month == "december" and day < 21))

winter = not (spring or summer or fall)

if spring:
  print("Spring")

elif summer:
  print("Summer")

elif fall:
  print("fall")

elif winter:
  print("winter")

else:
  print("unexpected error.")
