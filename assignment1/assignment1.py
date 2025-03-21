# Task 1
def hello():
    return "Hello!"
print(hello())

# Task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Scarlett"))

# Task 3

def calc(a, b, task="multiply"):
    try:
        if task == "subtract":
            return a - b
        elif task == "add":
            return a + b
        elif task == "multiply":
            return a * b
        elif task == "divide":
            return a / b
        elif task == "modulo":
            return a % b
        elif task == "int_divide":
            return a // b
        elif task == "power":
            return a ** b
        else:
            return "error"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
print(calc(5,6,))

# Task 4
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
print(data_type_conversion("123", "int"))

# Task 5
def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        elif average < 60:
            return "F"
    except TypeError:
        return  "Invalid data was provided."
    
    print(grade(75, 85, 95))
    print(grade("three", "blind", "mice"))

# Task 6
def repeat(string, count):
    res = ''
    for i in range(count):
        res += string
    return res
    print(repeat("up,", 4))

# Task 7
def student_scores(position="best", **kwargs):
    if position == "best":
        max = 0
        students = ""
        for key, value in kwargs.items():
            if value > max:
                students = key
                max = value
        return students
    else:
        sum = 0
        for key, value in kwargs.items():
            sum += value
        average = int(sum/len(kwargs))
        return average
print(student_scores( Tom=75, Dick=89, Angela=91, Frank=50 ))

# Task 8
def titleize(string):
    exception_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = string.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in exception_words:
            words[i] = word.capitalize()
    return " ".join(words)
print(titleize('goga magoga'))

# Task 9
def hangman(secret, guess):
    res = []
    for i in secret:
        if i in guess:
            res.append(i)
        else:
            res.append("_")
    return "".join(res)

print(hangman("difficulty","ic"))

# Task 10

def pig_latin(string):
    vowels = "aeiou"
    res = []
    new_string = string.split()
    for i in new_string:
        if i[0] in vowels:
            i = i+ 'ay'
        elif i[0]=="q" and i[1]=="u":
            i= i[2:]+"quay"
        elif i[0] not in vowels and i[1]=="q" and i[2]=="u":
            i=i[3:]+i[0]+i[1]+i[2]+"ay"
        elif i[0] and i[1] not in vowels:
            i=i[2:]+i[0]+i[1]+"ay"     
        else:
            i=i[1:]+i[0]+"ay"
        res.append(i)    
    return " ".join(res)
print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))