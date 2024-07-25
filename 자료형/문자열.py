import random

a = "Hello World"
print(a)

a = 'Hello World'  # '로 감싼것과 " 로 감싼것은 같은 문자열을 나타냄
print(a)

# 멀티라인 문자열 "
a = """
hello
my
name
is
hwan"""
print(a)

# 멀티라인 문자열 '
a = '''
hello
my
name
is
hwan'''
print(a)

# 큰따옴표 안에 작은따옴표 포함하기
a = "hello Python's favorte food is perl"
print(a)

# 작은따옴표 안에 큰따옴표 포함하기
a = 'hello "hi!!" nice to meet you'
print(a)

# 작은따옴표 큰따옴표를 역슬래시를 이용하여 문자열에 포함하기
a = 'hello Python\'s favorte food is perl'
print(a)

a = "hello \"hi!!\" nice to meet you"
print(a)

# 문자열 줄바꿈
a = "Life is too shrot\nYou need python"
print(a)

# 이스케이프 코드란?
# 문자열 예제에서 여러 줄의 문장을 처리할 때 역슬래시 문자와 소문자 n을 조합한 \n 이스케이프 코드를 사용했다.
# 이스케이프(escape) 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 ‘문자 조합’을 말한다.
# 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다. 몇 가지 이스케이프 코드를 정리하면 다음과 같다.

# 코드	설명
# \n	문자열 안에서 줄을 바꿀 때 사용
# \t	문자열 사이에 탭 간격을 줄 때 사용
# \\	\를 그대로 표현할 때 사용
# \'	작은따옴표(')를 그대로 표현할 때 사용
# \"	큰따옴표(")를 그대로 표현할 때 사용
# \r	캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
# \f	폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
# \a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
# \b	백 스페이스
# \000	널 문자

# * 이 중에서 활용 빈도가 높은 것은 \n, \t, \\, \', \"이다. 나머지는 프로그램에서 잘 사용하지 않는다.
a = '\\'
print(a)

# 문자열 곱하기
a = "python"
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
print("\'" + a + "\' String length = " + str(len(a)))

# 문자열 인덱스, 슬라이싱
print(a[0] + ", " + a[3])
print(a[0:3])
print(a[:5])
print(a[5:])
print(a[:5] + ", " + a[5:])
a = a[:5] + "," + a[5:]
print(a)

#문자열 포맷팅
a = "I eat %d apples."
print(a % 3)

print("I eat %d apples" % 1)
print("I eat 3 %s" % "banana")

num = 10;
print("I eat %d apples" % num)

print("A %d B %d C %d" % (1, 2, 3))

#문자열 포맷 코드
# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)

print("Error is %d%%" % 10)

print("%10s" % "hi")
print("%-10s" % "hi")

print("%0.4f" % 3.141592)
print("%0.4f" % 3.14)

print("I eat {0} apples".format(3))
print("i atr {0} apples. so I was sick for {1} days".format(3, 10))
print("i atr {number} apples. so I was sick for {day} days".format(number=3, day=10))
print("i atr {0} apples. so I was sick for {day} days".format(3, day=10))

print("{0:<10}".format("abcdefg"))
print("{0:?<10}".format("abcdefg"))

print("{0:>10}".format("abcdefg"))
print("{0:!>10}".format("abcdefg"))

print("{0:^10}".format("abcdefg"))
print("{0:=^10}".format("abcdefg"))

print("{0:0.4f}".format(3.141592))
print("{0:10.4f}".format(3.141592))

print("{name} {{name}}".format(name="hi"))
name = "홍길동"
age = "29"
print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다")

d = {'name': '홍길동', 'age': 20}
print(f"나의 이름은 {d['name']} 입니다. 나이는 {d['age']} 입니다")

a = "hi"
print(f'{"hi":<10}')
print(f'{a:!<10}')

print(f'{"hi":>10}')
print(f'{a:?>10}')

print(f'{"hi":^10}')
print(f'{a:=^10}')


#문자열 관련 함수
a = "hobby"
print(a.count('b'))
print(len(a))
print(a.count('o'))
print(a.count('q'))
print(a.count('h'))

print(",".join("abcd"))
print("abcd".join(",,,,"))
print("abcd".upper())
print("abcd".lower())
print(" abcd ".lstrip())
print(" abcd ".rstrip())
print(" abcd ".strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

d = a.split()
print(d[0])
print(d[1])
print(d[2])
print(d[3])


