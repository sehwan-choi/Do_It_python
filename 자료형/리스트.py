#리스트
a = list()
b = []
c = [1, 2, 3]
d = [1, 2, 3, [4, 5, 6]]
e = [1, "2", 3, ["4", 5, "6"]]

print(a)
print(b)
print(c)
print(d)
print(e)

print(e[0] + e[2])
print(e[-1])
print(e[-1][0])
print(e[-1][1])
print(e[-1][2])

print(e[:3])
print(e[3:])
print(e[3][:2])

a = [1,2,3]
b = [4,5,6]

print(a + b)
print(a * 2)
print(b * 2)

print(str(a[0]) + 'hi')

a[1] = 99
print(a)

a[0] = None
print(a)

del a[2]
print(a)

a = [1,2,3,4,5,6,7,8,9]
del a[:3]
print(a)
del a[3:]
print(a)

# 리스트 정렬
a = [1,2,3]
a.append(99)
print(a)
a.extend([8,13])
print(a)
a[0] = 4
a[1] = 9
a[2] = 6
a.sort()
print(a)

a = ['a','z','q']
print(a)
a.sort()
print(a)

a.reverse()
print(a)

print(a.index('a'))
# print(a.index('k'))

a.insert(1,'k')
print(a)
print(a.index('k'))
# print(a[a.index['k']])

a = [1,2,3]
b = [1,2,3]
a.extend(b)
print(a)

a.remove(3)
print(a)

a.remove(3)
print(a)

print(a.pop())
print(a)

print(a.pop(0))
print(a)

print(a.count(1))
print(len(a))

a = [1,2,3]
a += [1,2,3]
print(a)

a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)