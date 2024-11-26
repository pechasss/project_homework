# def prime_generator(end):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     for n in range(2, end + 1):
#         if is_prime(n):
#             yield n
#
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')

###11.2

# def generate_cube_numbers(end):
#     n = 2
#     while True:
#         cube = n**3
#         if cube > end:
#             return
#         yield cube
#         n += 1
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
#
# print('Ok')

###11.3

# def is_even(number):
#     return (number & 1) == 0
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
#
# print('Ok')

