def count_up_to(max):
    count = 0
    while count <= max:
        yield count
        count += 1

my_generator = count_up_to(5)
print(next(my_generator)) #0
print(next(my_generator)) #1
print(next(my_generator)) #2
print(next(my_generator)) #3
print(next(my_generator)) #4
print(next(my_generator)) #5
# print(next(my_generator)) #StopIteration

# for number in my_generator:
#     print(number)

import random
import sys

def unique_random_gen(num):
    randoms = set()
    while len(randoms) < num:
        rand_num = random.randint(1, sys.maxsize)
        if rand_num not in randoms:
            randoms.add(rand_num)
            yield rand_num

num_length = 100_000

my_nums = unique_random_gen(num_length)
print(sys.getsizeof(my_nums)) 

my_nums = list(unique_random_gen(num_length))
print(sys.getsizeof(my_nums))

