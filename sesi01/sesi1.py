print(123123123123123123123123123123123123123123123123 + 1)
print(type(123123123123123123123123123123123123123123123123 + 1))

print("Hacktiv8")
print(type("Hacktiv8"))

print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')

print(True)
print(type(False))
print(100 == 100)
print(100 > 200)

n = 300
print(n)

a = b = c = 20
print(a + b + c)

x = 23.5
print(x)

x = 'Superb'
print(x)

_a = a_ = a1 = b_a = 20
print(_a, a_, a1, b_a)
print(_a - a)
print(a * b_a)
print(a1 / a_)

lis = ['foo', 'bar', 'baz', 'qux']
print(lis)
print(type(lis))
print(lis[0].upper())
print(lis[0].title())
print(lis[0:3])

c = ['foo', 'bar', 'baz', 'qux']
print(c * 2)
c = c * 2
print(c)
c[2] = 3
print(c)
del c[1]
print(c)
c[3:6] = [3, 2, 4]
print(c)

# immutable / tidak bisa di ubah atau edit
n = (1, 3, 5, 7)
print(n)
print(type(n))
# n[0] = 3

dic = {'a': 20, 'b': 30, 'c': [1, 3]}
print(dic['a'])
print(dic.keys())
print(dic['c'][1])

age1 = 20
age2 = 22
age3 = 13

someone_is_of_working_age = (age1 >= 18 and age1 <= 60) or (
    age2 >= 18 and age2 <= 60) or (age3 >= 18 and age3 <= 60)

print(someone_is_of_working_age)

someone_is_of_working_age = (age3 >= 18 and age3 <= 60)
print(someone_is_of_working_age)