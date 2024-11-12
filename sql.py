import sqlite3

## Connect to sqlite database
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record,create table,retrieve data
cursor=connection.cursor()

## create the table 
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

## Insert Some more records
cursor.execute('''Insert into STUDENT('Mudassir','Web Developer','A',90)''')
cursor.execute('''Insert into STUDENT('John Doe', '10th', 'A', 85)''')
cursor.execute('''Insert into STUDENT('Alice Smith', '9th', 'B', 92)''')
cursor.execute('''Insert into STUDENT('Michael Brown', '11th', 'C', 78)''')
cursor.execute('''Insert into STUDENT('Jessica Lee', '12th', 'A', 88)''')
cursor.execute('''Insert into STUDENT('Arjun Patel', '10th', 'A', 85)''')
cursor.execute('''Insert into STUDENT('Anjali Gupta', '12th', 'A', 88)''')
cursor.execute('''Insert into STUDENT('Sanya Mehta', '12th', 'B', 89)''')
cursor.execute('''Insert into STUDENT('Sneha Rao', '9th', 'A', 93)''')
cursor.execute('''Insert into STUDENT('Ananya Iyer', '12th', 'A', 88)''')
cursor.execute('''Insert into STUDENT('Priya Sharma', '9th', 'B', 92)''')

## Display all the records in the database
print("The inserted records are")


data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close()