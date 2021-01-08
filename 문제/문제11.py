# 조건문 연습
'''
    1. 나이를 입력 받고 아래 조건에 맞게 출력
        7세 이하 : 아동입니다.
        8세~19세 : 청소년입니다.
        20세~64세 : 성인입니다.
        65세 이상 : 노인입니다.
    [출력결과]
    나이 입력 : 15
    청소년입니다.
'''








'''

# 1. 나이 입력 받기 
age = int(input("나이 입력 : "))

# 2. 조건문
if age < 8 and age >= 0: # 0 ~ 7
    print("아동입니다.")
elif age < 20 and age >= 8: # 8 ~ 19
    print("청소년입니다.")
elif age < 65 and age >= 20: # 20 ~ 64
    print("성인입니다.")
elif age >= 65:
    print("노인입니다.")
else:
    print("잘못 입력하였습니다.")
'''







'''
    2. 주민등록번호 남/녀 판별기
        주민등록번호를 010101-3456789 형태로 입력 받고,
        7번째 숫자에 따라 "남자" 또는 "여자" 출력
            9, 1, 3, 5, 7 : 남자
            0, 2, 4, 6, 8 : 여자

    [출력결과]
    주민등록번호 입력 : 010101-3456789
    남자

        >> 입력받은 주민등록번호를 바로 정수로 변환하면 안 됨...
            jumin = int(input("주민등록번호 입력 : "))
            이렇게 시작하면 큰 일 난다...
'''






'''


jumin = (input("주민등록 번호 입력:"))

num = int(jumin[7])

#조건문 만들기

#   1) in 연산자 이용

if num in [1,3,5,7,9]:
    print("남자")
else :
    print("여자")

#   2) or 연산자 이용

#  if jumin == 1 or jumin ==3 or jumin ==5 or   ... .


if (num % 2 != 0) :
    print("남자")
elif (num %2 ==0):
    print("여자")

    
#jumin = input("주민등록번호 입력 : ")
jumin = "010101-3456789" # int()를 쓰지않고, input()만 하면 문자열




'''







'''
    3. 3개 과목의 점수를 입력 받고, 평균 점수에 따라 합격/불합격 출력
        - 평균 60점 이상 합격
        - 평균 점수는 소수점 첫 번째 자리까지만 출력
        - 합격일 때, 65점 미만이면 "턱걸이하셨네요~~!"를 추가로 출력        

    [출력결과]
    세 과목 점수 입력 : 60 60 61
    당신은 60.3점으로 합격입니다.
    턱걸이하셨네요~~!
'''








'''

score1,score2,score3 = map(int, input("세 과목 점수 입력 :").split())

Total_Avg = (score1+score2+score3)/3

if Total_Avg >=60 :
    print("당신은 {:.1f}점으로 합격입니다.".format(Total_Avg))
    if Total_Avg <65 :
        print("턱걸이 하셨네요~~!")

else :
    print("불합격 입니다.")



'''















'''
    4. 세가지 수를 입력 받아 가장 큰 수를 출력하기 

    [출력결과]
    세 수 입력 :20 34 32
    제일 큰 수 :34
'''




'''
num1, num2, num3, = map(int,input("세 수 입력:").split())

if num1 > num2 and num1 > num3 :
    print("제일 큰 수 : {}".format(num1))

elif num2 > num1 and num2 > num3 :
    print("제일 큰 수 : {}".format(num2))
elif num3 > num1 and num3 > num2 :
    print("제일 큰 수 : {}".format(num3))

'''


'''
num1 ,num2, num3 = map(int,input("세 수 입력 :").split())
result  = 0

if num1 > num2 :
    if num1 > num3 :
        result = num1
    else :
        result = num3

elif num2 > num3 :
    result = num2

else :
    result = num3

print("제일 큰 수 :",result)


'''










'''
    5. 똑똑한 계산기
        - 2개의 숫자와 연산할 기호를 입력 받고 결과를 출력하기
            (1) 계산할 2개의 숫자를 입력 받기
            (2) 연산할 기호를 입력 받기
            (3) 연산 기호에 맞는 결과를 출력

     [출력결과1]
     2개의 숫자를 입력하세요 : 10 3
     연산할 기호를 입력하세요(+,-,*,/) : +
     결과 : 10 + 3 = 3
     
     [출력결과2]
     2개의 숫자를 입력하세요 : 10 3
     연산할 기호를 입력하세요(+,-,*,/) : /
     결과 : 10 / 3 = 3.3
'''



'''
num1 , num2 = map(int,input("2개의 숫자를 입력 하세요 :").split())
str1 = input("연산할 기호를 입력하세요(+,-,*,/) :")


if "+" ==  str1 :
    print("결과 : {} {} {} = {}".format(num1,str1,num2,(num1+num2)))
          
elif "-" == str1 :
    print("결과 : {} {} {} = {}".format(num1,str1,num2,(num1-num2)))

elif "*" == str1 :
    print("결과 : {} {} {} = {}".format(num1,str1,num2,(num1*num2)))

elif "/" == str1:
    print("결과 : {} {} {} = {:.1f}".format(num1,str1,num2,(num1/num2)))
else :
    print("연산 기호를 잘못 입력 하셨으니 다시 입력해주세요!!!")
    


'''






'''
    6. 강남마켓 장바구니
        - 장바구니 가격을 입력받고, 금액에 따라 할인율 적용
            > 10,000원 이상 	: 5%
            > 50,000원 이상 	: 10%
	    > 100,000원 이상 	: 20%

    [출력결과1]
    총 구매액을 입력해주세요 : 50000
    최종 결제액은 45000원 입니다.

    [출력결과2]
    총 구매액을 입력해주세요 : 5000
    최종 결제액은 5000원 입니다.
    10000원 이상 구매 시 할인되니 많이 사주세요^^ 

'''






'''
price = int(input("금액을 입력해주세요:"))


if price >= 100000 :
    print("최종 결제액은 {}원 입니다.".format(int(price*0.80)))

elif price >= 50000:
    print("최종 결제액은 {}원 입니다.".format(int(price*0.90)))

elif price >= 10000:
    print("최종 결제액은 {}원 입니다.".format(int(price-(price*0.05))))
else :
    print("최종 결제액은 {}원 입니다.".format(int(price)))
    print("10000원 이상 구매시 할인되니 많이 사주세요^^")
    
    
'''











      
'''
    7. input으로 정수 하나를 입력받고 입력값이 4의배수이면,
	4의 배수입니다. 출력, 아니면 4의 배수가 아닙니다 출력.
	
'''




'''

num = int(input("정수입력 해주세요:"))

if num%4 == 0 and num !=0:
    print("4의 배수입니다.")
else:
    print("4의 배수가 아닙니다.")
          
'''











'''
    8. 비만도 계산기(BMI 지수) 만들기

    BMI 지수 계산법 = 체중(kg) / 키(m) * 키(m)
    예) 키 170cm(미터로 계산), 몸무게 75kg인 사람의 BMI 지수 계산
        1.70 * 1.70 = 2.89
        75 / 2.89 = 25.95

        1) 키와 몸무게 입력 받기
        2) BMI 지수 출력 (소수점 2자리까지)
        3) BMI 지수(체질량 지수)에 따른 비만도 출력
            BMI지수(체질량 지수)

    저체중		18.5 미만

    정상체중		18.5이상 22.99 이하

    과체중 		23.0 이상

  - 위험체중	23.0 초과 24.99 이하

  - 비만 1단계	25.0 이상 29.99 이하

  - 비만 2단계	30.0 이상 39.99 이하

  - 비만 3단계	40.0 이상

    [출력 결과]
    키(신장) 입력 :170
    몸무게 입력 :75
    결과 : BMI 지수 25.95
    비만 1단계
'''
num1 = int(input("키(신장) 입력 : "))
num2 = int(input("몸무게 입력 : "))
num1 = num1 * 0.01
BMI = num2 / (num1 ** 2)
print("결과 : BMI 지수 {:.2f}".format(BMI))

if BMI < 18.5:
    print("저체중")
elif BMI < 23.0:
    print("정상체중")

elif BMI == 23.0:
    print("과체중")
elif BMI < 25.0:
    print("위험체중")
elif BMI < 30.0:
    print("비만 1단계")
elif BMI < 40.0:
    print("비만 2단계")
else:
    print("비만 3단계")















