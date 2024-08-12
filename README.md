# Factorial Calculator in Python

## Description
This Python script calculates the factorial of a given number. The factorial of a number `n` is the product of all positive integers less than or equal to `n`. For instance, the factorial of 5 (written as `5!`) is `5 * 4 * 3 * 2 * 1`, which equals 120.

## Overview
1. The script defines a function `factorial(end)` that computes the factorial of a number `end`.
2. The function initializes a variable `product` to 1.
3. It then loops through each number from 1 to `end` (inclusive), multiplying `product` by each number in this range.
4. The final value of `product` is the factorial of `end` and is returned by the function.
5. The script prompts the user to enter a number, calls the `factorial` function with this number, and prints the result.

## Output
- **After running the script, you will see:**
    - The factorial of the entered number displayed in the console.

## Code
```python
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
```

## Example
```plaintext
Enter Number you want its Factorial: 5
120
```

## Key
- [Description](#description)
- [Overview](#overview)
- [Output](#output)
- [Code](#code)
- [Example](#example)