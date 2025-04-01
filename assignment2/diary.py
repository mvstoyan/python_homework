import traceback

#Task 1
try:
    with open('diary.txt', 'a') as file:
        diary = file.write(input("What happened today?")+"\n")
        res = ''
        while diary:
            if res!= "done for now":
                res = input("What else? ")
                diary = file.write(res +"\n")
            elif res == "done for now":
                break
except Exception as e:
    trace_back = traceback.extract_tb(e.traceback)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).name}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
print(res)



