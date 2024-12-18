# Defining a function
def greet(name):
    print(f"Hello, {name}!")
greet("World")   

# function parameters

def calculate_area(length,width):
    area=length*width
    print(area)
calculate_area(10,20)     


# Returning Values

def add_numbers(a,b):
    return a+b
result = add_numbers(2,3)
print(result)

#Default Parameters

def Big(name="Friend"):
    print(f'Hello {name}')
Big()
Big("Eshwar")

