# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
#
# print(say_hi("Alex", 32))
# print(say_hi("Frank", 68))
#
# print('ОК')

##### 7.2
# def correct_sentence(text):
#     text = text[0].upper() + text[1:]
#
#     if not text.endswith('.'):
#         text += '.'
#
#     return text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
#
# print('ОК')

###### 7.3
# def second_index(text, some_str):
#
#     first_index = text.find(some_str)
#
#     if first_index == -1:
#         return None
#
#     second_index = text.find(some_str, first_index + 1)
#
#     return second_index if second_index != -1 else None
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
#
# print('ОК')

### 7.4

# def common_elements():
#
#     multiplesOf3 = {num for num in range(100) if num % 3 == 0}
#
#     multiplesOf5 = {num for num in range(100) if num % 5 == 0}
#
#     intersection = multiplesOf3 & multiplesOf5
#
#     return intersection
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test failed'
# print('ОК')



