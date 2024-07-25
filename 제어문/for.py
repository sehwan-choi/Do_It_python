# for 변수 in 리스트(또는 튜플, 문자열, 집합):
#     수행할_문장1
#     수행할_문장2

for i in ['apple','banana','carrot']:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

a = ([1,2,3,4])
for i in a:
    print(i)

a = "My name is Sehwan"
for i in a:
    print(i)

a = (1,2,3,4,5,6,'a','b','c')
for i in a:
    print(i)

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.

# marks = [90,25,67,45,80]
marks = (90,25,67,45,80)
number = 0;
for i in marks:
    number += 1
    if i >= 60:
        print("%d. %d 점 합격" % (number, i))
    else:
        print("%d. %d 점 불합격" % (number, i))


# 앞에서 for 문 응용 예제를 그대로 사용해서 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않는 프로그램작성

marks = (90,25,67,45,80)
number = 0
for i in marks:
    number += 1
    if i < 60:
        continue
    print("%d번 합격 축하합니다!" % number)

sum = 0;
for i in range(1,11):
    sum += i;
print("sum = %d" % sum)

# 구구단

for i in range(2,10):
    for j in range(2,10):
        print("%2d x %2d = %2d" % (i,j,i*j), end=" ")
    print()


### 리스트 컴프리헨션
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
print(result)

# [표현식 for 항목 in 반복_가능_객체 if 조건문]
result = [num * 4 for num in a]
print(result)

result = [num for num in a if num % 2 ==0]
print(result)

# 여러개도 가능
# [표현식 for 항목1 in 반복_가능_객체1 if 조건문1
#       for 항목2 in 반복_가능_객체2 if 조건문2
#       ...
#       for 항목n in 반복_가능_객체n if 조건문n]
result = [x*y for x in range(2,10)
               for y in range(1,10)]
print(result)
