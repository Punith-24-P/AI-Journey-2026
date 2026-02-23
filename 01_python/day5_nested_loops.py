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