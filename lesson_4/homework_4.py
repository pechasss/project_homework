# lst = [0, 1, 0, 2, 3]
# number= 0
#
# for i in range(len(lst)):
#     if lst[i] != 0:
#         lst[number] = lst[i]
#         number += 1
#
# while number < len(lst):
#     lst[number] = 0
#     number += 1
#
# print(lst)



# ex2


#
# lst = []
# #
# if lst:
#     sumOfNumbers= sum(lst[i] for i in range(0, len(lst), 2))
#     result = sumOfNumbers * lst[-1]
# else:
#     result = 0
# print(result)


# ex 3
# import random
#
# n = random.randint(3, 10)
#
# random_list = [random.randint(0, 10) for _ in range(n)]
# print("First list:", random_list)
#
# newList = [random_list[0], random_list[2], random_list[-2]]
# print("New list:", newList)
