# Calculate the multiplication and sum of two numbers

def calculate(number1, number2):
    # Calculate the product of two numbers
    product = number1 * number2
    # Check if the product is less than 1000
    if product < 1000:
        return product
    else:
        return number1 + number2

# Given 1
number1 = 20
number2 = 30
result = calculate(number1, number2)
print(f"The result is {result}")
    
# Given 2
number1 = 40
number2 = 30