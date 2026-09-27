# is_login = True

# def check_login(func):
#     def inner(name):
#         if is_login == True:
#             res = func(name.capitalize())
#             return res
#         else:
#             return "Please login!"
#     return inner


# @check_login
# def hello(name):
#     return f"Hello {name}"

# print(hello("akbar"))


# generator = lambda start, end: [i for i in range (start, end+1) if i % 2 == 0]

# print(generator(1, 1000000))



# def welcome(func):
#     def inner(name):
#         print ("Welcome!")
#         return func(name)
#     return inner

# @welcome
# def show_name(name):
#     print(name)

# print(show_name("Ali"))

# test 2

# def goodby(func):
#     def inner(*args, **kwargs):
#         print ("Goodbye!")
#         return func(*args, **kwargs)
#     return inner

# @goodby
# def show_city(city):
#     return city

# print(show_city("Dushanbe"))



# test 3

# def repeat_three_times(repeat):
#     def inner1(func):
#         def inner(*args, **kwargs):
#             for i in range(repeat):
#                 func(*args, **kwargs)
#         return inner
#     return inner1

# @repeat_three_times(3)
# def hello():
#     print("Hello")

# hello()


# test 4

# def show_func_name(func):
#     def inner(*args, **kwargs):
#         print (f"Function: {func.__name__}")
#         return func (*args, **kwargs)
#     return inner

# @show_func_name
# def add(a, b):
#     return a + b

# a = int(input())
# b = int(input())

# print(add(a, b))



# test 5
# def uppercase_result(func):
#     def inner(name):
#         return func(name.upper())
#     return inner

# @uppercase_result
# def get_name(name):
#     return name

# print(get_name("Ali"))


# test 6
# def positive_number(func):
#     def inner(num):
#         if num > 0:
#             return func(num**2)
#         else:
#             print("The number must be positive")
#     return inner


# @positive_number
# def square(number):
#     return number

# print(square(-7))


# test 7

# add = lambda a, b: a + b

# print(add(7, 5))


# test 8

# square = lambda num: num**2

# print(square(6))



# test 9

# filter = lambda start, end: [i for i in range (start, end+1) if i % 2 == 0]


# print(filter(1, 6))


# test 10

people = [('Ali', 22), ('Sara', 19), ('Bob', 25)]

people = sorted(people, key=lambda x:x[1])
print(people)
