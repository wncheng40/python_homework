from numpy import true_divide
import traceback


try:
    #open diary.txt
    with open("diary.txt", "a") as f:
        prompt = "What happened today?"
        while True:
            #get user input
            user_input = input(prompt)
            #check user input if "done for now"
            if user_input == "done for now":
                break
            #write user input to diary.txt
            f.write(user_input + "\n")
            prompt = "What else?"

    pass

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")