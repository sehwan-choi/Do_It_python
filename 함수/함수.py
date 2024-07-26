# 함수의 구조
# def 함수_이름(매개변수):
#     수행할_문장1
#     수행할_문장2

def add(a,b):
    return a+b

a = add(1,2)
print(a)

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
# *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아 튜플로 만들어 준다
def add_many(*args):
    result = 0
    for i in args:
        result +=i
    return result

a = add_many(1,2,3,4,5,6,7,8);
print(a)

def calc1(choice, *args):
    result = 0
    if choice == 'add':
        for i in args:
            result += i
    elif choice == 'sub':
        for i in args:
            result -= i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    else:
        print("calc Fail!")
    return result

r = calc1('add', 1,2,3,4,5,6,7,8,9,10)
print(r)

r = calc1('sub',1,2,3,4,5,6,7,8,9,10)
print(r)

r = calc1('mul', 1,2,3,4,5,6,7,8,9,10)
print(r)

r = calc1('any', 1,2,3,4,5,6,7,8,9,10)
print(r)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='choi',age=3)

# 함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b,a*b  #   두개를 반환한다면?

a = add_and_mul(1,3)
print(a)    #    튜플이 반환된다.

a,b = add_and_mul(1,3)
print('%s %s' % (a,b))  #   위와같이 a,b 로 받으면 각각받을수있다.

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself('홍길동', 20, False)

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a+1
vartest(a)
print(a)

#  함수 안에서 함수 밖의 변수를 변경하는 방법
# 1.return
a = 1
def vartest2(a):
    a +=1
    return a
a = vartest2(a)
print(a)

# 2. global
a = 1
def vartest3():
    global a
    a += 1
vartest3()
print(a)

# lambda
# lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다.
# 우리말로는 ‘람다’라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식

# 아래 lambda식은 이와 같다
# def add(a,b):
#     return a+b
add = lambda a,b:a+b
a = add(1,2)
print(a)