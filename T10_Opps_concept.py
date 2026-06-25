# example

# class Mihul:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(self.name)

# r = Mihul("Hello")
# r.show()


# Example 1

# class Mihul:
#     def __init__(self):
#         print("calling constructor")

#     def show(self):
#         print("show the name")

# r = Mihul()
# r.show()


# Example 2

# class Mihul:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getAge(self):
#         print("My age is: ",self.age)
    
#     def getName(self):
#         print("My name is: ",self.name)

# r = Mihul("hello",20)
# r.getName()
# r.getAge()

# r = Mihul(age = 19, name = "Mihul")
# r.getName()
# r.getAge()


# Example 3

# class student:
#     def __init__(self,*args):
#         print(type(args))
#         print(args)
#         self.name = args[0]

#     def getstudent(self):
#         print("the student is:",self.name)
#         return self.name

# s = student("Mihul",19,"9116640022","mihul@gmail.com")
# t = s.getstudent()
# print(t)


# Example 4

# class student:
#     def __init__(self,args):
#         print(type(args))
#         print(args)
#         self.name = args

#     def getstudent(self):
#         # print("the student is:",self.name)
#         return self.name

# s = student({"name":"Mihul","age":19})
# t = s.getstudent()
# print(t["name"])
# print(t["age"])


# Example 5

# class Student:
#     def __init__(self, *args):
#         self.names = args[0]
#         self.info = args[1]

#     def users(self):
#         for name in self.names:
#             print(name)

#     def details(self):
#         for key, value in self.info.items():
#             print(key, ":", value)


# s = Student(["dheeraj", "kunal", "harsh", "praveen"],{"address": "kukas", "college": "arya", "loc": "jaipur"})

# s.users()
# s.details()



# class student:
#     def __init__(self,*args):
#         self.data = args

#     def users(self):
#         for i in self.data[0]:
#             print(i)

#     def details(self):
#         print(self.data[1])
#         for i in self.data[1]:
#             print()

# s = student(["dheeraj","kunal","harsh","praveen"],{"address":"kukas","college":"arya","loc":"jaipur"})

# print("--- Users List ---")
# s.users()
# print("\n--- Details ---")
# s.details()



# Constructor

# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

# a = Address("Jaipur","Rajasthan")
# print(a.state)
# print(a.city)



# Class method and self

# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

#     def show(self):
#         print("the city is: ",self.city)

# a = Address("Jaipur","Rajasthan")
# a.show()



# Inheritance

# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
  
#     def location(self):
#         return f"My location is {self.city} in {self.state}"
 
# class User(Address):
#     def __init__(self,name,age,city,state):
#         super().__init__(city,state)
#         self.name = name
#         self.age = age
#         # self.city = city
#         # self.state = state
 
#     def userName(self):
#         print(f"my name is {self.name}")
 
#     def userDetails(self):
#         print(f"My name is {self.name} and My location is {self.city} in {self.state}")
 
# u = User("Mihul",20,"Kukas","Rajasthan")
# print(u.city)
# u.userDetails()
# print(u.location())





# Encapsulation

# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

#     def location(self):
#         print(f"My location is {self.city} in {self.state}")

# a = Address("Jaipur","Rajasthan")
# a.location()
# print(a.city)
# print(a.state)



# Polymorphism

# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

#     def location(self):
#         print(f"My location is {self.city} in {self.state}")

# class Hometown:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

#     def location(self):
#         print(f"My hometown is {self.city} in {self.state}")

# a = Address("Jaipur","Rajasthan")
# a.location()

# h = Hometown("Kukas","Rajasthan")
# h.location()




# Class variable

# class Address:
#     total = 0  # Class variable

#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#         Address.total += 1

#     def location(self):
#         print("location")


# # Creating instances
# a = Address("Jaipur", "Rajasthan")
# b = Address("Alwar", "Rajasthan")

# # Printing the total count
# print(a.total)

 


# overloading and overriding


# def address(city, state):
#     print(f"My location is {city} in {state}")

# def address(city, state, country):
#     print(f"My location is {city} in {state}, {country}")

# # address("Jaipur", "Rajasthan") --> this will give an error because the second function definition overwrites the first one. To avoid this, we can use default arguments or variable-length arguments.
# address("Jaipur", "Rajasthan", "India")



# overriding

# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
    
#     def location(self):
#         print("Address Location")

# class User(Address):
#     def __init__(self,name,age,city,state):
#         super().__init__(city,state)
#         self.name = name
#         self.age = age

#     def location(self):
#         print("User location")

# u = User("Arya Mains",20,"Kukas","Rajasthan")
# u.location()
# Address.location(u) 