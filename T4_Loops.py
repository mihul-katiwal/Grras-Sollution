# for
for i in range(5):
    print(i)

for i in range(1, 11):
    print("Number:", i) 

l = [1, 2, 3, 4, 5]
print(len(l))
for i in range(5):
    print(l[i])

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)



# while
num1 = int(input("Enter a number: "))
i = 0
while i < num1:
    print(i)
    i += 1

l = [11, 12, 13, 14, 15]
i = 0
while i < len(l):
    print(l[i])
    i += 1

d = {"name": "Mihul", "age": 18, "phone": "9116640022"}
print(d)
for i in range(len(d.keys())):
    print(i)

# example
l = [10, [11, 12, 13, 14, 15]]
for i in range(len(l[1])):
    print(l[1][i])

for i in l[1]:
    print(i)



# break
for i in range(10):
    if i == 5:
        break
    print(i)



# continue
i = 0
while True:
    i += 1
    if i == 5:
        continue
    print(i)
   



# pass
i = 0
while True:
    print(i)
    if i == 4:
        pass
    if i == 5:
        break
    else:
        i += 1
        continue
