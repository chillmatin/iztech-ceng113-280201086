num_stud = int(input('Number of students: '))
grade_list = []
for i in range(num_stud):
    midterm1 = int(input('Midterm1: '))
    midterm2 = int(input('Midterm2: '))
    final = int(input('Final : '))
    result = midterm1 * 0.3 + midterm2 * 0.3 + final * 0.4
    if result > 90.0:
        grade_list.append([midterm1, midterm2, final,result])
print(grade_list)