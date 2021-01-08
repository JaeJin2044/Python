# while문 연습


'''
    1. 1부터 10까지 합 구하기
        > 1~10까지 증가할 변수
        > 합계를 누적할 변수

    [출력결과]
    1~10까지 합은 55입니다.
'''

'''

my_num = 0
my_sum = 0

while my_num < 10:
    my_num += 1
    my_sum += my_num

print("1 ~ 10까지의 합은 {}입니다.".format(my_sum))

'''









'''
    2. 1부터 입력 받은 수까지 합 구하기
    [출력결과]
    숫자 입력 : 5
    1~5까지 합은 15입니다.
'''



'''

input_num = int(input("숫자입력:"))
my_num = 0
my_sum = 0
while my_num < input_num :
    my_num +=1
    my_sum += my_num

print("1~{} 까지의 합은 {}입니다.".format(input_num,my_sum))    

'''










'''
    3. 구구단 7단 출력하기
        [출력결과]
        7 * 1 = 7
        ...
        7 * 9 = 63
'''


# 단은 고정!
# 곱해지는 숫자는 1 ~ 9까지 (변수 생성)
# while문 작성(1 ~ 9 까지 반복)



'''
num1 = 0
num2 = 7
while num1 < 9 :
    num1 += 1
    print("{} X {} = {}".format(num2,num1,(num1*num2)))
    

'''





'''
    4. 입력 받은 단 출력하기
        [출력결과]
        단을 입력하세요 : 5
        5 * 1 = 5
        ...
        5 * 9 = 45
'''




'''

dan = int(input("단을 입력하세요 :"))
gob = 0
while gob < 9 :
    gob += 1
    print("{} X {} = {}".format(dan,gob,(dan*gob)))

'''




'''
    5. * 찍기
        - 입력된 숫자만큼 아래와 같은 모양으로 별 찍기
        - 조건변수를 증가시키며 문자열 연산을 하면 매우 편하게 출력할 수 있다.

    [출력결과]
    숫자 입력 : 5
    *
    **
    ***
    ****
    *****
'''


'''
my_num= 0
str1 = "*"
num1 = int(input("숫자 입력: "))
while  my_num < num1 :

    my_num += 1
    print(str1*my_num)
    

'''





'''
    6. 숫자 맞추기
        1~100까지 랜덤으로 정답 숫자를 생성
        while문 안에서 숫자를 입력 받고, 숫자가 정답이면 탈출!

    [출력결과] (정답이 70이라고 가정)
    숫자 입력 : 50
    더 큰 수를 입력해보세요.
    숫자 입력 : 80
    더 작은 수를 입력해보세요.
    숫자 입력 : 70
    정답입니다!
    3회만에 맞추셨습니다.   * 심화 : 몇 회 만에 맞췄는지 추가로 출력
'''

# 1. 랜덤한 정답 숫자 생성
# 2. while문 작성 (무한반복)
# 3. while문 안에서 입력 받기 & 판별(정답인지 아닌지)
# 4. 변수 이용해서 몇회 만에 맞추었는지 출력 


import random

random_num = random.randint(1,100)
print("정답미리공개 :{}".format(random_num))
score = 0
while True :
    score += 1
    my_num = int(input("숫자를 입력 하세요:"))
    if my_num > random_num :
        print("더 작은수를 입력해보세요.")
    elif my_num < random_num:
        print("더 큰수를 입력해보세요.")
    else:
        print("정답 입니다!")
        print("{}회만에 정답을 맞추셨네요".format(score))
        break

        




'''
#for문 사용 

random_num = random.randint(1,100)
print("정답 :{}".format(random_num))
for i in range(101):
    i +=1
    my_num = int(input("숫자를 입력 하세요:"))
    if my_num > random_num :
        print("더 작은수를 입력해보세요.")
    elif my_num < random_num:
        print("더 큰수를 입력해보세요.")
    elif my_num == random_num:
        print("정답 입니다!")
        print("{}회만에 정답을 맞추셨네요".format(i))
        break

        
'''
    




















