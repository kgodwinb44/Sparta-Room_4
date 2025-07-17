# Task 1

---

## 1. Open a file in Python
- Open() also creates the file
``` 
f = open('file_name.txt')
print(f.read())
```
---

## 2. Use Try/Exception blocks to handle errors
- The try block lets you test a block of code for errors. 
- The except block lets you handle the error
```
try:
    f = open('foo_list.txt')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("The file 'food_list.txt' was not found.")
```

---

### 3. What are the different "modes" we can use to open files in Python?

- In Python, there are six different access modes that you can use when working with files such  as 'r', 'w', 'a', 'r+', 'w+', 'a+'
- 'r' - read only
- 'w'- write only
- 'a' - append only
- 'r+' - read + write 
- 'w+' - write + read'
- 'a+' -append + read

---

### 4. Close a file properly after opening it in Python
- close()
```
try:
    with open('food_list.txt', 'r+') as file:
        content = file.read()
        print(content)
        file.close()

except FileNotFoundError:
    print("The file 'food_list.txt' was not found.")
```

---

### 5. Write a small program that will open a text file with food types on each line. Iterate through the food types and output them to the console.
#### 5.1 Use Try/Except blocks to handle errors
#### 5.2 Make sure the output looks clean (each food type is on a new row)
```
try:
    with open('food_list.txt', 'r+') as file:
        file.write('Carbs')
        ## Reset pointers
        file.seek(0)
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file 'food_list.txt' was not found.")
```
---

### 6. What is the "with" statement? Why is it better than "open" usually? Refactor your program to use it.
- With statement in Python is a clean and safe way to work with files. In the sense, you don’t need to remember to call 'file.close' if we use 'with' statement.

---

### 7. How do you write to a file from Python?
#### 7.1 Make a program that writes up a 3 course meal order to a file called "order.txt"
#### 7.2 OPTIONAL BONUS Can make the program (script) idempotent?
````
file = open('my_file.txt', 'w')

file.write('Hello, world!')    

file.close()                     
 
with open('my_file.txt', 'w') as file:
file.write('Hello again!')
````