# List
# import pandas as pd
# df = pd.Series([10,20,30])  # DataFrame --> df
# print(df)
# print(df[0])



# Dictonary
# import pandas as pd
# dict = {"Name":["Mihul","Mayank","Mohammed","Armaan","Ali"],
#         "Age":[19,20,18,21,22],
#         "Salary":[{"In-hand":"15000","ctc":"2.45pa"},{"In-hand":"20000","ctc":"2.21pa"},
#                   {"In-hand":"23000","ctc":"2.70pa"},{"In-hand":"25000","ctc":"3.21pa"},
#                   {"In-hand":"27000","ctc":"3.30pa"}]
#         }
# df = pd.DataFrame(dict)
# print(df)



# CSV
# import pandas as pd
# df = pd.read_csv("file1.csv")
# print(df)



# Excel
# import pandas as pd
# url = "file1.xlsx"
# df = pd.read_excel("url")
# print(df)



# Json
# import pandas as pd
# df = pd.read_json("file1.json")
# print(df)



# import package pandas
# import pandas as pd
# df = pd.Series([10,20,30])
# print(df)


# d = {"Name":"Mihul", "Age":19,"Roll-no":187}
# df = pd.Series(data=d, index=["Name","Age","Roll-no"])
# print(df)



# import pandas as pd
# d = {
#     "Name":["Mihul","Mayank","Priya","Mohammed","Armaan"],
#     "Roll-no":[12,13,14,15,16]
# }
# df = pd.DataFrame(data=d)
# print(df)



# # CSV
# import pandas as pd
# df = pd.read_csv("file1.csv")
# print(df)


# # JSON
# import pandas as pd
# df = pd.read_json("file1.json")
# print(df)


# EXCEL
# import pandas as pd
# df = pd.read_excel("file2.xlsx")
# print(df)



# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# # head  -> starting 5 rows
# print(df.head(2))
# # head -> 2 rows data
# print(df.head(-3))
# # head -> negative number



# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# print(df.tail(2))
# print(df.tail(-4))



# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# print(df.info())
# print(df.info(verbose=True))
# print(df.info(verbose=False))



# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# print(df.rename(columns={"name":"Student Name"},inplace=True))
# print(df)



# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# print(df.marks.describe())



# import pandas as pd

# data = {
#     "Emp_ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
#     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
#     "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
#     "Experience": [2, 3, 5, 4, 1, 3]
# }

# df = pd.DataFrame(data)

# print(df.head(2))
# print(df.tail(2))
# print(df.info())
# print(df.Salary.describe())
# print(df.shape)
# print(df.rename(columns={"Name":"Emp_Name"},inplace=True))
# print(df)




# Operations

# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)

# # get single column data
# print(df["name"])

# # add single column
# df["salary"] = [100,200,300,400,500]
# print(df)



# import pandas as pd
# d = {
#     "name":["vishal","virat","vineet"], # 3 rows
#     "salary":[100,200,300] # 3 rows
# }
# df = pd.DataFrame(data=d)
# # df["marks"] = [10,20,30]
# # df["marks"] = df["salary"] / 2
# df["holidays"] = df["salary"] / 100
# df["decrement"] = [10,20,30]
# # delete column
# df.drop(["name","salary"],axis=1,inplace=True)
# print(df)



# import pandas as pd
# d = {
#     "name":["vishal","virat","vineet"], # 3 rows
#     "salary":[100,200,300] # 3 rows
# }
# df = pd.DataFrame(data=d)

# print(df.loc[2,"name"])
# print(df.iloc[2,0])

# # get single row data
# print(df.iloc[2])
 
# # get single row using loc
# print(df.loc[0])

# # get multiple row
# print(df.iloc[0:3])

# # get multiple row using loc
# print(df.loc[0:3])

# # subdata get using iloc
# df1 = df.iloc[0:2,[0]]
# print(df1)

# # subdata get using iloc
# df2 = df.loc[0:2,["name"]]
# print(df2)





# Question

# import pandas as pd

# data = {
#     "Emp_ID": [101, 102, 103, 104, 105, 106],
#     "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
#     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
#     "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
#     "Experience": [2, 3, 5, 4, 1, 3]
# }

# df = pd.DataFrame(data)

# print(df.loc[2,"Experience"])
# print(df.iloc[3,1])

# # get single row data
# print(df.iloc[0])
 
# # get single row using loc
# print(df.loc[0])

# # get multiple row
# print(df.iloc[0:3])

# # get multiple row using loc
# print(df.loc[0:2])

# # subdata get using iloc
# df1 = df.iloc[0:6,[2]]
# print(df1)

# # subdata get using iloc
# df2 = df.loc[0:5,["Salary"]]
# print(df2)



# import pandas as pd
# df = pd.read_json("student-data.json")

# df1 = df.loc[df["gender"] == "Male", ["gender"]]
# print(df1)

# # Using Jump
# df1 = df.iloc[3:9:5]
# print(df1)

# Filter
# print(df[df["english"] == 95])
# print(df[df["maths"] < 60])
# print(df[df["physics"] <= 56])

# print(df[(df["maths"] >= 80) ^ (df["english"] >= 45)])



# import pandas as pd
# df = pd.read_json("student-data.json")

# # by default assending
# print(df.sort_values("english"))

# # decending
# print(df.sort_values("english",ascending=False))

# # by default assending method 1
# print(df.sort_values(by=["english"],ascending=False))

# # multiple cols sort
# print(df.sort_values(by=["english","maths"],ascending=[True,False]))

# df["name"] = df["name"].str.lower()
# print(df.sort_values("name"))

# # add column
# df["total"] = df["english"] + df["maths"] + df["physics"]
# print(df)

# # add row
# df.loc[14] = ["Mihul","Male",80,95,95,270]
# print(df)

# # delete column
# print(df.drop("total",axis=1))

# # delete row
# print(df.drop(14,axis=0))

# df.drop([6, 7, 8, 9, 10, 11, 12, 13], inplace=True)
# print(df)
# df['doj'] = ['2025-01-01','2025-02-02','2025-03-03','2025-04-04','2025-05-05','2025-06-06']
# print(df)



# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)

# df['doj'] = ['2025-01-01','2025-02-02','2025-03-03','2025-04-04','2025-05-05']
# print(df)

# df["doj"] = pd.to_datetime(df["doj"])
# print(df["doj"].dtype)

# # date operation
# print(df["doj"].dt.year)
# print(df["doj"].dt.month)
# print(df["doj"].dt.day)
# print(df["doj"].dt.day_name())

# # 20 days
# print(df['doj'] + pd.to_timedelta(20,unit='D'))
# print(df['doj'] + pd.to_timedelta('20 days'))



# import pandas as pd
# import numpy as np
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)

# df.loc[4, "marks"] = None
# print(df)
# df.iloc[4, 2] = None
# print(df)
# df.loc[4,'marks'] = np.nan
# print(df)
# df.iloc[4, 2] = np.nan
# print(df)

# print null
# df.loc[4, "marks"] = None
# print(df.isnull())

# column count null values
# print(df.isnull().sum())



# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)

# print(df.isnull())

# # sum
# print(df.isnull().sum())

# # drop null values by row
# print(df.dropna(axis=0))

# # drop null values by column
# print(df.dropna(axis=1))

# # fill null values by 0
# print(df.fillna(0))

# # fill by 100
# print(df.fillna(100))

# # roll no -> 200 | marks -> 100
# print(df.fillna({"roll no":200,"marks":100}))

# # marks column fill by mean
# print(df.fillna({"marks":df["marks"].mean()}))



# aggregation
# import pandas as pd
# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)

# # manual
# print(df["marks"].sum())
# print(df["marks"].mean())
# print(df["marks"].min())
# print(df["marks"].max())

# print(df["marks"].agg(["sum","mean","min","max","std"]))



# concatenate
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df1 = pd.read_json(url)
print(pd.concat([df,df1],axis=0)) # row wise
print(pd.concat([df,df1],axis=1)) # column wise

# change name
df.loc[2, "name"] = "Mihul"
print(df)