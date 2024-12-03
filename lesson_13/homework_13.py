# class Human:
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'
#
# class Student(Human):
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return f'Student: {self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record Book: {self.record_book}'
#
# class Group:
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.group.add(student)
#
#     def delete_student(self, last_name):
#         student_to_remove = self.find_student(last_name)
#         if student_to_remove:
#             self.group.remove(student_to_remove)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = '\n'.join(str(student) for student in self.group)
#         return f'Group Number: {self.number}\nStudents:\n{all_students}'
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
#
# gr.add_student(st1)
# gr.add_student(st2)
#
# print(gr)
#
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'
#
# gr.delete_student('Taylor')
# print(gr)
#
# gr.delete_student('Taylor')

####ex2
# class Counter:
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_current(self, start):
#         if start < self.min_value or start > self.max_value:
#             raise ValueError("The initial value is out of the minimum or maximum bounds.")
#         self.current = start
#
#     def set_max(self, max_max):
#         if max_max < self.min_value:
#             raise ValueError("The maximum value cannot be less than the minimum value.")
#         self.max_value = max_max
#         if self.current > self.max_value:
#             self.current = self.max_value
#
#     def set_min(self, min_min):
#         if min_min > self.max_value:
#             raise ValueError("The minimum value cannot be greater than the maximum value.")
#         self.min_value = min_min
#         if self.current < self.min_value:
#             self.current = self.min_value
#
#     def step_up(self):
#         if self.current < self.max_value:
#             self.current += 1
#         else:
#             raise ValueError("Maximum reached")
#
#     def step_down(self):
#         if self.current > self.min_value:
#             self.current -= 1
#         else:
#             raise ValueError("Minimum reached")
#
#     def get_current(self):
#         return self.current
#
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# assert counter.get_current() == 10, 'Test1'
#
# try:
#     counter.step_up()  # ValueError
# except ValueError as e:
#     print(e)
#
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
#
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e)
#
# assert counter.get_current() == 7, 'Test4'

