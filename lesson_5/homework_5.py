
# ex5.2
# while True:
#     n1 = int(input("Enter first number: "))
#     action = input("Enter action (+, -, *, /): ")
#     n2 = int(input("Enter second number: "))
#
#     if action == "+":
#         print("Result:", n1 + n2)
#     elif action == "-":
#         print("Result:", n1 - n2)
#     elif action == "*":
#         print("Result:", n1 * n2)
#     elif action == "/":
#         if n2 != 0:
#             print("Result:", n1 / n2)
#         else:
#             print("Error: impossible to solve (division by zero)")
#     else:
#         print("Enter correct action")
#
#
#     cont = input("Do you want to continue? (y/n): ").lower()
#     if cont != "y":
#         print("Calculator off.")
#         break




# ex5.3
# import string
#
# def create_hashtag(text):
#
#     clean_text = ''.join(char for char in text if char not in string.punctuation)
#     words = clean_text.split()
#     hashtag = '#' + ''.join(word.capitalize() for word in words)
#
#     if len(hashtag) > 140:
#         return hashtag[:140]
#     return hashtag
# user_word= input("Enter your word: ")
# print(create_hashtag(user_word))



# ex5.1
# import string
# import keyword
#
#
# def valid_name(name):
#
#     if name in keyword.kwlist:
#         return False
#
#     if name[0].isdigit():
#         return False
#
#     if any(char.isupper() for char in name):
#         return False
#
#     invalid_chars = set(string.punctuation) - {"_"}
#     if any(char in invalid_chars for char in name):
#         return False
#
#     if name.count("_") > 1:
#         return False
#
#     return True
# user_name= input("Enter name:")
# print(valid_name(user_name))


