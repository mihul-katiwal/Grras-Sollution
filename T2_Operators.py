# operators & expressions
# +, -, *, /, //, %, **

# +
a = 10
b = 20
print(a + b)

# -
c = 20
d = 10
print(c - d)

# *
e = 10
f = 5
print(e * f)

# /
num1 = 20
num2 = 2
print(num1 / num2)

# //
num3 = 20
num4 = 2
print(num3 // num4)

# %
num5 = 10
num6 = 3
print(num5 % num6)

# **
num7 = 5
num8 = 3
print(num7 ** num8)

# Example (even or odd)
num1 = int(input("Enter first number: "))
num2 = 2
print(num1 % num2)



# relational operators
# ==, !=, >, <, >=, <=

# ==
num1 = 10
num2 = 11
print(num1 == num2)

# <
num1 = 10
num2 = 11
print(num1 < num2)

# >
num1 = 20
num2 = 10
print(num1 > num2)

# <=
num1 = 10
num2 = 10
print(num1 <= num2)

# >=
num1 = 20   
num2 = 10
print(num1 >= num2)

# !=
num1 = 10
num2 = 10
print(num1 != num2)



# assignment operators
# =, +=, -=, *=, /=, //=, %=, **=

# =
a = 10
b = a + 20
print(b)

# +=
a = 10
a += 20
print(a)

# -=
a = 20
a -= 10
print(a)

# *=
a = 10
a *= 5
print(a)

# /=
a = 20
a /= 2
print(a)

# //=
a = 20
a //= 2
print(a)

# %=
a = 10
a %= 3
print(a)

# **=
a = 5
a **= 3
print(a)



# logical operators
# and, or, not

# and
a = 10
b = 20
print(a and b)

# or
a = 10
b = 20
print(a or b)

# not
num = []
print(not num)

a = -10
b = 10
print(a and b)
print(a or b)

name1 = "Mihul"
name2 = ""
print(name1 and name2)
print(name1 or name2)



# bitwise operators
# &, |, ^, ~, <<, >>

# &
a = 5
b = 2
print(a & b)

# |
a = 5
b = 2
print(a | b)

# ^
a = 5
b = 2
print(a ^ b)

# ~
a = 4
print(~a)

# <<
a = 5
print(a << 1)

# >>
a = 5
print(a >> 1)

# example
name = 10
name1 = 10
print(name == name1)
print(name is name1)
print(id(name), id(name1))
