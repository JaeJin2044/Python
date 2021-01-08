# 09_exception_Answer.py


import random

while True:
    com = random.randint(1,3)   # 컴퓨터의 숫자
    user = input("숫자를 입력해주세요(1. 가위/ 2. 바위 / 3. 보):")
    # input()으로 문자열로 입력받기
    
    
    if user == "x" or user == "X":
        print("종료하겠습니다")
        break
    try:
        user = int(user)    # int()로 묶었을 때 오류가 발생 -> 숫자가 아닌 문자열
        
        if user > 3 or user < 1 :   # 입력한 값이 1 ~ 3사이가 아닐 때
            print("1 ~ 3사이의 숫자를 입력하세요")
            continue    # 다시 조건식으로 올라간다.
        
        if user == 1:   # 입력한 값이 가위일 때 
            if com == 1:
                print("비겼습니다.")
            elif com == 2:
                print("졌습니다.")
            else:
                print("이겼습니다.")
        elif user == 2: # 입력한 값이 바위 일때
            if com == 1:
                print("이겼습니다.")
            elif com ==2 :
                print("비겼습니다.")
            else:
                print("졌습니다.")
        else:       # 입력한 값이 보 일때 
            if com == 1:
                print("졌습니다.")
            elif com == 2:
                print("이겼습니다.")
            else:
                print("비겼습니다.")
        
    

    except:
        print("잘못 입력하였습니다.")
    
    
    
    
    
