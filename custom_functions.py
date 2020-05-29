# custom-functions/my_functions.py

# TODO: define temperature conversion function here

# TODO: define gradebook function here
def celsius_to_fahrenheit(c):
    f_temp = c*(9/5)+32
    return f_temp

def numeric_to_letter_grade(score):
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    elif score > 60:
        return "D"
    else:
        return "F"
    

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")


    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")





    print("--------------------")
    score = input("Please input a numeric letter grade:")
    #print(type(score))
    score = float(score)
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)