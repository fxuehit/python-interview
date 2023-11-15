#nested function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

#passing function to variable
hello = hello_function()
print(hello())

#access scope
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")


# example of decorator
def say_hi():
    return 'hello there'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

decorate = uppercase_decorator(say_hi)
print(decorate())

@uppercase_decorator
def say_hi2():
    return 'hello there'

print(say_hi2())

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi3():
    return 'hello there'

print(say_hi3())