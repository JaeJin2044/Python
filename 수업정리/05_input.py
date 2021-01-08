# 05_input.py

'''
    프로그램에서 값을 입력 받고 유동적인 코드를 작성
        (입력된 값에 따라 결과가 달라질 수 있도록)
    표준 입출력 :Standard input/output
        - IDLE이나 콘솔에서 내용을 출력하거나 입력 받는 것

    [사용자 입력 함수 input]
        - input() 함수 사용 -> '입력 대기 상태 ' -> 입력 후 엔터
            -> input() 함수에 의해 입력된 내용이  '문자열'로 변환
'''
print("[input()함수]")

# (1) input()이 사용되면 대기 상태가 된다.
# input()  # 문자열이다.

# input()

# (2) 변수에 대입
'''
input_str = input()
print("입력한 내용:",input_str)
'''

# (3) 바로 사용

# print("입력한 내용2 : ", input())

# (4) input()의 출력 기능

#print("문자열 입력해보세요 : ", end="")
#str1 = input()
#str1 = input("문자열 입력 : ")  # 1. 문자열 입력 출력 --> 출력대기 상태 --> 변수저장

# (5) 숫자 다루기

#print((input("숫자 입력 : ") +10)  # 오류 .. 문자열과 숫자가 연산해서 .. 그럼
'''
input_num = input("숫자 입력 : ")

input_num = int(input_num)
print(input_num+10)
'''

# 입력과 반환 한 번에
'''
input_num = int(input("숫자 입력 : "))

print(input_num+20)
'''

# 여러 값을 한 번에 입력받고 정수로 변환
# split(), map() 이용
my_str = "하 하 하 하 하"
print(my_str.split())

# map() : 특정한 함수 하나를 반복해서 사용할 때
# map(반복수행할 함수의 이름 ,요소가 여러 개인 값

a,b = map(int, ["1","2"])

# a, b = int("1"), int("2")
# a, b = 1, 2
print(a + b)


num1, num2 = map(int, input("두 수 입력 : ").split())  
# 1. 두 수 입력 출력
# 2. 입력은 띄어쓰기로 각각을 입력
#   10 20 입력했다면 "10 20" 문자열로 돌아옴
# num1, num2 = map(int, "10 20".split())
# 3. num1, num2 = map(int,["10","20"])
# 4. num1, num2 = int("10"), int("20")
#    num1, num2 = 10, 20
print(num1 + num2)
print()

# (1) 문자열 입력 
my_str = input("문자 입력:")

# (2) 숫자 하나만 입력
my_num = int(input("숫자 입력:"))

# (3) 여러개의 숫자를 입력 ..   #변수 수만 조절 하면됨 뒤에는 똑같이  입력 ....
num1, num2 = map(int, input("여러개의 숫자 입력 : ").split())



































