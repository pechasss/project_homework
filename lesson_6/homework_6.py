# ex6.1

# import string
#
# alphabet = string.ascii_letters
#
# userInput = input("Enter two letters separated by a hyphen:")
# start_letter = userInput[0]
# end_letter = userInput[2]
#
# start_index = alphabet.index(start_letter)
# end_index = alphabet.index(end_letter)
#
# result = alphabet[start_index:end_index + 1]
# print(result)

###ex6.2

# total_seconds = int(input("Enter the number of seconds (0 <= seconds < 8640000): "))
#
# SECONDS_IN_MINUTE = 60
# SECONDS_IN_HOUR = 60 * 60
# SECONDS_IN_DAY = 24 * 60 * 60
#
# days, remainder = divmod(total_seconds, SECONDS_IN_DAY)
#
# hours, remainder = divmod(remainder, SECONDS_IN_HOUR)
#
# minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)
#
# if days == 1:
#     day_word = "день"
# elif 2 <= days <= 4:
#     day_word = "дні"
# else:
#     day_word = "днів"
#
# hours = str(hours).zfill(2)
# minutes = str(minutes).zfill(2)
# seconds = str(seconds).zfill(2)
#
# print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")

# ex6.3
# number = int(input("Enter number: "))
#
# while number > 9:
#     product = 1
#
#     for digit in str(number):
#         product *= int(digit)
#     number = product
#
# print(number)
