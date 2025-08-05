from functools import wraps

def log_field(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        gen = func(*args,**kwargs)
        for value in gen:
            print(f"yield:{value}")
            yield value
    return wrapper

@log_field
def count_up_to(n):
    for i in range(1,n+1):
        yield i

x = count_up_to(5)
for j in x:
    print("Recived value:",j)