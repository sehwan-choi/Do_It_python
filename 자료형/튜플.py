# 리스트와 튜플
# 리스트는 [], 튜플은 ()으로 둘러싼다.
# 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.

# 프로그래밍을 할 때 튜플과 리스트는 구별해서 사용하는 것이 유리하다.
# 튜플과 리스트의 가장 큰 차이는 요솟값을 변화시킬 수 있는지의 여부이다.
# 즉, 리스트의 요솟값은 변화가 가능하고 튜플의 요솟값은 변화가 불가능하다.
# 따라서 프로그램이 실행되는 동안 요솟값이 항상 변하지 않기를 바란다거나 값이 바뀔까 걱정하고 싶지 않다면 주저하지 말고 튜플을 사용해야 한다.
# 이와 반대로 수시로 그 값을 변화시켜야할 경우라면 리스트를 사용해야 한다.
# 실제 프로그램에서는 값이 변경되는 형태의 변수가 훨씬 많기 때문에 평균적으로 튜플보다 리스트를 더 많이 사용한다.

# 튜플은 요솟값을 변화시킬 수 없다는 점만 제외하면 리스트와 완전히 동일하다

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b', ('ab','cd'))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# 튜플의 요솟값을 지우거나 변경하려고 하면 어떻게 될까?
# 앞에서 설명했듯이 튜플의 요솟값은 한 번 정하면 지우거나 변경할 수 없다. 다음에 소개하는 두 예를 살펴보면 무슨 말인지 알 수 있을 것이다.
#
# 1. 튜플 요솟값을 삭제하려 할 때
a = (1,2,3)
# del a[0]

# 에러 발생
# Traceback (most recent call last):
#   File "/Users/sehwan/python/doItPython/자료형/튜플.py", line 29, in <module>
#     del a[0]
# TypeError: 'tuple' object doesn't support item deletion

# 2. 튜플 요솟값을 변경하려 할 때
a = (1,2,3)
# a[0] = 9

# 에러 발생
# Traceback (most recent call last):
#   File "/Users/sehwan/python/doItPython/자료형/튜플.py", line 39, in <module>
#     a[0] = 9
# TypeError: 'tuple' object does not support item assignment

a = (1,2,'a','b')
print(a[0])
print(a[2])

print(a[:2])
print(a[2:])

t1 = (1,2,3)
t2 = ('a','b','c')
t3 = t1 + t2
print(t3)

t1 = (1,2,3)
print(t1*3)
print(len(t1 * 3))
