numbers = [1]
if len(numbers) >1:
    numbers.insert(0, numbers[-1])
    numbers.pop()
print(numbers)