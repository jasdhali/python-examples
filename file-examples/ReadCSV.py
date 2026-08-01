import csv
with open('/home/jaspal/personal/UnemploymentBenefits/WorkSearchLog.csv', 'r') as file:
    #create the csv reader object
    reader = csv.reader(file)

    #Optional: Skip the header row if exists
    header = next(reader)
    print(f"Headers: {header}")
    #Iterate through the remaining rows
    for row in reader:
        print(row)
