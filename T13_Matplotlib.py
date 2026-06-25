import matplotlib.pyplot as plt
score = [10,20,30,40]
over = [1,2,3,4]
plt.plot(score, over)
plt.show()



import matplotlib.pyplot as plt # visualization
x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.
plt.plot(x,y) # Line graph
plt.xlabel("Years") # x label
plt.ylabel("Sales") # y label
plt.title("Sales Report") # graph title
plt.show() # graph show



import matplotlib.pyplot as plt
x = [2010, 2015, 2020, 2025]
y = [100, 200, 250, 300]

# graph size
plt.figure(figsize=(6, 2))
plt.plot(x, y)
plt.show()



import matplotlib.pyplot as plt
x = [2010, 2015, 2020, 2025]
y = [100, 200, 250, 300]
plt.plot(x, y, color="green", marker="o", linestyle="dashed", linewidth=2, markersize=10)
plt.show()




import matplotlib.pyplot as plt
x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.

# '''
# **Markers**
# |character      |  |  |description |
# |-------------|  -------------------------------|
# |'.'       | | |point marker|
# |','       | | |pixel marker|
# |'o'       | | |circle marker|
# |'v'       | | |triangle_down marker|
# |'^'       | | |triangle_up marker|
# |'<'       | | |triangle_left marker|
# |'>'       | | |triangle_right marker|
# |'1'       | | |tri_down marker|
# |'2'       | | |tri_up marker|
# |'3'       | | |tri_left marker|
# |'4'       | | |tri_right marker|
# |'8'       | | |octagon marker|
# |'s'       | | |square marker|
# |'p'       | | |pentagon marker|
# |'P'       | | |plus (filled) marker|
# |'*'       | | |star marker|
# |'h'       | | |hexagon1 marker|
# |'H'       | | |hexagon2 marker|
# |'+'       | | |plus marker|
# |'x'       | | |x marker|
# |'X'       | | |x (filled) marker|
# |'D'       | | |diamond marker|
# |'d'       | | |thin_diamond marker|
# |'|'       | | |vline marker|
# |'_'       | | |hline marker|

# **Line Styles**

# |character      |  |  |  |description |
# |-------------|   -------------------------------|
# |'-'       | | | |solid line style|
# |'--'      | | | |dashed line style|
# |'-.'      | | | |dash-dot line style|
# |':'       | | | |dotted line style|

# Example format strings:

#     'b'    # blue markers with default shape
#     'or'   # red circles
#     '-g'   # green solid line
#     '--'   # dashed line with default color
#     '^k:'  # black triangle_up markers connected by a dotted line
# **Colors**

# |character      |  |  |  |color |
# |-------------|   -------------------------------|
# |'b'       | | | |blue|
# |'g'       | | | |green|
# |'r'       | | | |red|
# |'c'       | | | |cyan|
# |'m'       | | | |magenta|
# |'y'       | | | |yellow|
# |'k'       | | | |black|
# |'w'       | | | |white|
# '''

# # graph size
# plt.figure(figsize=(6,2)) # width or height
# plt.plot(x,y,color="y",marker='*',linestyle=":",linewidth=4,markersize=14,)
# plt.show()



# # Multi Lines Chart
# import matplotlib.pyplot as plt

# x = [2010,2015,2020,2025]
# y1 = [100,200,260,290]
# y2 = [150,185,195,300]

plt.plot(x,y1,label="jeans")
plt.plot(x,y2,label="shirt")
plt.xlabel("years")
plt.ylabel("sales")
plt.title("Sales Report")
plt.legend() # info of label
plt.show()



# # Question 1

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_A = [100, 120, 140, 130, 150]
sales_B = [90, 110, 135, 145, 160]
sales_C = [80, 100, 120, 125, 140]

plt.plot(months, sales_A, marker='o', label='Product A')
plt.plot(months, sales_B, marker='s', label='Product B')
plt.plot(months, sales_C, marker='^', label='Product C')

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()


# # Question 2

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

city1 = [30, 32, 31, 33, 35]
city2 = [28, 29, 30, 31, 32]
city3 = [25, 27, 26, 28, 29]

plt.figure(figsize=(8,5))

plt.plot(days, city1, marker='o', label="Jaipur")
plt.plot(days, city2, marker='s', label="Delhi")
plt.plot(days, city3, marker='^', label="Mumbai")

plt.title("Temperature Comparison")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.show()




# Bar Chart
import matplotlib.pyplot as plt
x = [2015,2020,2025,2030]
y = [100,150,200,290]

# size
plt.figure(figsize=(6,2)) 
plt.bar(x,y)
plt.show()




# Multi Bar Chart
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y1 = [10,20,20,40]
y2 = [20,30,25,30]
# calculation -> width
w = 0.40
plt.bar(x - w/2,y1 , label="boys",width=w) 
plt.bar(x + w/2,y2, label="girls",width=w) 

plt.xlabel("groups")
plt.ylabel("number of students")
plt.title("Number of Students in Each group")
plt.legend()
plt.show()



# Question 1
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])

y1 = [10, 20, 20, 40]
y2 = [15, 25, 30, 35]
y3 = [20, 30, 25, 30]

w = 0.25

plt.bar(x - w, y1, width=w, label="Boys")
plt.bar(x,     y2, width=w, label="Girls")
plt.bar(x + w, y3, width=w, label="Others")

plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in Each Group")
plt.legend()

plt.show()



# Question 2
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)

y1 = [1, 1.2, 2.3, 1.2]
y2 = [1.5, 1.4, 1, 3.2]
y3 = [4, 3, 2, 1]

w = 0.25

plt.bar(x - w, y1, width=w, label="2023", color="lightblue")
plt.bar(x,     y2, width=w, label="2024", color="blue")
plt.bar(x + w, y3, width=w, label="2025", color="lightgreen")

plt.xticks(x, ["Vehicle", "Home", "Work", "Office"])
plt.yticks([0, 1, 2, 3, 4], ["0", "1M", "2M", "3M", "4M"])

plt.title("Sales Comparison by Category")
plt.xlabel("Category")
plt.ylabel("Sales (Millions)")

plt.grid(axis="y")
plt.legend()
plt.show()



import matplotlib.pyplot as plt
marks = [40, 55, 60, 75, 90, 33, 50]
plt.hist(marks, bins=8, color="green")
plt.show()



# Pie Chart

import matplotlib.pyplot as plt

fruits = ["Apple", "Watermelon", "Orange", "Mango"]
count = [40, 30, 15, 70]

plt.pie(count, labels=fruits, autopct="%1.1f%%", colors=["red","green","orange","yellow"])
plt.title("Fruit Distribution")
plt.show()



import matplotlib.pyplot as plt

fruits = ["Apple", "Watermelon", "Orange", "Mango"]
count = [40, 30, 15, 70]
colors=["red","green","orange","yellow"]

plt.pie(count, labels=fruits, autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("Fruit Distribution")
plt.show()


# Subplots Chart

import matplotlib.pyplot as plt

# First subplot (Line Graph)
plt.subplot(1, 2, 1)
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 55]
plt.plot(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Graph")

# Second subplot (Pie Chart)
plt.subplot(1, 2, 2)
x1 = ["Apple", "Watermelon", "Orange", "Mango"]
y1 = [40, 30, 15, 70]
plt.xlabel("X1 Values")
plt.ylabel("Y1 Values")
plt.pie(y1, labels=x1, autopct="%1.1f%%",startangle=90)
plt.title("Pie Chart")

plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

fruits = ["Apple", "Watermelon", "Orange", "Mango"]
counts = [40, 30, 15, 70]

plt.figure(figsize=(12, 8))

# Line Chart
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o')
plt.title("Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(counts, labels=fruits, autopct="%1.1f%%")
plt.title("Pie Chart")

# Histogram
plt.subplot(2, 2, 4)
plt.hist(y, bins=5)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt

# Monthly Sales Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 200, 170, 220]

plt.figure(figsize=(12, 8))

# Line Chart
plt.subplot(2, 2, 1)
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(sales, labels=months, autopct="%1.1f%%", startangle=90)
plt.title("Monthly Sales - Pie Chart")

# Histogram
plt.subplot(2, 2, 4)
plt.hist(sales, bins=8)
plt.title("Monthly Sales - Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()



import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 8))

# 1. Line Chart
plt.subplot(2, 2, 1)

months = ["Jan", "Feb", "Mar", "Apr", "May"]
profit = [15, 25, 20, 35, 40]

plt.plot(months, profit, marker='s')
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")

# 2. Bar Chart
plt.subplot(2, 2, 2)

subjects = ["Math", "Science", "English", "Computer"]
marks = [70, 92, 78, 95]

plt.bar(subjects, marks)
plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# 3. Pie Chart
plt.subplot(2, 2, 3)

devices = ["Mobile", "Laptop", "Tablet", "Desktop"]
users = [45, 30, 15, 10]

plt.pie(users,labels=devices,autopct="%1.1f%%",explode=[0.1, 0, 0, 0],shadow=True)

plt.title("Device Usage")

# 4. Histogram
plt.subplot(2, 2, 4)
scores = np.random.randint(40, 100, 500)

plt.hist(scores,bins=10, edgecolor="black")

plt.title("Exam Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()



# Subplots Graph
import matplotlib.pyplot as plt

# graph one data
year = [2010, 2015, 2020, 2025]
dairy = [100, 520, 630, 400]

# graph two data
year = [1990, 2000, 2005, 2010]
farming = [300, 200, 250, 100]

fig, aux = plt.subplots(1, 2, figsize=(10, 4))

aux[0].plot(year, dairy)
aux[0].set_xlabel("Year")
aux[0].set_ylabel("Dairy")
aux[0].set_title("Dairy Production Graph")

aux[1].plot(year, farming)
aux[1].set_xlabel("Year")
aux[1].set_ylabel("Farming")
aux[1].set_title("Farming Production Graph")

plt.tight_layout()
plt.show()




# Subplots Graph
import matplotlib.pyplot as plt

# graph one data
year1 = [2010, 2015, 2020, 2025]
dairy = [100, 520, 630, 400]

# graph two data
year2 = [1990, 2000, 2005, 2010]
farming = [300, 200, 250, 100]

# graph three data
year3 = [2000, 2005, 2010, 2015]
fishing = [150, 250, 300, 200]

# graph four data
year4 = [1980, 1990, 2000, 2010]
flowers = [50, 100, 150, 200]

# Create a 2x2 subplot grid
fig, aux = plt.subplots(2, 2, figsize=(10, 8))

# Dairy Production Graph
aux[0, 0].plot(year1, dairy, color="black", marker="o")
aux[0, 0].set_xlabel("Year")
aux[0, 0].set_ylabel("Dairy")
aux[0, 0].set_title("Dairy Production Graph")
aux[0, 0].grid(True)

# Farming Production Graph
aux[0, 1].plot(year2, farming, color="green", marker="*")
aux[0, 1].set_xlabel("Year")
aux[0, 1].set_ylabel("Farming")
aux[0, 1].set_title("Farming Production Graph")
aux[0, 1].grid(True)

# Fishing Production Graph
aux[1, 0].plot(year3, fishing, color="blue", marker="^")
aux[1, 0].set_xlabel("Year")
aux[1, 0].set_ylabel("Fishing")
aux[1, 0].set_title("Fishing Production Graph")
aux[1, 0].grid(True)

# Flowers Production Graph
aux[1, 1].plot(year4, flowers, color="red", marker="s")
aux[1, 1].set_xlabel("Year")
aux[1, 1].set_ylabel("Flowers")
aux[1, 1].set_title("Flowers Production Graph")
aux[1, 1].grid(True)

plt.tight_layout()
plt.show()




import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [85, 90, 75, 88, 95]
 
attendance = [80, 90, 75, 85, 95]
 
ages = [18, 19, 18, 20, 19]
 
fig, ax = plt.subplots(2, 2)
 
# Line Chart
ax[0,0].plot(students,marks,marker='o')
ax[0,0].set_title("Marks Trend")
ax[0,0].set_xlabel("Students")
ax[0,0].set_ylabel("Marks")
ax[0,0].grid(True)
 
# Bar Chart
ax[0,1].bar(students,attendance,color="orange")
ax[0,1].set_title("Attendance")
ax[0,1].set_xlabel("Students")
ax[0,1].set_ylabel("Attendance %")
 
# pie char
ax[1,0].pie(ages,labels= students)
 
# Histogram
ax[1,1].hist(marks,bins=5,color="green",edgecolor="black")
ax[1,1].set_title("Marks Distribution")
ax[1,1].set_xlabel("Marks")
ax[1,1].set_ylabel("Frequency")
 
plt.tight_layout()
 
plt.gcf().canvas.get_supported_filetypes()
plt.savefig("subplot.jpg")

plt.show()




# Mini Project 1

import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_json("temperature-data.json")

print("Original DataFrame:")
print(df)

df = df[df['day'] != 'Wednesday']

df['humidity_pct'] = df['humidity_pct'].fillna(df['humidity_pct'].mean())

df['temperature_f'] = (df['temperature_c'] * 9/5) + 32

print("\nUpdated DataFrame:")
print(df)

# Subplots --> pie chart and line chart

fig, ax = plt.subplots(3, 3, figsize=(12, 8))

# Temperature (Celsius)
ax[0, 0].plot(df['day'], df['temperature_c'], marker='o', color='blue')
ax[0, 0].set_title("Temperature (°C) Line Chart")
ax[0, 0].set_xlabel("Day")
ax[0, 0].set_ylabel("Temperature")
ax[0, 0].grid(True)

# Humidity
ax[0, 1].plot(df['day'], df['humidity_pct'], marker='s', color='green')
ax[0, 1].set_title("Humidity (%) Line Chart")
ax[0, 1].set_xlabel("Day")
ax[0, 1].set_ylabel("Humidity")
ax[0, 1].grid(True)

# Temperature (Fahrenheit)
ax[0, 2].plot(df['day'], df['temperature_f'], marker='^', color='red')
ax[0, 2].set_title("Temperature (°F) Line Chart")
ax[0, 2].set_xlabel("Day")
ax[0, 2].set_ylabel("Temperature")
ax[0, 2].grid(True)

# Bar chart of Temperature (Celsius)
ax[1, 0].bar(df['day'], df['temperature_c'], color='orange')
ax[1, 0].set_title("Temperature (°C) Bar Chart")
ax[1, 0].set_xlabel("Day")
ax[1, 0].set_ylabel("Temperature")
ax[1, 0].grid(True)

# Bar chart of Humidity
ax[1, 1].bar(df['day'], df['humidity_pct'], color='Skyblue')
ax[1, 1].set_title("Humidity (%) Bar Chart")
ax[1, 1].set_xlabel("Day")
ax[1, 1].set_ylabel("Humidity")
ax[1, 1].grid(True)

# Bar chart of Temperature (Fahrenheit)
ax[1, 2].bar(df['day'], df['temperature_f'], color='purple')
ax[1, 2].set_title("Temperature (°F) Pie Chart")
ax[1, 2].set_xlabel("Day")
ax[1, 2].set_ylabel("Temperature")
ax[1, 2].grid(True)

# Pie Chart of Temperature (Celsius)
ax[2,0].pie(
    df['temperature_c'],
    labels=df['day'],
    autopct='%1.1f%%'
)
ax[2,0].set_title("Temperature (°C) Pie Chart")

# Pie Chart of Temperature (Humidity)
ax[2,1].pie(
    df['humidity_pct'],
    labels=df['day'],
    autopct='%1.1f%%'
)
ax[2,1].set_title("Humidity (%) Pie Chart")

# Pie Chart of Temperature (Fahrenheit)
ax[2,2].pie(
    df['temperature_f'],
    labels=df['day'],
    autopct='%1.1f%%'
)
ax[2,2].set_title("Temperature (°F) Pie Chart")

plt.tight_layout()
plt.show()
