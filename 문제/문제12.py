# for문 연습
# n의 배수 : 어떤 숫자를 n으로 나눈 나머지가 0   --> num % n == 0 --> num은 n의배수
# 공배수 :    n1과 n2의 공배수 = 둘 다 만족!    num % n1 == 0 and num % n2 == 0
'''
    1. 1부터 입력 받은 수까지 '짝수'의 합 구하기

        [출력결과]
        숫자 입력 : 5
        1~5까지 짝수의 합은 6입니다.
'''



'''
my_num = int(input("숫자 입력:"))
sum1 = 0
for i in range(1,my_num+1):
    if i % 2 ==0:
        sum1 +=i

print("1 ~ {}까지의 짝수의 합은 {}입니다.".format(my_num,sum1))   
'''








'''
    2. 1부터 200까지 3과 4의 공배수를 하나의 변수에 '누적'
       누적된 수가 1000을 초과하면 반복문을 '탈출'
       이때, 누적된 수와 마지막에 더했던 공배수를 출력

        [출력결과]
        누적된 수 : 1092
        더한 수 : 156
'''






''''
sum1= 0


for i in range(1, 201):
    if i % 3 == 0 and i % 4 == 0 :
        sum1+= i
    if sum1 > 1000 :
        Total = sum1
        last = i
        break;

print("누적된수  :",Total)
print("더한수 :" , last)  # 굳이 last 아니라 i 변수로 넣어도 됨 ..

'''







'''
    3. 1~100 사이 정수 중, 3의 배수와 5의 배수를 '역순'으로 출력
       단, 3과 5의 공배수는 <15> 처럼 출력

       [출력결과]
       100 99 96 95 93 <90> 87 ... 5 3
'''



'''
for i in reversed(range(1, 101)):
    if i % 3 == 0 or i % 5 == 0:
        
        if i % 3 == 0 and i % 5 == 0 :
            print("<{}>".format(i))
            continue;
        print("{} ".format(i),end="")
'''







'''
    난이도 <상>
    4. 2중for문 구구단 예제를 for문 1개만 사용해서 만들어보기
        - 총 반복 횟수 = 72회
        - 처음 단은 2
        - 곱해지는 숫자는 처음이 1
        - 9회 수행마다, 단이 1 증가, 곱해지는 숫자는 1로 변경

'''

# 1. 구구단의 단을 저장할 변수
# 2. 구구단의 곱을 저장할 변수
# 3. 72회가 반복되도록 for문 작성
# 4. 곱해지는 숫자가 9가 되었을 때 단 1증가 , 곱해지는 숫자를 1로 변경 (if문)



'''
dan = 2 # 2부터 시작
gob = 1 # 1부터 시작



for i in range(72) :  # 0 ~ 71 (72회 반복)
    print("{} * {} = {} ".format(dan, gob, (dan*gob)))
    gob += 1
    if gob == 10 :
        dan += 1 # 단을 1씩 증가
        gob = 1  # 곱해지는 숫자를 다시 1로 변경

'''






'''
i = 0
j = 0

for i in range (2,10):        
    while j < 9:
        j+= 1
        print("{} X {} = {}".format(i,j,(i*j)))
    j=0
'''






# import (젤 위에다가 만들어 줘야함)
# import random (random이라는 소스파일을 이 파일에 추가하겠다.)


import random
a= 10
b= 100
print(random.randint(10, 100))   # randint 10<= x <= 100  (이상 이하 )

random_num = random.randint(1,100)

print(random_num)

print(random.choice(["!","@","#"]))






















