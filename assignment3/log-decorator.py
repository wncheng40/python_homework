'''
Task 1: Write a logging decorator called logger_decorator
'''

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...

# To write a log record:
#logger.log(logging.INFO, "this string would be logged")
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # 1. get func name
        func_name = func.__name__
        
        # 2. deal with position parameters (if no parameters, display "none")
        pos_params = list(args) if args else "none"
        
        # 3. deal with keyword parameters (if no parameters, display "none")
        kw_params = kwargs if kwargs else "none"
        
        # 4. execute original function, and store the return value
        result = func(*args, **kwargs)
        
        # 5. assemble the message format to be written to the log
        log_message = (
            f"function: {func_name}\n"
            f"positional parameters: {pos_params}\n"
            f"keyword parameters: {kw_params}\n"
            f"return: {result}\n"
        )
        
        # 6. write to ./decorator.log file
        logger.log(logging.INFO, log_message)
        
        # 7. return the original function's return value
        return result

    return wrapper
# 3. Declare a function that takes no parameters and returns nothing.
@logger_decorator
def say_hello():
    print("Hello, World!")
# 4. Declare a function that takes a variable number of positional 
# arguments and returns True. Decorate this function with your decorator.
@logger_decorator
def check_args(*args):
    return True
# 5. Declare a function that takes no positional arguments and a variable 
# number of keyword arguments, and that returns logger_decorator.  
# Decorate this function with your decorator.

@logger_decorator
def return_decorator_ref(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    print(check_args(1, "apple", 3.5))
    return_decorator_ref(name="Alice", role="student")