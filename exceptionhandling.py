try:
    
    num1 = 10
    num2 = 0
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    # Example 2: Index out of bounds
    my_list = [1, 2, 3]
    print("Element at index 3:", my_list[3])

except IndexError:
    print("Error: Index out of bound.")

try:
    # Example 3: Invalid value Error
    value = int("abc")
    print("Value:", value)

except ValueError:
    print("Error: Invalid value.")

