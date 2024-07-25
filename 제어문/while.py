# while 조건문:
#     수행할_문장1
#     수행할_문장2
#     수행할_문장3

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d 번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")


prompt = """
1. Add
2. Del
3. List
4. Quit"""

number = 0
# while number != 4:
while False:
    print(prompt)
    number = int(input())


coffee = 10
money = 300
while money:
    print("커피 주문완료")
    coffee -= 1
    print("남은 커피 수 %d" % coffee)
    if coffee == 0:
        print("남은 커피가 없습니다.")
        break;

coffee = 10
# while True:
while False:
    money = int(input("돈을 넣어주세요: "))

    if coffee == 0:
        print("커피가 없습니다.")
        break;
    elif money < 300:
        print("잔액이 부족합니다.")
    elif money >= 300:
        coffee -= 1
        print("커피 주문 완료!")
        print("잔여 커피 %d 거스름돈 %d" % (coffee, money - 300))
    else:
        print("커피 주문에 실패하였습니다.")

a = 0
while a < 10:
    a +=1
    if a % 2 == 0:
        continue
    print(a)

