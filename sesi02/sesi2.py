a = 1
b = 4

if a < b:
    print("yes")

if b < a:
    print("no")

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')

print('After conditional')

x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break  # Break Statement
    print(n)
print('Loop ended.')

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

for n in range(1, 6):
    print(n)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)
else:
    print("Done")