'''
    4. 재귀함수로 팩토리얼 값 구하기
        팩토리얼(factorial) : 1부터 어떤 수까지 모두 곱한 결과
            5! = 5 * 4 * 3 * 2 * 1
               = 5 * 4!
            3! = 3 * 2 * 1
               = 3 * 2!
            2! = 2 * 1!
            1! = 1

            n! = n * (n-1)!

        [출력결과]
        숫자 입력 : 5
        5! = 120
'''


'''

num = int(input("숫자 입력 :"))

def Cal(num):
    
    result = num * (Cal(num-1))
 


print("{}! = {}".format(num,Cal(num)))
    
    

'''





'''
    5. 로또 번호 추첨기 만들기 !
        - 45개의 숫자들 중 중복되지 않게 6개의 숫자를 가지고 온다.
        - 총 입력한 횟수 만큼 로또 번호를 만들어 준다. 
        - 리스트, 리스트 관련 함수 이용

    [출력결과]
    로또 횟수 입력 : 5
    [10, 16, 19, 23, 27, 31]
    [13, 18, 23, 27, 29, 40]
    [10, 19, 32, 39, 41, 45]
    [2, 8, 9, 10, 19, 24]
    [2, 9, 21, 25, 40, 42]
    

'''

import random

numbers = list(randrange(1,46))
lotto = []

while len(lotto) <6 :
    num = random.choice


input_number = int(input("로또 횟수 입력:"))


























































