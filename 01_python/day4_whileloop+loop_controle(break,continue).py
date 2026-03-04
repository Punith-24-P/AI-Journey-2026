i = 1
while i <= 20:
    print(i)
    
    i += 1
    
    
i = 2
while i <= 50:
    print(i)
    
    i += 2
    
    
    
i = 1
while True:
    print(i)
    
    if i == 10:
        break
    i += 1
    
i = 1
while i <= 20:
    print(i)
    i += 2
    

while True:
    i = int(input("enter the number"))
    if i == 7:
        
        print("Correct")
        break
    else:
        print("Try again")

rows = 4

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()
    

rows = 4
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    

rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()   