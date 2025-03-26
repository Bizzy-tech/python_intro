
x = input("Enter first number: ")
y = input("Enter second number: ")

# convert to numbers
try:
        int_x = int(x)
        int_y = int(y)
        print(int_x / int_y)
except:
    print("Invalid input")

#TODO add a function to multiply