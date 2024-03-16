import mysql.connector as mysql


db=mysql.connect(
    host='127.0.0.1',
    user='practice',
    port=3306,
    password='practice',
    database="example_database")


print("connected to: ",db.get_server_info())