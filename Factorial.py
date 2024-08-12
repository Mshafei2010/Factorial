def factorial(end):
    # Initialize product to 1, since we are multiplying
    product = 1
    
    # Loop through each number from 1 to 'end' (inclusive)
    for number in range(1, end + 1):
        # Multiply the current product by the current number
        product *= number
    
    # Return the final product which is the factorial of 'end'
    return product

# Prompt the user to input the number for which they want to calculate the factorial
end = int(input("Enter Number you want its Factorial:"))

# Call the factorial function with the user's input and store the result
result = factorial(end)

# Print the calculated factorial
print(result)
