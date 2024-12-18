# if
age=18
if age>=18:
    print("You are an adult")

# if-else
age =16
if age>=18:
    print("You are an adult")
else :
    print("You are minor")
    
# if-elif-else

age=9
if age>=18:
    print("You are an adult")
elif age>=10 or age<18:
    print("You are minor")
else :
    print("You are a Child")    

# nested if

age =21
has_license=True

if(age>=10):
    if(has_license):
        print("You are eligible for applying driving license")
    else:
        print("You need License")
else:
    print("You are too young not eligible for driving")      
    
#Logical operators     
temperate=25
is_sunny=True
if(temperate>20 and is_sunny):
    print("Perfect time for Picnic")
else:
    print("We will plan another day")       
    
is_raining=False
if not is_raining:
    print("No need of Umbrella")     
    
#terinary operators

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)    

# Comparision Operators


x = 10
y = 5
print(x == y)  
print(x > y)  


name = "Alice"
print(name == "Alice") 
print(name != "Bob")   


fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) 
print("orange" not in fruits) 
