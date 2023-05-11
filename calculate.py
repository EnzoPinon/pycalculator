# Expected Output: Simple interface, calculator. Correct usage of exception handling and the raise method.


#define function to catch strings. 
def selection_check(selection):
    try:
        operation = int(selection)
        return(operation)
    except ValueError:
        operation = 'null'
        return(operation)

#define function to validate the inputted numbers.
def number_validator(num1, num2):
    #validate first number
    try:
        first = int(num1)
    except:
        first = 'not_valid'
    #validate second number
    try:
        second = int(num2)
    except:
        second = 'not_valid'
    return(first, second)


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
        print(" \ninvalid input. Please try again.")
    
    if not operation is 'null':
        if operation > 5 or operation < 1:
            print(" \nThe number is out of range. Please try again.")
    
    if not operation is 'null' and operation is 5:
        print(" \nGoodbye! Closing the application.")
        stop_counter = True
    
    if not operation is 'null' and operation is 1:
        print(" \nYou have selected **Addition!**")
        num1 = input("Please input first number: ")
        num2 = input("please input second number: ")
        first, second = number_validator(num1, num2)

        #collect results from validation system
        if first is 'not_valid' or second is 'not_valid':
            print(" \nOne of the inputs are not a valid integer. Returning to main screen.")
        
        print(" \ninputs are validated! Calculating...")
        #finally, we can add.
        add_sum = first + second

        #print results
        print("==============================")
        print("Your first number is: ", first)
        print("Your second number is: ", second)
        print("Their sum is: ", add_sum)
        print("==============================")
        print(" \nCalculation complete! Thank you for using py-calc!")
    
    if not operation is 'null' and operation is 2:
        print(" \nYou have selected **Subtraction!**")
        num1 = input("Please input first number: ")
        num2 = input("please input second number: ")
        first, second = number_validator(num1, num2)

        #collect results from validation system
        if first is 'not_valid' or second is 'not_valid':
            print(" \nOne of the inputs are not a valid integer. Returning to main screen.")
        
        print(" \ninputs are validated! Calculating...")
        #finally, we can add.
        deduct_difference = first - second

        #print results
        print("==============================")
        print("Your first number is: ", first)
        print("Your second number is: ", second)
        print("Their difference is: ", deduct_difference)
        print("==============================")
        print(" \nCalculation complete! Thank you for using py-calc!")

