#03_type1.py

'''
    [data type] : 자료형
            >어떠한 값의 형태

            [1.숫자형(Number)]
                정수        : -123, 0 ,123
                실수(소수)  : -1.23, 10.1323
                2진수(binary): 0b10, 0B10,     0B(대소문자 다가능 (이것을 적고 뒤에 값 작성..)
                8진수(octal) : 0o10, 0O10      위와 같은 맥락 ...
                16진수(hexadecimal) : 0x10,0X10


10진수(0~9) :  0  1  2  3  4  5  6  7  8    9  10  11  12  13  14  15  16
8진수 (0~7) :  0  1  2  3  4  5  6  7  10  11  12  13  14  15  16  17  20
16진수(0~9) :  0  1  2  3  4  5  6  7  8    9   a   b   c   d   e   f  10  11  12                    
     (a~f)
2진수 (0,1) : | 128 |   64 |  32 |   16  |  8 |   4 |   2 |   1 |
               2^8                                   2^2      2^1     
                 0      0      0    0      0     0     0     0  = 10진수의  0
                 0      0      0    0      0     0     0     1  = 10진수의  1
                 0      0      0    0      0     0     1     0  = 10진수의  2
                 0      0      0    0      0     0     1     1  = 10진수의  3
                 0      0      0    0      0     1     0     0  = 10진수의  4
                 0      0      0    0      0     1     0     1  = 10진수의  5
                 0      0      0    0      1     0     1     0  = 10진수의  10

===> 이런식으로 표현한다 ..!!
2진수의 최솟값은 0      0      0    0      0     0     0     0
2진수의 최댓값은 1      1      1    1      1     1     1     1

0~255가지를 표현 가능 = 256
2진수의 값을 10진수로 바꾸는 것읕 조금 익숙해 둘 필요가 있다..


2^8=256
==>256가지의 수를 표현할 수 있다. 

0=X 사용하지 않겠다.  EX)전원버튼    
1=O  사용하겠다

bit(컴퓨터의 최소단위) : 0또는 1을 저장할 수 있는 크기를 나타냄
8bit = 1Byte
1024Byte= 1KB
1024KB = 1MB
1024MB = 1GB
1024GB = 1TB


'''
print("======================================================================")
print("1. 숫자형")
print("======================================================================")
print("[기본 숫자형]")
print("정수 : ",-10,0,123)
print("실수 : ", -1.11 , 10.12)

#print()함수는 숫자를 10진수로 출력해준다 ..
print("2진수 : " , 0b10, 0B10)
print("8진수 : " , 0o10, 0B10)
print("16진수 : " , 0x10,0X10)
print()


'''
    사칙연산 : + - * /
    제곱연산 : **
    나머지연산 : %
    몫 연산 : //

'''

print("[숫자 연산하기]")
#연산자: 연산을 수행하는 '기호'
#피연산자 : 연산자의 작업 대상
#연산을 수행한다 = 피연사자를 이용하여 '하나의 값'을 만든다.


num1 = 10
num2 = 3

print("num1+num2 = " ,(num1+num2))
print("num1-num2 = " ,(num1-num2))
print("num1*num2 = " ,(num1*num2))
print("num1/num2 = " ,(num1/num2))
print("num1//num2 = " ,(num1//num2)) #소수점을 버린다 ....정수의 값만 출력 
print("num1%num2 = " ,(num1%num2))
print("num1**num2 = " ,(num1**num2))

#나머지 연산 % 중요!!!!

# 두 수를 나누고 나머지 값만 사용
# 12 를 3으로 나눈 나머지가 0이면 12는 3의 배수이다.
# 어떤 수를 2로 나눈 나머지가 0 이라면 ... ==> 짝수다  , 만약 나머지가 1이면 홀수
print()

'''

    [2. 문자형(String)]
        "abc"
        'abc'
            -->따옴표로 둘러싸이면 문자열이다.
        문자열을 만드는 방법
            1. 큰 따옴표 1개
            2. 작은 따옴표 1개
            3. 큰 따옴표 3개
            4. 작은 따옴표 3개
'''
print("================================================")
print("2.문자형")
print("================================================")

print("[문자열 만드는 4가지 방법]")
print("1. happy day")
print('2. happy day')
print("""3. happy day""")
print('''4. happy day''')

print()

print("[각 방법들의 사용 용도]")

# 아이유 : "파이썬 재밌다!!"

#print("아이유 : "파이썬 재밌다!!"") # 오류 !!

print('아이유 : "파이썬 재밌다!!"')
print("아이유 : '파이썬 재밌다!!'")

'''
    이스케이프 문자
        - '문자열' 안에서 특수한 기능을 가지는 문자
        - 역슬래시 (\)로 시작
            \n : 개행(줄바꿈)
            \t : tan 키 만큼 간격 띄우기
            \\ : \하나를 문자로 사용
            \' : '하나를 문자로 사용
            \" : "하나를 문자로 사용
'''

#이스케이프 문자 삽입

print("아이유 : \'파이썬 재밌다!!\"")
print()

#여러 줄의 문자열을 다루기 ---> 3개짜리 사용

print("""안녕하세요
파
이
썬입니다.""")


hello = ''' 반가워
파이썬!'''


print(hello)

#문자열과 주석은 같은 것
'''
    설명~~~!
'''

# 파이썬이 주석(문자열)을 읽긴 하지만 영향이 없다.
print()


'''
    문자열 연산하기
        1. +    : 연결
        2. *    : 반복
'''

print("[문자열 연산하기]")

# +

print("안녕"+"하세요")

Str1 = "안녕"
Str2 = "하세요"

print(Str1+Str2)
print()
# *
print("안녕"*3)

#곱셈도 연산--> 하나의 값을 만든다.
#문자열 곱셈 연산의 결과가 "안녕안녕안녕"이고 이걸 출력 !!!

Str3 = "hi" *5  #연산 결과를 만든 후 변수에 대입

print(Str3)
print()

print("="*50)
print("1. 제목~!!")
print("*"*50)
print()

'''
    문자열 인덱싱
        - 인덱싱(Indexing) : index 색인, 무언가를 가리킨다.
        - 문자열에서 특정 글자를 뽑아내어 사용하는 것
            > 특정 글자를 찾을 때 , '순서'를 사용 -> 인덱스
            > 순서는 0 부터 시작
            > 음수는 뒤에서 부터 순서를 센다 .
'''
print("[문자열 인덱싱]")
# 서두르지도 말고 , 쉬지도 마라 - 괴테 
my_str = "Without haste, but without rest."#32글자 (공백, 특수문자, 포함)

print(my_str)

#문자열에서 특정 순서의 글자를 뽑을 때 [] 사용
print(my_str[0],my_str[1],my_str[6],my_str[-3])
print(my_str[0]+my_str[1]+my_str[6]+my_str[-3])
print(my_str[-1])

#print(my_str[32]) #인덱스 범위를 초과하면 오류 발생 !!!!!!
print()

'''
    문자열 슬라이싱
        - 슬라이싱(slicing) : 조각낸다.
            >인덱스로 특정 범위의 문자를 조각내서 사용

        my_str[0:3] --> 콜론(:)으로 범위 지정

        my_str[시작인덱스 : 끝 인덱스] --> 끝 인덱스는 포함이 안 된다.(미만이라생각)
        
        my_str[시작인덱스 : ] --> '시작인덱스' 부터 '끝' 까지

        my_str[:끝덱스] --> '처음' 부터 '끝인덱스'까지 (끝인덱스는 포함X)

        my_str[:] --> 시작부터 끝 --> my_str와 같다 .

'''

my_str = "Without haste, but without rest." #32 글자

print(my_str[0]+my_str[1]+my_str[2]+my_str[3])   #인덱싱으로 출력

print(my_str[0:4])                               #슬라이싱으로 출력
print(my_str[8:13])
print(my_str[0:100])                  #슬라이싱은 범위초과해도 오류 X

print(my_str[15:])                  #15q부터 끝까지
print(my_str[:-5])                  #처음부터 뒤에서 5번째 까지 (끝인덱스틑 포함x)

print(my_str[:-200])            #뒤에서 200번째는 없다 .

#my_str의 문자중 , 첫 글자를 소문 w로 바꾸고 싶다면 ..

#my_str[0] = "w"    이미 만들어진 문자열은 변경이 불가능하다 .
#슬라이싱을 이용해서 새로운 문자열을 만들어야 한다 ..

new_str = "w" +my_str[1:]

print(new_str)

#!!!!중요 --> 문자열은 변경 불가능 ---> 고로 새로 만들어야 한다 .

print()

'''
    #문자열 기본 포메팅
        -문자열 안에 '값'을 '삽입'하는 방법

        -포맷 코드(서식문자)
            %s 문자열(string)
            %c 문자 1개
            %d 정수
            %f 실수
            %% %하나 삽입
            %o 8진수
            %x 16진수
'''
print("=" *70)
print("[문자열 기본 포메팅]")
print("정수 : %d" %10)
my_str = "정수 : %d" %30

#my_str ="정수 : 30

print(my_str)

#'문자열'에 값을 삽입해서 새로운 문자열을 만든다.
# 문자열 뒤에 바로 %기호를 붙여서 값을 입력

print("실수 : %f " %103.9384333333) # %f 기본이 6자리
print("문자열 : %s " %"나는 문자열")

#포맷코드의 사용은 뒤 따라오는 값을 어떤 형태로 삽입할 지 결정

print("정수 : %d " %3.45454) #실수 값을 정수로 삽입 (소수점 이하 소멸)
print("실수 : %f" % 30)      #정수 값을 실수로 삽입(없던 소수점 생김)

print("문자열 : %s" %10)     
print("문자열 : %s" %30.3434)
#숫자를 문자 형태로 삽입 할 수 있다. %s는 다 글자 취급
#print("정수 : %d" %"문자열") #이건 안됨 

print()

year = 2020
print("변수 사용 :%d" %year)

#올해는 2020년 입니다.

print("올해는 ",year,"년 입니다." ,sep="") #너무 불편함 ...
print("올해는 %d년 입니다." %year)    #이렇게 하면 훨씬 편함.....

year += 1   # year = year + 1 와 동일한 코드
#복합대입연산자 : 연산기호와 대입연산자(=)가 합혀진 형태
#자기 자신의 값을 이용해서 연산 후 다시 나한테 대입 해주는것

print("올해는 %d년 입니다." %year)

# -=, *=, /=

year -= 1  # year = year -1 
print("올해는 %d년 입니다." %year) 
year *= 2  # year = year * 2
print("올해는 %d년 입니다." %year) 

year /= 2  # year = year / 2
print("올해는 %d년 입니다." %year)
print()


print("%d개 이상의 %s 넣기" %(2,"값"))
#% 두 개 이상일 때 반드시 소괄호로 묶어준다 .. 그리고 순서대로 포맷코드에 삽입
print()

print("오늘의 행복 지수 100%")
print("오늘의 행복 지수 %d%%" %100)
#문자열 포메팅을 사용하지 않으면 (뒤에 %를 붙이지 않으면)
# % 기호는 일반 문자 처럼 사용되지만
# 포매팅을 사용하면, %하나를 사용하고 싶을 때 %%를 두 번 써야 한다.
print()

print("포맷코드를 활용한 소수점 표현")
print("소수 : %f" % 10.1) #기본 6자리
print("소수 : %f" % 10.666666666666666666)   #7번째 자리에서 자동으로 반올림
print("소수점 지정 : %.2f" % 10.666666666666) #둘째 자리까지 표현하겠다.. 나머지 반올림
print("소수점 지정 : %.8f" % 10.6666666666666) #8번째 자리까지 표현하겠다.. 마찬가지로 반올림
print("소수점 지정 : %.0f" % 10.666666666666) #.0으로 적으면 소수점을 날려버릴 수 있다. 마지막 자리에서 반올림
print()

print("[포맷코드를 활용한 정렬과 공백]")
print("[%s][%s]" % ("파이썬","재밌다"))
print("[%10s][%10s]" % ("파이썬","재밌다"))     #삽입 시 10칸 확보 후 값을 넣겠다. 우측정렬
print("[%-10s][%-10s]" % ("파이썬","재밌다"))   #좌측 정렬
print("=" *70)

# 포매팅 함수
# "문자열".format() --> 이런 형태가 많다.
# 포맷코드 대신에 {}중괄호를 사용해 사용한다 . 마치 %s와 같다라고 생각 하면됨.

my_str = "제 이름은 {} 입니다. ".format("홍길동") # (1) 만든 문자열을 변수에 대입
print(my_str)

print("제 나이는 {}살 입니다.".format(20))      #  (2)  만든 문자열을 바로 출력

print("1.제 이름은 {}이고 ,  {}살 입니다.".format("홍길동",20))    # 기본은 순서대로
print("2.제 이름은 {1}이고 , {0}살 입니다.".format("홍길동",20))   # {}안에 인덱스 사용

#변수 사용

name = "홍길동"
age = 20

print("3.제 이름은 {}이고 , {}살 입니다. " .format(name,age)) ####이게 가장 잘쓰임 


# 키워드 사용 (변수의 값에 대입하듯이 키워드에도 값을 대입 할 수 있음.

print("4.제 이름은 {name}이고 , {age}살 입니다. ".format(name="홍길동", age=20)) #키워드를 적는 순간 인덱스 번호는 사라짐
print("4.제 이름은 {name}이고 , {age}살 입니다. ".format(age=20, name = "홍길동")) #순서 상관 x 어차피 값에 맞춰서 들어감

print("6.제 이름은 {name}이고 , {age}살 입니다. ".format(name=name ,age=age))
#name 키워드에 name변수의 값인 "홍길동" 문자열을 삽입하겠다.
#age 키워드에 age 변수의 값인 정수 20을 삽입하겠다.

#키워드와 인덱스 혼용 시 키워드는 맨 뒤에 위치해야한다 .
print("7. 제 {}은 {name}이고, {}살 입니다. ".format("이름",20,name=name)) #파이썬은 인덱스를 먼저 넣는다 ... 그래서 오류남
#format()안의 값은 인덱스 한테 먼저 우선권이 주어진다 ...
print()

#출력 방법 비교

print("제 이름은 " + name + "이고, " , age, "살 입니다", sep="") #포매팅 x
print("제 이름은 %s이고, %d살 입니다." %(name,age)) #기본 포매팅
print("제 이름은 {}이고, {}살 입니다.".format(name,age))  #포맷 함수 포매팅
print()

# 소수점 표현

print("소수 : {}".format(10.123))
print("소수 : {}".format(10.123913840923485092485092485098908908)) #소수점 14번째 까지 출력 해준다 . 0부터센다
print("소수점 지정 : {:.2f}".format(10.7777777777))           #마찬가지로 반올림 가능 
# format() 함수 사용 시 중괄호{}에 특수한 기능을 추가하는 기호 --> 콜론(:)
# 콜론을 사용할 때는 인덱스 뒤에 위치한다. (인덱스 생략 가능 )
print()

#정렬
print("[{}] [{}]".format("파이썬","재밌다"))
print("[{:10}] [{:10}]".format("파이썬","재밌다"))   #10칸 확보 , 기본 좌측정렬 (기본값이 좌측정렬 이라 써도되고 안써도됨)
print("[{:>10}] [{:>10}]".format("파이썬","재밌다")) #우측정렬  >
print("[{:<10}] [{:<10}]".format("파이썬","재밌다")) #좌측 정렬 <
print("[{:^11}] [{:^11}]".format("파이썬","재밌다")) #가운데 정렬 ^
print()

#정렬 후 빈 공간에 값 채우기
print("[{:!^11}] [{:*^11}]".format("파이썬","재밌다"))
#1개의 선택된 문자로만 채울 수 있다 .. 
print("[{:굿^11}] [{:a^11}]".format("파이썬","재밌다"))

print("="*50)

print("[문자열 관련 함수]")
#"".format() 처럼 문자열을 이용해서 사용할 수 있는 유용한 함수들이 많다.
#문자열 --> 문자열.함수() 문법 규칙!!!

#upper() : 문자열의 영문을 모두 대문자로 변환하여 새로운 문자열을 만든다.
#lower() : 소문자로 만들어준다.

str1 = "I'm a Boy"

print(str1.upper())  
print(str1)
#1) 기존 값을 이용해서 새로운 결과를 만들어 낸다.
#2) 기존 값 자체가 변하지 않는다.
new_str = str1.lower()

print(new_str)
#1) 만들어진 문자열을 어딘가에 바로 사용
#2) 변수에 대입

print("sadfdfwerkj".upper()) #이렇게도 사용가능하다!!!
print()

#title() : 문자열에 존재하는 '영단어'의  첫 글자를 대문자로

str2 = "python python"
print(str2.title())
#문자열은 변경할수 없고 새롭게 만들어 주어야한다 .원본은 유지 됨 !!!
print(str2)
print()

#strip() : 문자열 좌우측에 존재하는 '공백'을 제거
str3 = "        공 백 제 거         "
print(str3.strip())
print(str3.lstrip())  #left : 좌측 공백 제거 
print(str3.rstrip())  #right : 우측 공백 제거

#join() : 특정 문자열을 대상 문자열에 삽입
# "A".join("BBB") --> "BABAB"
print("!asdf34".join("문자열 삽입 join"))
print()
#count("A") : 문자열에서 "A"의 개수를 반환 (함수의 결과 값이 A의 개수 )
str4 = "python python python"
print("str4에서 p의 개수 : ", str4.count("p"))      #결과 값이 '정수 
print("str4에서 python의 개수 : ", str4.count("python"))
print("str4에서 x의 개수 : ", str4.count("x")) #없으면 0 이나옴 
print()
#replace("A","B") : 문자열에서 모든 "A"를 찾아서 "B"로 변경
str5 = "replace : python python python"
print(str5.replace("py","Py"))
print(str5.replace(" p"," P"))
str3 = "        공 백 제 거         "
print(str3.replace(" ", ""))
print()
#***split("A") : 문자열을 기준 문자("A")로 나눈다.
str6 = "문자열 나누기 split"  #공백을 기준으로 나눈다 ..
print(str6.split()) #split() 함수 안에 아무 값도 넣지 않으면
                    #기본이 공백, 개행 등 여백으로 나눈다.
                    #기준되는 문자는 사라진다.

print(str6.split("열"))  #나오는 결과는 list자료형이다.
print()

#index("A") : 문자열에서 "A"를 찾고 , 그 위치(index)반환 (찾지 못하면 오류)
str7 = "문자열 위치 찾기 (index)"
print("str7에서 '열'의 위치 : ", str7.index("열")) #정수 반환 
print("str7에서 'index'의 위치 : ", str7.index("index")) #찾은 첫 문자의 위치

####print("str7에서 'z'의 위치 : ", str7.index("z")) #찾지 못하면 오류 발생### 

# find("A") :index와 같다 --> 그러나 찾지 못하면 -1을 반환 , 즉 오류가 나지 않는다.
print("abcdefg".find("e"))
print("abcdefg".find("k"))  #없을 때 오류 반환하지 않고 -1을 반환한다.(index와차이)
print()

print("문자열문자열".index("열")) #문자열안에 여러개가 있을때 어떻게???
                                #첫번째로 발견되는 문자를 기준 한다 ..

print("문자열문자열".rindex("열")) # r은 리버스의 약자, 뒤에서 부터 찾아준다
                                 #찾은 위치를 말해주는 것이지 음수가 아님 !!!

#find도 rfind 라고 사용
print("문자열문자열".index("열"))
print("문자열문자열".rfind("열"))

#만약 세번 반복시에 ... 중간에는 그러면 어떻게 처리??
print("문자열문자열문자열".index("열",3)) #3번의 인덱스 번호 부터 찾아주겠다 라는뜻.

#find도 똑같다.
print("문자열문자열문자열".find("열",3))





























































































        
        

















































            
    


 

















