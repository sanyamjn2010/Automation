"""
x=int(input("plaease enter a value"))
if x<0:
    print("negative")
elif x>0 and x<10:
    print("positive and between 10")
else:
    print("get lost")
"""

"""
import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server};'
'Server=localhost\sqlexpress;'
'Database=sanyam;')
cursor = connection.cursor()
SQLCommand = ("INSERT INTO dbo.employeee "
                 "(name, age, salary,designation) "
                 "VALUES (1,2,3,5)")
Values = [1,2,3,4]
cursor.execute(SQLCommand,Values)
connection.commit()
connection.close()
"""


import pypyodbc
cnxn = pypyodbc.connect(r'Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=sanyam;Trusted_Connection=yes;')
cursor = cnxn.cursor()
print(cursor.execute("INSERT INTO dbo.employeee "
                 "(name, age, salary,designation) "
                 "VALUES (1,2,3,5)"))
x=SQLCommand = "SELECT * FROM employeee"
print(x)