'''
#Python loop

for x in range(10): #0123456789
    print(x)

for x in range(1, 10): #123456789
    print(x)  

for x in range(1, 10, 2): #13579
    print(x)

for x in range(5): #0124
    if x == 3:
        continue
    print(x)

for x in range(5): #012
    if x == 3:
        break
    print(x)

fruit = ["apple", "banana", "cherry"]

for i in fruit:
    print(i)

#Python nested loop

for i in range(2):
    for j in range(3):
        print("i: {}, j: {}".format(i, j), end=" ")
    print()

#PYTHON WHILE LOOP

i = 1
while i < 6:
    print(i)
    i += 1
'''
