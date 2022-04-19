from cv2 import boundingRect


def calculate_rect(length, width):
    print('Area: ', length * width)


length = 100
width = 20

calculate_rect(length, width)


def printinfo(name, age):
    print("name: ", name)
    print("age: ", age)


printinfo('priaydi', 13)


def printinfo(name, age=26):
    '''This prints a passed info into this function'''
    print("Name : ", name)
    print("Age  : ", age)
    print("")


# Now you can call printinfo function
printinfo(age=50, name="hacktiv8")


def print_bought_items(name, **bought_items):
    '''Create a function to print which items somebody bought'''
    print('Name: ', name)

    for key, value in bought_items.items():
        print('Key: ', key)
        print('Value: ', value)

    print('')


print_bought_items("Ani",
                   first="eggs",
                   second="sugar",
                   third="salt",
                   fourth="baking powder")
print_bought_items("Ali", first="thread", second="hoop", wheel="needle")

multiply = lambda x, y: x * y
print(multiply(3, 3))

total = 0


def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside Function local total: ", total)


sum(10, 20)
print("Outside function global total: ", total)