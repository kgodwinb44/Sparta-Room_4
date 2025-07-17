try:
    with open('food_list.txt', 'r+') as file:
        content = file.read()
        print(content)
        file.close()

except FileNotFoundError:
    print("The file 'food_list.txt' was not found.")
