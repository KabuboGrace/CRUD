import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected")


conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(1,'Grace','Kabubo',21, 45000.00,'Employer')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(2,'Mark','Masaai',25, 67000.00,'Manager')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(3,'Mercy','Nungari',31, 35000.00,'Chef')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(4,'Thomas','Kamau',26,64000.00,'HR')")

conn.commit()
print("Successfully inserted values into Staff table")

conn.close()