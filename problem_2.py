# Probem 2 of Project Euler
# Python 3.9.5
# Even Fibonacci numbers

# Create Fibonacci list and even Fibonacci list
fib_list = []

even_fib_list = []

# Create Fibonacci sequence

def fibonacci(n):
    a, b = 0, 1
    for x in range(1, n):
        a, b = b, a + b
    return b

for i in range(1, 34):
    fib_list.append(fibonacci(i))


# Print Fibonacci seq no more than 4,000,000
print(fib_list)

# Get the even values from fib_list and add it it into the even list
for value in fib_list:
    if value % 2 == 0:
        even_fib_list.append(value)
    else:
        None

print("Updated list", even_fib_list)

# Add values from even_fib_list together
print(sum(even_fib_list))
