money = 2000

if money >= 3000:
    print("택시타고 가자!")
else:
    print("걸어가자!")

money = 1000
card = True

if money >= 3000 or card:
    print("택시타고 가자!")
else:
    print("걸어가자!")

if money >= 3000 and card:
    print("택시타고 가자!")
else:
    print("걸어가자!")

if not card:
    print("택시타고 가자!")
else:
    print("걸어가자!")

print(1 in [1,2,3])
print(1 in [11,22,33])
print(1 not in [11,22,33])
print(1 not in [1,2,3])


print('a' in ('a','b','c'))
print('j' in 'python')

pocket = ['paper', 'cellphone','money']
if 'money' in pocket:
    print("택시타고 가자!")
else:
    print("걸어가자!")

pocket = ['paper', 'cellphone','money']
if 'money' in pocket:
    pass
else:
    print("걸어가자!")


pocker = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라!")
    else:
        print("걸어가라!")


if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라!")
else:
    print("걸어가라!")

score = 10
if score >= 50:
    message = "success"
else:
    message = "fail"
print(message)

# 삼항연산자
# 변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
message = "success" if score >= 50 else "fail"
print(message)