# Write your code here.
# ========================= # Task 1: Hello World ====================
def hello():
    return "Hello!"

print(hello())
# ========================= # Task 2: Greet with a Formatted String ===========================
def greet(name):
    return f"Hello, {name}!"

print(greet("Zoe"))
# ========================= # Task 3: Calculate - Basic Arithmetic ===========================
def calc(a,b,operator ="multiply"):
    try:
        match operator:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "power":
                return a ** b
            case "int_divide":
                return a // b
            case _:  
                return None  
    #error handling for division by zero
    except ZeroDivisionError:
        return "You can't divide by 0!"
    #error handling for type errors
    except TypeError:
        return "You can't multiply those values!"

print(calc(10, 2, "add"))
print(calc(10, 2, "subtract"))
print(calc(10, 2, "multiply"))
print(calc(10, 2, "divide"))
print(calc(10, 2, "modulo"))
print(calc(10, 2, "power"))  
print(calc(10, 0, "divide"))
print(calc("hello", "world", "subtract"))

# ========================= # Task 4: Data Type Conversion ===========================
def data_type_conversion(value, type_name):
    try:
        match type_name:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return None
    except ValueError:
        return f"You can't convert {value} into a {type_name}."

print(data_type_conversion("110", "float"))
print(data_type_conversion(7,"float"))
print(data_type_conversion(91.1,"str"))
print(data_type_conversion("banana", "int"))

# ========================= # Task 5: Grading ===========================
def grade(*args):
    try:
        avg = sum(args) / len(args)
    
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return None
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

print(grade(75,85,95))

# ========================= # Task 6: Use a For Loop with a Range ===========================
def repeat(value, times):
    result = ""
    for i in range(times):
        result += value
    return result

print(repeat("up", 4))

# ========================= # Task 7: Student Scores, Using **kwargs ===========================
def student_scores(positional, **kwargs):
    if positional == "mean":
        #get average grade
        return sum(kwargs.values()) / len(kwargs)
    elif positional == "best":
        #get the student with the best grade
        max_grade = max(kwargs.values())
        for key, value in kwargs.items():
            if value == max_grade:
                return key


print(student_scores("best", Alice=90, Bob=95, Charlie=80))
print(student_scores("mean", Alice=90, Bob=95, Charlie=85))   
    
# ========================= # Task 8: Titleize ===========================
def titleize(sentence):
    words = sentence.split()
    if not words:
        return ""
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    result = []
    for i, word in enumerate(words):
       if i == 0 or word == words[-1] or word not in little_words:
        result.append(word.capitalize())
       else:
        result.append(word.lower())
    return " ".join(result)

print(titleize("war and peace"))
print(titleize("a separate peace"))
print(titleize("after on"))
print(titleize("the quick brown fox"))

#===========================# Task 9: Hangman with more String Operations===========================
def hangman(secret, guesses):
    result = ""
    for char in secret:
        if char in guesses:
            result += char
        else:
            result += "_"
    return result

print(hangman("difficulty", "ic"))
            

#===========================# Task 10: Pig Latin===========================
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []
    for word in words:
        #(1): if a word starts with a vowel
        if word[0] in vowels:
            result.append(word + "ay")
        #(3): "qu" is a special case, as both of them get moved to 
        # the end of the word, as if they were one consonant letter.
        elif "qu" in word:
            qu_position = word.find("qu") + 2
            result.append(word[qu_position:] + word[:qu_position] + "ay")
        #(2): If the string starts with one or several consonants, 
        # they are moved to the end and "ay" is tacked on after them
        else:
            i = 0 # start with 0 index (first letter)
            #keep going until find a vowel
            while i < len(word) and word[i] not in vowels:
                i += 1
            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)
            
print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))
    
