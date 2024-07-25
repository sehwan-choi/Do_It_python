# 딕셔너리란?
# 딕셔너리는 단어 그대로 ‘사전’이라는 뜻이다.
# 즉 "people"이라는 단어에 "사람", "baseball"이라는 단어에 "야구"라는 뜻이 부합되듯이 딕셔너리는 Key와 Value를 한 쌍으로 가지는 자료형이다.
# 예컨대 Key가 "baseball"이라면 Value는 "야구"가 될 것이다.

# -> Key 와 Value를 한 쌍으로 가지는 자료형이다(aka. java Map)

# 딕셔너리 만들 때 주의할 사항
# 1. 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점에 주의해야 한다. 다음 예에서 볼 수 있듯이 동일한 Key가 2개 존재할 경우, 1: 'a' 쌍이 무시된다.
# 2. Key에 리스트는 쓸 수 없다는 것이다. 하지만 튜플은 Key로 쓸 수 있다. 딕셔너리의 Key로 쓸 수 있느냐, 없느냐는 Key가 변하는(mutable) 값인지, 변하지 않는(immutable) 값인지에 달려 있다. 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다.

a = {'name': 'choi', 'phone' : '010-1234-5678', 'birth':'1010'}
print(a['name'])

a = {'list' : [1,2,3]}
print(a['list'])

a = {1:'a'}
a[2] = 'b'
a[3] = 'c'
print(a)

a['abc'] = 123
print(a)

del(a['abc'])
print(a)

a = {1:1, 2:'b', 'a':[1,2,3]}
print(a)
print(a.keys())

for key in a.keys():
    print(key)

print('--')
for value in a.values():
    print(value)

print(a.items())
for t in a.items():
    print(str(t[0]) + ' ' + str(t[1]))

a.clear()
print(a)

a = {'a':1, 2:'b', 'c':[1,2,3]}
print(a)
print(a.get('c'))
print(a.get('999', 'default'))

print('a' in a)
print('aa' in a)

if 'a' in a:
    print("a!")
else:
    print("no a.")

