print("Day 2 - variables practice")

name = "Punith"
age = 20
hight = 5.8

print("Name:",name)
print("Age:",age)
print("Hight:",hight)


user_name = input("Enter your name:")
user_age = int(input("Enter your age:"))

print("Hello",user_name)
print("Next year you will be",user_age + 1)



num = int(input("Enter a number:"))

if num % 2 == 0:
    print("Even")
else:
    print("odd")
    
    
    
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a >= b and a >= c:
    print("Largest is:",a)
elif b >= a and b >= c:
    print("Largest is:,b")
else:
    print("Largest is:",c)
    
    
for i in range(1, 11):
    print(i)



n = int(input("Enter a number for sum:"))
total = 0

for i in range(1,n + 1):
    total += i

print("Sum is:",total)


print("--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(f"Result: {num1 + num2}")
elif op == "-":
    print(f"Result: {num1 - num2}")
elif op == "*":
    print(f"Result: {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid Operator")
    
    
for a in range(1, 11):
    print(a)
    
i = 1

while i <= 10:
    print(i)
    i += 1
    
n = int(input("enter the number:"))

total = 0
for i in range(1,n + 1):
    total += i
    
print("sum is:",total)    

for i in range(2, 50, 2):
    print(i)    
    
i = 2
while i <= 50:
    print(i)
    i += 2

        
        
