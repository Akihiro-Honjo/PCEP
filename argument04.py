###アンパック

numbers = (1, 2, 3)
a, b, c = numbers
print(a, b, c)

student = {
    'name': 'Alice', 
    'age': 20,
    'course': 'English'
        }
print(*student) #name age course
print(*student.values()) #Alice 20 English
print(*student.items()) #('name', 'Alice') ('age', 20) ('course', 'English')


student2 = {
    'name': 'Mark', 
    'age': 22,
    'course': 'Math'
        }
def print_student2(name, age, course):
    print(f'name: {name}, age: {age}, course: {course}')
student_list =["Mark", 22, "Math"]
print_student2(*student_list)
print_student2(**student2)


student_dict = [
    {'name': 'Alice', 'age': 20, 'course': 'English'},
    {'name': 'Bob', 'age': 22, 'course': 'Math'},
    {'name': 'Charlie', 'age': 25, 'course': 'Science', 'address': 'Tokyo'}
    ]
def print_student3(name, age, course, address='Unknown'):
    print(f'name: {name}, age: {age}, course: {course}, address: {address}')
for student3 in student_dict:
    print_student3(**student3)
    

