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