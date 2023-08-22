def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = generate_fibonacci(n - 1)
        next_element = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_element)
        return fibonacci_sequence

# Ask input of the number of Fibonacci elements from user
num_elements = int(input("Enter the number of Fibonacci sequence elements: "))

# Generate and print the Fibonacci sequence
fib_sequence = generate_fibonacci(num_elements)
print(fib_sequence)
