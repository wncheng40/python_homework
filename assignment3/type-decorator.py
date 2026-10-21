# 1. define a decorator factory that takes a type as an argument
def type_converter(type_of_output):
    # 2. define the actual decorator
    def decorator(func):
        # 3. define the wrapper function
        def wrapper(*args, **kwargs):
            # execute original function and get result
            x = func(*args, **kwargs)
            # convert the result to the specified type and return it
            return type_of_output(x)
        return wrapper
    # return the decorator
    return decorator

# 2. declare the first function: return an integer 5, but convert to str through the decorator
@type_converter(str)
def return_int():
    return 5

# 3. declare the second function: return a string, but try to convert to int through the decorator
@type_converter(int)
def return_string():
    return "not a number"  

if __name__ == "__main__":
    # test 1: verify that the return type of return_int() is a string "str"
    y = return_int()
    print(type(y).__name__)  # should print "str"

    # test 2: verify that return_string() raises a ValueError when converting to int
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # this is the expected thing to happen