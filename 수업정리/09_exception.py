# 09_exception.py
'''
    [예외처리]
        개발자가 의도하지 않은 오류 발생에 대한 처리
            > 프로그램 오류가 나면 프로그램이 종료된다.
            (다음 코드는 수행되지 못한다.)

    try, except문

    try:
        기본 수행문(무조건 진입해서 수행)
    except:
        오류 발생 시 수행되는 수행문
'''



'''
try:
    input_num = int(input("숫자 입력 : "))
    print("결과 :", input_num)
except:
    print("숫자를 입력하세요!!")


'''


# (1) try문 : 오류가 발생되는 '예상' 지역
# (2) except문 : 오류 발생 시 '처리' 지역
#   > 오류 발생 시 '오류가 발생한 코드'에서 except문으로 점프한다.
#   오류가 발생하지 않으면 except문은 수행되지 않고 try문이 끝

# finally문 : 마지막에 무조건 수행된는 구문
#   > 정상/오류 구분없이 무언가 마무리할 코드가 있을 때 사용 


'''
try:
    input_num = int(input("숫자 입력 : "))
    print("결과 :", input_num)
except:
    print("숫자를 입력하세요!!")

finally:    # try, except문에 종속 
    print("예외처리 끝!")
'''

# 오류 구분하기

try:
    print(abc)  # abc를 정의 한적이 없음 !!!! 젤 밑에 except 예외 발생 ..
    num1, num2 = map(int,input("두 수 입력:").split())
    print("나눈 결과 :", num1 / num2)   # 0으로 나누면 오류 발생

    my_list = [1, 2, 3]
    index = int(input("인덱스를 입력 (0~2):"))
    try:
        print("값 :", my_list[index])
    except:
        print("try 문 안에 또다른 try의 except문!")

        
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
    
except ValueError:
    print("숫자를 정확히 입력하세요!")
    
except IndexError:
    print("인덱스가 잘못되었습니다.")

except:   # 위에 해당되지 않은 모든 오류에 대한 처리
    print("뭔진 몰라도 오류가 발생!!")


num1, num2 = map(int, input("두 수 입력:").split())

if num2 == 0:
    print("0으로 나눌 수 없습니다.")
else :
    print("나눈 결과", num1 / num2)


    
 


























































    
