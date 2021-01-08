'''

가위 바위 보 게임 만들기.

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 1     

이겼습니다. ^^

---------------------------

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 1     

졌습니다. ㅜㅜ

------------------------------

=== 가위 바위 보 게임 ===

숫자를 입력해주세요 ( 1. 가위 / 2. 바위 / 3. 보 ) : 1     

비겼습니다. -_-


// 기능 추가 : 컴퓨터가 선택한 숫자 출력.
// 예외처리 : 1, 2, 3 이외의 숫자가 들어가면 에러메시지 출력 후 복귀(게임 지속)
// 'x' or 'X' 를 입력 받으면 종료. x외의 문자 입력시에도 에러메세지 출력후 복귀.
'''
import random

com_num = random.randint(1,3)

try:
    while True:
    my_num = input("숫자 입력 바람(1.가위 / 2. 바위/ 3.보):")
    
     if int(my_num) > 3 or int(my_num) < 1:
         print("1,2,3만 입력가능하니  다시 입력 바람")
         continue

     if my_num == "X" or my_num == "x":
         print("종료")
         break

     if int(my_num) > int(com_num):
        print("이겼습니다. ^^")

     elif int(my_num) < int(com_num): 
        print("졌습니다. ㅜㅜ")
        
     else:
        print("비겼습니다")
     break

    
except ValueError:
    print("잘못 입력하셨으니 다시 입력해주세요")
    

  
        
        
        




        

        

    
    
                  









