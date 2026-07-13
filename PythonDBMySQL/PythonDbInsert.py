import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="practice",
    password="practice",
    database="spring_security"
)

#print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#    print(x)

#mycursor.execute("CREATE TABLE spring_security.customers (id int primary key,name VARCHAR(100),address VARCHAR(100))")

sql = "insert into customers (name,address) values (%s,%s)"
val = ("Ram","Highway 181")
mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount, "Record created")