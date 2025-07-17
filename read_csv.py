import csv
# 1
with open('user_details.csv','r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# 2
with open('user_details.csv','r') as file:
     reader = csv.reader(file)
     # Skips header
     next(reader)

     for row in reader:
        print(row[4])

# 3
with open('user_details.csv', 'r') as file:
    reader = csv.reader(file)
    data_list = list(reader)
    # Lists of lists
    print(data_list)


