# 06_conditional.py

'''
    제어문 - 조건문, 반복문
        >코드를 상황에 따라 제어한다. (프로그램의 흐름을 제어한다.)

    [조건문]
        조건을 판단하여 상황에 맞게 처리

        if 문 - 만약 , ~~면
            '만약' 조건에 만족하면 수행해라 !!
                만족한다 = True
                만족 x = False
    


'''
# True
# False는 실행 안됨
'''
if 3 > 0 :
    print("3은 0보다 크다 ")
    print(3>0)
    print(3<0)
print("If문!")    #위에 출력문이랑 별개의 문장이다 ..
'''
'''
    [if문 기본 구조]
    if 조건식 :
        수행문
    elif 조건식 :
        수행문
    elif 조건식 :
        수행문
    else:
        수행문
        
    1. 조건식
        참(True)이나 거짓(False)이 있어야 한다.
        조건식의 끝에는 콜론(:)을 붙인다. (콜론이 있으면 조건식이 끝)
        콜론(:) 뒤부터는 수행문으로 간주한다.
        ex) if 3 > 0 : print("3은 0보다 크다") 수행문이 1개일때는 한 줄도도 가능!!

    2. 수행문
        조건식이 만족할 때 수행하는 코드들
        반드시 '들여쓰기'를 해야 한다. --> 공백 4개로 한다.
        수행문 코드 간의 들여쓰기가 맞지 않으면 오류가 난다.

        들여쓰기만 맞으면 수행문을 여러 줄 작성할 수 있고
        들여쓰기를 끝내면 if문의 수행문이 끝난 것

    3. elif 조건식 : (else if) 다른 만약
        위 조건식이 만족하지 않으면 이 조건식은?
        if문에 종속된다. (if문 없이 바로 사용할 수 없다.)
            > 조건문의 시작은 무조건 if문으로 시작
        여러 개 사용 가능
        경우의 수가 늘어남

    4. else :
        위 조건식이 만족하지 않으면 '무조건' 여기를 수행해라 !
            > 조건식이 없다.
        if문에 종속
        하나만 사용할 수 있다.

        > if문 밑에 elif나 else가 종속된 경우 '하나의 조건문'
        > if문, elif, elif, else 이 구조의 조건문은 '조건식' 4개
            >> 하나의 조건문에 조건식이 4개이다.
            >> else는 조건식이 없다. 하지만 '무조건'도 하나의 조건이 된다.

'''

print()

'''

num = int(input("숫자를 입력 해주세요: " ))

#하나라도 조건식을 만족하면 그 수행문을 수행한 후 '조건문'을 빠져나간다.

if  (num > 0):
    print("양수입니다")
    
elif (num <0) :
    print("음수입니다.")
elif num==0 :               # 비교연산자 기호 중 == 기호는 같은지 비교 
    print("0입니다.")
    
else :  # 연산없이 무조건 진입 (효율적)
    print("0입니다.")
'''

# if문 중첩
#   > if문의 수행문 안에 또 다른 if문을 작성하는 것
'''

score = int(input("점수 입력:"))


if score >= 60 :            #크거나 같으면 
    print("합격입니다.")
    
    if score == 100:
        print("만점입니다.")
    
    print("축하합니다.")
    
else:
    print("불합격입니다.")

'''

'''
    [비교연산자]
        조건식에 자주 사용되는 연산자
        조건에 만족하면 결과 값이 True 아니면 False
        a < b a가 b보다 작냐?
        a > b a가 b보다 크냐?
        a <= b a가 b보다 작거나 같냐?
        a >= b a가 b보다 크거나 같냐?
        a == b a와 b가 같나?
        a != b a와 b가 다르냐?
'''

'''
    [논리연산자]
        a or b      a 또는 b중에 하나라도 참이면 참 / 둘 다 거짓이어야 거짓
       (a || b )
       
        a and b     a 와 b 둘다 참이어야 참  / 둘 중 하나라도 거짓이면 거짓 
       (a && b )

        not a       a가 거짓이면 참 / 참이면 거짓 (참과 거짓을 뒤집는다.)
        (!a)

'''

'''
    [포함연산자]
        a in b      b안에 a가 있으면 참 / 없으면 거짓
        a not in b   b안에 a가 없으면 참 / 있으면 거짓

        > b에는 요소가 여러 개인 자료형의 값이 위치한다. (리스트, 튜플, 문자열 등)

        ex) if 4 in [1, 2, 3, 4] : print("4")

        "A" in ["A", "B"] --> True
        "A" in "AB"       --> True
        "A" in ["AB", "ABC"] --> False
'''

# and : 좌우측이 둘 다 True일 때만 결과가 True

num1 = -10
num2 = -20

if num1 > 0 and num2 > 0 :
    print("둘 다 양수입니다.")

elif num1 < 0 and num2 < 0 :
    print("둘 다 음수입니다.")

print()

# or : 둘 중 하나라도 True이면 결과가 True이다.

num1 = 1
num2 = -1

if num1 > 0 or num2 > 0 :
    print("둘 중 하나는 양수")

if num1 < 0 or num2 < 0 :
    print("둘 중 하나는 음수")


print()

# not : 참과 거짓을 반대로

if not num1 > 0:
    print("첫 번째 숫자는 양수가 아니다.")



# in, not in

num1 = 1
num2 = 10
my_list = [1, 2, 3]

if num1 in [1, 2, 3] :
    print("첫 번째 숫자는 1, 2, 3 중에 있다.")

if num2 not in my_list :
    print("두 번째 숫자는 {} 중에 없다.".format(my_list))


print()


if (num1 in my_list) and (num2 in my_list) :
    print("둘 다 1, 2, 3 중에 있다.")

if (num1 in my_list) or (num2 in my_list):
    print("둘 중 하나는 1, 2, 3 중에 있다.")

    
    

    
    



        


        





        
        
















        

    
    
    
    

            


    
