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
    

###仮引数のアンパック
def sum_func(*args):
    print(args*2)
    total = sum(args*2)
    return total

nums = [1, 2, 3, 4, 5]
multi = sum_func(*nums)
print(multi)

def print_menu(**kwargs):
    for dish, price in kwargs.items():
        print(f'{dish}: {price} yen')

#print_menu(ramen=800, curry=900, pasta=1000)

menu = {
    'ramen': 800,
    'curry': 900,
    'pasta': 1000
    }
print_menu(**menu)


def create_profile(**kwargs):
    print(kwargs)
    # profile = {}
    # for key, value in kwargs.items():
    #     profile[key] = value
    # return profile
    return kwargs

my_profile = create_profile(name='suzuki', email='test@test.com',age=20)

def foo(first_arg, second_arg, *args, **kwargs):
    print(first_arg)
    print(second_arg)
    print(args)
    print(kwargs)

# foo("first", "second", 1,2,3, a="apple", b="banana", c="cherry")
my_tuple = (10, 20, 30, 40)
my_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
foo("first", "second", *my_tuple, **my_dict)

