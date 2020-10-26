GPA = float(input("GPA: "))
lectures = int(input("Lectures: "))

if GPA < 2.0:
    if lectures < 47:
        print("Not enough number of lectures and GPA!")
    if lectures >= 47:
        print("Not enough GPA!")

elif GPA >= 2.0:
    if lectures < 47:
        print("Not enough number of lectures!")
    if lectures >= 47:
        print("GRADUATED!")