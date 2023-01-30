x = 'From marquard@uct.ac.za'
print(x[14:17])

print(len('banana')*7)

print(len('banana'))


x = 'some text'

print(str(x.upper()))
print(x)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


t = (1, 2, 3,)
print(t.index(2))

data = [1,2,3]

data.sort(reverse=True)
print(data)