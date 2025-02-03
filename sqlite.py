import sqlite3

# connecting to sqlite3 database
connection=sqlite3.connect("Student.db")

# to insert,create records by using a object called cursor
cursor=connection.cursor()

# table information
table_info="""
Create Table Student(NAME VARCHAR(25),
            CLASS VARCHAR(25),
            SECTION VARCHAR(25))
"""
# creating a table
cursor.execute(table_info)

#inserting records
cursor.execute("""Insert into Student values('manav','10','C')""")
cursor.execute("""Insert into Student values('abhi','10','E')""")
cursor.execute("""Insert into Student values('riya','9','F')""")
cursor.execute("""Insert into Student values('ruchita','10','C')""")
cursor.execute("""Insert into Student values('kamlesh','9','A')""")

# display the inserted records
print("The inserted records are: ")
data=cursor.execute("""Select * from Student""")
for row in data:
    print(row)

connection.commit()
connection.close()