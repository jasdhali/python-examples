import mysql.connector as mysql


conn = mysql.connect(
    host='127.0.0.1',
    user='practice',
    port=3306,
    password='practice',
    database="example_database")


#print("connected to: ",db.get_server_info())

cursor = conn.cursor()

sql = "insert into example_database.country  values (2,1,'US','USA')"

try:
    # Executing the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    conn.commit()
except:
    # Rolling back in case of error
    conn.rollback()
    # Closing the connection
    conn.close()