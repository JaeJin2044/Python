# 함수 연습
'''
    1. 홀짝 판별기
        함수의 순기능 : 전달된 숫자가 홀수인지 짝수인지 판별
            > 짝수 : Even_umber

            > 반환 값이 있는 형태와 없는 형태로 함수를 2개 만들기
            > 0은 "0입니다"

          1. 숫자 입력
          2. 입력 받은 숫자를 함수의 매개변수로 전달
          3. 함수는 전달 받은 매개변수의 값으로 홀짝 판별

        [출력결과]
        숫자 입력 : 20
        함수1 : 짝수입니다.
        함수2 : 짝수입니다.
'''



'''

# 반환값 매개 변수 둘 다 있는경우
def Cal1 (my_num):
    if my_num == 0:
        result = "0"
    elif my_num %2 == 0 :
        result = "짝수"
    else:
        result = "홀수"
    return result


my_num = int(input("숫자입력:"))

print("함수 1 : {}입니다.".format(Cal1(my_num)))

'''

'''

# 반환값 없는 형태
def Cal2(my_num):
    result = 0
    if my_num == 0:
        result = "0"
        
    elif my_num % 2 == 0:
       result = "짝수"
        
    else:
        result = "홀수"
    print("함수 2: {}입니다.".format(result))

      
my_num = int(input("숫자입력:"))

Cal2(my_num)

      
'''





        





'''
    2. 두 수를 입력 받고, 큰 수에서 작은 수를 뺀 결과 값을 '반환'하는 함수 정의
        - 계산기 : calc
        - 위 내용이 함수의 순기능임
         > 매개변수 2개, 반환 값 있음

        [출력결과]
        두 수 입력 : 1 20
        결과 : 19
'''



'''
def clac(num1,num2):
    if num1 >= num2 :
        return num1 - num2
    elif num2 >= num1:
        return num2 - num1

num1,num2 = map(int, input("두 수 입력 :").split())

print(clac(num1,num2))



'''
    
    










'''
    3. 1~10 사이의 두 수를 입력 받기
       1~100까지 전달된 두 수의 공배수를 출력하는 함수만들기 (반환 X)
        > 매개변수 2개, 반환 값 없음

           [출력결과]
           두 수 입력 : 3 5
           결과 : 15 30 45 60 75 90
'''



def Cal(num1,num2):
    print("결과 : ", end = "")
    for i in range(1,101):
        if i % num1 == 0 and i % num2 == 0:
           print("{} ".format(i), end= "")


num1 , num2 = map(int ,input("두 수 입력:").split())

Cal(num1,num2)








































