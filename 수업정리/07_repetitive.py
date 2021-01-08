# 07_repetitive.py


'''
    [반복문]
        조건에 만족하면 수행한다 (조건문과 동일)
            > 단, 조건에 만족하지 않을 때 까지

        1. while문
            - 조건식이 참이면 수행문 수행
            - if문과 기본 구조가 동일
                > if문     : 조건이 참이면 수행하고 끝
                > while문  : 조건이 참이면 수행하고 다시 조건식을 비교

    [while문 기본 구조]
    while 조건식:
        수행문
        수행문

'''


print("[while문]")

num = 0

while num < 3:
    print("num = {} ".format(num))
    num += 1 # num = num + 1

# (1) num = 0, 0 < 3 만족하여 수행 (출력 및 num 1 증가)
# (2) num = 1, 0 < 3 만족하여 수행 (동일)
# (3) num = 2, 2 < 3 만족하여 수행 (동일)
# (4) num = 3, 3 < 3 만족하지 않아서 끝

# while문 수행 순서
# 조건 비교 -->  (만족) 수행 --> 비교 --> (만족)수행.... --> 계속해서 반복
# 강제종료 control c 

'''
num = 0

while num < 3:
    print("num = {} ".format(num))      

'''




'''
    (1) 무한반복
    처음 반복문과는 다르게, num의 값을 수행문에서 증가시키지 않았다.
    조건식에서 비교 대상인 num의 값이 계속 동일하기 때문에
    항상 조건이 만족하여 반복문이 끝나지 않는다. --> 무한 반복 현상
    Ctrl + C : 강제 종료

    (2) 조건변수
    num과 같이 조건식의 비교에 사용되는 변수를 '조건변수'라고 한다.
    반복문에서 이 조건변수를 다루는게 매우 중요!!
    조건변수를 어떻게 다루었는지에 따라 반복 횟수가 정해진다.

    조건변수는 조건식에서 그 값이 '사용'되기 때문에 미리 생성된 변수여야한다.

    초기 값(조건변수 생성)
    while 조건식 : (조건변수 사용)
        수행문 (반복해서 수행하고 싶은 코드 + 조건변수의 변화식)

'''

# 반복 횟수 지정
'''
count = int(input("반복할 횟수 입력 :")) #조건변수 생성

while count > 0 :   # 조건변수 사용
    print("count = ", count)
    count -=1    # count = count -1 (조건변수의 변화식)
'''

# 특정 조건 만족(종료)
# x를 입력하면 종료
'''
input_str = 0 # 조건변수 생성 

while input_str != "x":
    input_str = input("x를 입력하면 종료:")  # 조건변수의 변화식

'''


'''
    반복문 공통
        - break문 : 반복문을 빠져나간다. (탈출)

        - continue문 : 반복문의 첫 문장으로 돌아간다.
                        다음 식으로 이동

'''

# break 사용 (반복문 종료)
'''
while True : # 항상 만족 --> 무한반복
    input_str = input("x를 입력하면 종료: ")
    
    if input_str == "x":
        break
'''




print("="*50)
# continue 사용 (while문의 조건식으로 점프)

num = 1 # 조건변수 생성
while num < 10 :      # num의 값이 10보다 작을 때 수행
    if num % 2 == 0:  # 짝수일 때 수행 
        num += 1      # 수행문이 끝날 때 하던 코드를 추가로 작성  
        continue      # 수행문이 끝나는 지점 (조건식으로 올라간다)

    print("num=",num)
    num += 1
    # 원래 수행문이 끝나는 지점

print("num의 값? :",num)



'''
    2. for문
        - 리스트, 튜플, 문자열 등 요소가 나열된 형태의 값을 첫 요소부터 마지막 요소까지
          변수에 대입하여 반복

    [for문 기본 구조]
    for 변수 in 요소가 여러개인 값:
        수행문
        수행문
'''

# in 의 사용
# if : 포항 되어 있는지 확인하여 True/False
# for : 하나씩 대입한다.

# 범위 지정 반복문

for z in [1, 2, 3]: # 요소를 변수에 대입하기 때문에 이 때 생성
    print("z = " ,z)

print("끝! z = " ,z)

for z in "대한민국" :  # 문자열의 한 요소씩 대입(한 문자씩 대입)
    print("z = ",z)
    
print("끝! z = ",z)

# 꼭 변수를 사용해야만 하는건 아니다.
for z in [1, 2, 3, 4, 5]:
    print("하하")

print("===="*10)

# for문을 사용할 때 일반적인 사용법
# range() : 지정한 범위만큼의 숫자들을 반환

for i in range(10):     # 0~9까지 순서대로 i에 대입
    print(i)


'''
    range(10)  : 0 ~ 9
    range(5)   : 0 ~ 4
        > 값을 하나만 넣으면 시작은 0, 끝은 포함X

    range(1,10) : 1 ~ 9 (끝은 포함x)
    range(10, 50 ) : 10 ~ 49
    
    range(1, 10, 2) : 1 ~ 9 값이 2씩 증가 --> 1, 3, 5, 7, 9
    range(10, 0, -1) :  10~ 1 까지 1씩 감소 

    reversed(range(10)) :  0 ~ 9를 뒤집는다 --> 9 ~ 0

'''

# for문으로 1 ~ 10까지 합 구하기
print()
my_sum = 0   # 합계누적용 변수 생성

for i in range(1, 11):# 1 ~ 10까지 대입
    
    my_sum +=i # my_sum = my_sum + i
print("1 + 10까지의 합 :",my_sum)

'''
    my_sum = my_sum + i
    my_sum =  0 + 1
    my_sum =  1 + 2 
    my_sum =  3 + 3
    my_sum =  6 + 4
            .
            .
            .
    my_sum = 45 + 10
    my_sum = 55
'''
'''
# 입력하는 횟수만큼 반복

count = int(input("반복 횟수 입력 : "))

for i in range(count,0,-1):
    print(i)
print()


for i in reversed(range(1, count+1)):
    print(i)
print()

'''

print("========================")
# for문 활용 (1)

# 손님리스트 : 이름, 나이

guest_list = [["홍길동", 20], ["이몽룡", 19], ["성춘향", 17], ["김철수", 29] , ["임꺽정", 22]]

num = 0

for guest in guest_list :  # 5회 반복
    print(guest)
    num += 1 
    name = guest[0]
    age = guest[1]

    print("{}번 손님입장".format(num))
    if age > 19 :
        print("{}님은 성인입니다. 입장!".format(name))
    else :
        print("{}님은 미성년자입니다. 집에서 노세요!!!".format(name))

    # for문에서의 continue
    if age < 20 :
        print()
        continue

    print("{}님은 성인입니다. ({}세)".format(name,age))
    print()


# for문 활용 예시 (2)
# 구구단 출력 - for문 수행문안에 또 다른 for문이 중첩된 2중 for문

for i in range(2,10) : # 단 2: 9
    # i 에 2가 대입된 상태로 'i의 for문'이 수행
    # 'i의 for문'의 수행문에 또 다른 'j의 for문'이 수행된다.
    #   >> i의 for문이 전체 수행되고 끝이 나야 i가 2일때 수행 1회가 끝이난다.

    # i에 3대입후부터 쭉 위 내용이 반복 (i에 9가 대입될때까지)
    for j in range(1, 10):
        print("{} X {} = {}  ".format(i,j,i*j),end="")

    print()
print()

# 3중 for문


for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1,4):
            print(i, j, k)





# import (젤 위에다가 만들어 줘야함)
# import random (random이라는 소스파일을 이 파일에 추가하겠다.)


import random
a= 10
b= 100
print(random.randint(10, 100))   # randint 10<= x <= 100  (이상 이하 )

random_num = random.randint(1,100)

print(random_num)

print(random.choice(["!","@","#"]))



   
    



















































 
    
    




    




          
















    
    
    


        
