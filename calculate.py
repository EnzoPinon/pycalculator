# Expected Output: Simple interface, calculator. Correct usage of exception handling and the raise method.


#define number checking for selection
def selection_check(selection):
    try:
        operation = int(selection)
        return(operation)
    except ValueError:
        operation = 'null'
        return(operation)
#Make a simple UI upon opening
print("==============================\nPy-Calc v1.0\n-by Lorenzo Pinon, in Python\n==============================")
print(" ")

#initialize stop counter
stop_counter = False

#start while loop
while not stop_counter:
    print(" ")
    print("**Choices**\n(1) Addition [+]\n(2) Subtraction [-]\n(3) Multiplication [*]\n(4) Division [/]\n(5) Close the application")
    selection = input("Please type the number of your selection: ")
    operation = selection_check(selection)

    if operation is 'null':
        print("invalid input. Please try again.")
    
    if not operation is 'null':
        if operation > 5 or operation < 1:
            print("The number is out of range. Please try again.")