# Task 2 – CSV Task: Reading and Transforming CSV Data

---

## 1. Read a CSV file using the `csv` module
```
import csv
# 1
with open('user_details.csv','r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

## 2. Print only emails from the CSV

```
# 2
with open('user_details.csv','r') as file:
     reader = csv.reader(file)
     # Skips header
     next(reader)

     for row in reader:
        print(row[4])
```

---

## 3. How can you skip the headers?
```
with open('user_details.csv','r') as file:
     reader = csv.reader(file)
     # Skips header
     next(reader)

     for row in reader:
        print(row[4])
```

---

## 4. Cast the CSV data to a list and print the list
## 5. Transform the CSV by removing `"title"` and `"gender"` keys
```
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
```

---