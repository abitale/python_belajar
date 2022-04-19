file = open('Hack8_Sample_Text.txt')
file.close()

try:
    f = open("Hack8_Sample_Text.txt", encoding='utf-8')
except FileNotFoundError:
    print("File not Found")

with open("sample.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

with open('sample.txt', 'r') as reader:
    # Read & print the entire file
    print(reader.read())

import sys


def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win' in sys.platform), "This code runs on Windows only."
    print('Doing something.')


try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed')

print('')

try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('os_interaction() function was not executed')
else:
    try:
        with open('sample.txt') as file:
            read_data = file.read()
            print(read_data)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions')