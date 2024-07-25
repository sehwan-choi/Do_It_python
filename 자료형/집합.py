s = set([1,2,3])
print(s)

s = set("hello")
print(s)

s = set()
print(s)

s = set([1,3,5,6,'a','c',1,1])
print(s)

l = list(s);
print(l)
print(l[0])


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print(s1&s2)
print(s1.intersection(s2))

# 합집합
print(s1|s2)
print(s1.union(s2))

# 차집합
print(s1-s2)
print(s1.difference(s2))

print(s2-s1)
print(s2.difference(s1))

s1.add(99)
print(s1)

s1.update(set([11,22,33]))
print(s1)

s1.remove(11)
print(s1)

s1.remove(22)
print(s1)
