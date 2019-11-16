# Check for enrolledstudent
list_of_enrolled_students = ['michael', 'peter', 'zara', 'alison']
new = input('enter a name :')

if new in list_of_enrolled_students:
    print('student already enrolled')
else:
    print(f'Student {new} is waiting to enroll')
