import csv

# 4
with open('user_details.csv', 'r') as file:
    reader = csv.reader(file)
    # Remove title and gender from each row
    altered_data = []
    for row in reader:
        row.pop(0)
        row.pop(2)
        altered_data.append(row)

    print(altered_data)

with open('altered_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(altered_data)