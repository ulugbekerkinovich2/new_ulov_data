# function to calculate EKUB
def calculate_ekub(a, b):
    while b != 0:
        a, b = b, a % b
        print(a)
        print(b)
    return a


# function to calculate EKUK
def calculate_ekuk(a, b):
    return (a * b) // calculate_ekub(a, b)


# get user input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# calculate EKUK and EKUB
ekuk = calculate_ekuk(a, b)
ekub = calculate_ekub(a, b)

# print the results
print(f"EKUK of {a} and {b} is: {ekuk}")
print(f"EKUB of {a} and {b} is: {ekub}")
