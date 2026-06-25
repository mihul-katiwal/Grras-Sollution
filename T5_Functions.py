# function

# def hello():
#     print("Hello function is working")
# hello()



# example

# def hello(a):
#     print(a)    
# hello(100)



# example

# def add(a = 2,b = 3):
#     c = a + b
#     print(c)
# add(10,5)    
# add()



# example

# def power(a,b):
#     c = a ** b
#     print(c)
# power(5,2)
# power(2,5)
# power(b = 5,a = 2)
# power(a = 2,b = 5)



# example

# def student(*a):
#     print(a)
#     print(type(a))
#     print(a[0])
# student(1,2,3,4,5)



# example

# def student(a,b):
#     print(a,b)
# student(1,2)



# Question
# def marks(a):
#     for i in a:
#         print(i)
 
# marks([10,20,30,40,50])  



# Question

# def address(a):
#     print(a)
#     for i in a:
#         for j in i:
#               print(j)
 
# address(['hello','yourname'])  



# example
# def sum(a,b):
#     return a + b

# result = sum(10,20)
# print(result)







# --> Lambda function 

# add = lambda x: x
# print(add(100))

# sum = lambda x,y: x + y
# print(sum(10,20))

# a = lambda x: x
# print(a([10,20,30,40]))



# Question

# a = lambda *x: [i for i in x]
# print(a(10,20,30,40,50))
# print(a("Mihul","World"))



# list comprehension [expression for item in iterable]
# print([i for i in range(5)])


# example
# l = [10,20,30,40,50,60]
# print([l[i] for i in range(len(l))])

# Question
 
# l = [10,20,30,40,50,60]

# print([l[i] for i in range(1, len(l) + 1)])