# 자료형의 참과 거짓

# 값	참 or 거짓
# "python"	참
# ""	거짓
# [1, 2, 3]	참
# []	거짓
# (1, 2, 3)	참
# ()	거짓
# {'a': 1}	참
# {}	거짓
# 1	참
# 0	거짓
# None	거짓

print(type(list[1,2,3]))
print(type(set([1,2])))
a = {'a':1}
print(type(a))
print(type(True))
print(1>2)
print(1<2)

a = [1,2,3,4,0]
while a:
    print(a.pop())

if []:
    print("true")
else:
    print("false")

if [1,2,3]:
    print("true")
else:
    print("false")


if ():
    print("true")
else:
    print("false")

if (1,):
    print("true")
else:
    print("false")

if ([]):
    print("true")
else:
    print("false")

if ([1,2,3]):
    print("true")
else:
    print("false")

print(bool('python'))
print(bool([]))