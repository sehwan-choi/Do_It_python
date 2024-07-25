#정수형
a = 123
print(a)
print("정수형 = " + str(a))
print("정수형 = {}".format(a))
print("정수형 = %d" % a)

#실수형
a = 1.2
print(a)
a = -3.45
print(a)
a = 4.24E10
print(a)
a = 4.24E-10
print(a)

#8진수 16진수
# 8잔수를 만들기 위해서는 숫자가 0o, 0O(숫자 0 + 알파벳 소문자 o 또는 대문자 O)
a = 0o177
print(a)

# 16진수를 만들기 위해서는 0x로 시작하면 된다
a = 0xAA
print(a)

#사칙연산
a = 3
b = 7
print("%d + %d = %d" % (a, b, a + b))
print("%d * %d = %d" % (a, b, a * b))
print("%d / %d = %d" % (a, b, a // b))
print("%d %% %d = %d" % (a, b, a % b))
print("%d ** %d = %d" % (a, b, a ** b))