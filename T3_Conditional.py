# if
num1 = 10
num2 = 20
if num1 < num2:
    print(num2)

# if else
num1 = int(input("Enter first number: "))
if num1 :
    print("number :-", num1)
else:
    print("zero", num1)

# if elif else
age = int(input("Enter your age: "))
if age == 18:
    print("your age is:", age)
elif age > 18:
    print("you are above then:", age)
else:
    print("you are below then:", age)    


# example
age = int(input("Enter your age: "))
if age == 18:
    print("aligible for vote")
elif age > 18:
    print("aligible for vote")
else:
    print("not aligible for vote")

# example
marks = int(input("Enter your marks: "))
if marks >= 60:
    print("Grade C")
elif marks >= 75:
    print("Grade B")
elif marks >= 90:
    print("Grade A")
else:
    print("Fail")
