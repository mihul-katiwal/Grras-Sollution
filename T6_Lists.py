# List

L = [10,20,30,40,50,"hello",True]
print(L)
print(L[0])
print(L[-1])
print(L[-2])


# Example of append

L = ["hello", "yourname", "python"]
L.append("for arya mains")
print(L)
print(L[0])
print(L[-1])



# Example for insert

L = [True,False,10,20]
L.insert(1,100)
print(L)


# Question

L = [10,20,30,{"name":"yourname","address": ["jaipur","kukas","home town","friend house"]}]
print(L[3]['address'])
print(L[-1]['address'])
for i in L[3]['address']:
    print(i)


# question

l = [10,20,30,[40,50,[60,70,80]]]
for i in range(len(l[3])-1):
  print(l[3][i])


for i in l[3]:
  print(i)

# Question

l = [10,20,[30,40,50,60]]
print([l[2][i] for i in range(len(l[2]))])
print([l[-1][i] for i in range(len(l[-1]))])



# Nested list  --> Slicing

L = [10,20,30,["hello","hello1","hello2",[True,False]]]
print(L)

# slicing
L1 = L[:3]
print(L1)

# Example
print(L[2:])

print(L[3][1:3])
print(L[3][3][1:])




# Map (2 arguments)
# using Function


def square(x):
    return x * x

L = [10, 20, 30]
L1 = list(map(square, L))
print(L1)


# Map (2 arguments) using lambda
L = [10, 20, 30]
L1 = list(map(lambda x:x*x, L))
print(L1)


# alternative | without in built function
L1 = []
for i in range(len(L)):
    L1.append(L[i]*L[i])   
print(L1)


# Example
def hello(x):
    return x.upper()

L = ["apple", "boy", "cat", "dog"]
L1 = list(map(hello, L))
print(L1)


# Filter
def hello(x):
    return x.startswith('a')

L = ["apple","boy","cat","dog"]
L1 = list(filter(hello,L))
print(L1)


# Filter using lambda
L = ["apple", "boy", "cat", "dog"]
L1 = list(filter(lambda x: x.startswith("a"), L))
print(L1)


# Example | alternative of filter
L1 = []
for i in L:
    if 'g' == i[-1]:
        L1.append(i)
print(L1)    


# Reduce
# L = [10,20,30]
