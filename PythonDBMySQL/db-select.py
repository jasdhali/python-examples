import mysql.connector

try:
    # 1. Establish the connection
    connection = mysql.connector.connect(
        host='localhost',        # or server IP
        user='practice',
        password='practice',
        database='example_database'
    )

    if connection.is_connected():
        # 2. Create a cursor object
        #cursor = connection.cursor()
        # Create a dictionary cursor
        cursor = connection.cursor(dictionary=True)

        # 3. Execute a query
        query = "SELECT deptno,dname FROM example_database.dept"
        cursor.execute(query)

        # 4. Fetch and print results
        records = cursor.fetchall()
        #print(records.length)
        for row in records:
            print(f"Data {row['dname']} - {row['deptno']}")

            #print(row)

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # 5. Always close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
