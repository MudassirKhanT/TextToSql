import sqlite3

## Connect to sqlite database
connection = sqlite3.connect("st.db")

## Create a cursor object to insert record,create table,retrieve data
cursor=connection.cursor()

## create the table 
table_info="""
Create table ST(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

## Insert Some more records
cursor.execute('''Insert into ST values('Mudassir','Web Developer','A',90)''')
cursor.execute('''Insert into ST values('John Doe', '10th', 'A', 85)''')
cursor.execute('''Insert into ST values('Alice Smith', '9th', 'B', 92)''')
cursor.execute('''Insert into ST values('Michael Brown', '11th', 'C', 78)''')
cursor.execute('''Insert into ST values('Jessica Lee', '12th', 'A', 88)''')
cursor.execute('''Insert into ST values('Arjun Patel', '10th', 'A', 85)''')
cursor.execute('''Insert into ST values('Anjali Gupta', '12th', 'A', 88)''')
cursor.execute('''Insert into ST values('Sanya Mehta', '12th', 'B', 89)''')
cursor.execute('''Insert into ST values('Sneha Rao', '9th', 'A', 93)''')
cursor.execute('''Insert into ST values('Ananya Iyer', '12th', 'A', 88)''')
cursor.execute('''Insert into ST values('Priya Sharma', '9th', 'B', 92)''')

## Display all the records in the database
print("The inserted records are")


data=cursor.execute('''Select * From ST''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close()