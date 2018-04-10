students=[]
for student_number in range(25):
    new_student={'height':'175cm','weight':'65kg'}
    old_student={'height':'195cm','weight':'65kg'}
    students.append(new_student)
    students.append(old_student)

for student in students[:5]:
    if student['height'] == '175cm':
        student['height']='185cm'
        student['weight']='60kg'
    elif student['height']=='195cm':
        student['height']='200cm'
#显示前5个外星人
for student in students[0:5]:
    print(student)
print('...\n')

print('The number of students is:'+str(len(students)))
