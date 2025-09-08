# import time
#
# def log_function_call(func):
#     def wrapper(*args):
#         print(f"[LOG] calling function:{func.__name__}")
#         print(f"[LOG] Arguments:{args}")
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         print(f"[LOG] Function {func.__name__} completed in {end-start:.4f}seconds")
#         return result
#     return wrapper
#
#
# @log_function_call
# def fetch_user_data(user_id,name):
#     time.sleep(1)
#     return {"id":user_id,"name":name}
#
# # @log_function_call
# # def process_payment(amount,method="card"):
# #     time.sleep(0.5)
# #     return f"Processed ${amount} via {method}"
#
# fetch_user_data(42,"ritu")
#
# # process_payment(100,method="UPI")

def generate_table(x):
    for i in range(1,11):
        yield x*i


gen = generate_table(4)
print(next(gen))
print(next(gen))
