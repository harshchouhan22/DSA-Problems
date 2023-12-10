import time

def function_progress(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} function, started executing")
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} function execution completed!")
        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} function execution time: {duration:.2f} seconds")
        return result
    return wrapper

@function_progress
def addition(a, b):
    #adding sleep function just to see time taken by this function in execution
    time.sleep(2)
    result = a + b
    return result

#Run Function
addition(8, 5)
