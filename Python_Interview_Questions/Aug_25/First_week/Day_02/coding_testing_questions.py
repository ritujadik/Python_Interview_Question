def greet(func):
    def wrapper():
        print("Hello")
        return func()
    return wrapper


@greet
def message():
    return "How are you"


print(message())