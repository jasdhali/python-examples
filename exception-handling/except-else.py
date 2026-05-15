try:
    file = open("data.txt","r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File read successfully")
finally:
    print("closing resources")
    # This runs even if the file was't found or if an error occurred during reading
    