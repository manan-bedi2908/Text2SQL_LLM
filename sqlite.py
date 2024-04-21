import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()
table_info = """
Create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25)
);
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Manan', 'DS', 'A')''')
cursor.execute('''Insert Into STUDENT values('Ritesh', 'Web', 'B')''')
cursor.execute('''Insert Into STUDENT values('Tanishq', 'SDE', 'C')''')
cursor.execute('''Insert Into STUDENT values('Hitesh', 'SDE', 'D')''')
cursor.execute('''Insert Into STUDENT values('Lakshay', 'DSA', 'E')''')

print("The inserted records are: ")
data = cursor.execute('''SELECT * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()