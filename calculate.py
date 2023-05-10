# Expected Output: Simple interface, calculator.


#Make a simple UI upon opening
print("==============================\nPy-Calc v1.0\n-by Lorenzo Pinon, in Python\n==============================")
print(" ")

#initialize stop counter
stop_counter = False

#start while loop
while stop_counter is False:
    print(" ")
    print("**Choices**\n(1) Addition [+]\n(2) Subtraction [-]\n(3) Multiplication [*]\n(4) Division [/]\n(5) Close the application")
    operation = int(input("Please select the number of your selection: "))