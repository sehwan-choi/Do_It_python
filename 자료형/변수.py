a = [1,2,3]
print(id(a))

# 쉬운복사
a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b)

a[0] = 9
print(a)
print(b)

# 깊은복사
# [:]
a = [1,2,3]
b = a[:]
print(id(a))
print(id(b))
print(a)
print(b)

a[0] = 9
print(a)
print(b)

from copy import copy

# copy -> a[:] 와 동일
a = [1,2,3]
b = copy(a)

print(id(a))
print(id(b))
print(a)
print(b)
print(a is b)

a = [1,2,3]
b = a.copy()

print(id(a))
print(id(b))
print(a)
print(b)
print(a is b)

a,b = ('python', 'java')
print(a)
print(b)
print("{0} {1}".format(a,b))
print(f"{a} {b}")

(a,b) = 'python', 'java'
print(a)
print(b)

a,b = 'python', 'java'
print(a)
print(b)

[a,b] = ['python', 'life']
print(a)
print(b)

a = 3
b = 5
print(a)
print(b)
a,b = b,a
print(a)
print(b)