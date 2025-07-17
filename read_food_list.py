meal = "\nstarter\nmain course\ndessert\n"

with open('order.txt', 'a+') as f:
    f.seek(0)
    content = f.read()
    if meal not in content:
        f.write(meal)
        print("3-course meal added to order.txt")
    else:
        print("Meal already in order.txt — nothing added.")


