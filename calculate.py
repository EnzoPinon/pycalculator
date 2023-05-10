# Expected Output: Simple interface, calculator. Correct usage of exception handling and the raise method.


#Make a simple UI upon opening
print("==============================\nPy-Calc v1.0\n-by Lorenzo Pinon, in Python\n==============================")
print(" ")

#initialize stop counter
stop_counter = False

#start while loop
while stop_counter is False:
    print(" ")
    print("**Choices**\n(1) Addition [+]\n(2) Subtraction [-]\n(3) Multiplication [*]\n(4) Division [/]\n(5) Close the application")
    try:
        operation = int(input("Please select the number of your selection: "))
    except:
        raise TypeError("The input is not an integer, but a string. Please restart the app.")        
    #check if int is within the range
    if operation < 1 or operation > 5:
        raise ValueError("This number is either greater than 5, or less than 1. Please restart the app.")