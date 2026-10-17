
CONTRIBUTORS = ["Jovany", "Michel", "Student C", "Student D"] # Conflicts generator 1

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print(add(2, 2)) # Conflicts generator 2
    print(subtract(10, 2))
    print(multiply(10, 2))
    print(divide(10, 2))
