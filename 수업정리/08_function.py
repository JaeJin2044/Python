# 08_function.py

'''
    [함수 function]   (method : 같은말)
        - 특정 작업을 수행하는 일련의 문장들을 하나로 묶은 것

        - 함수의 장점
            1. 한번 만들어놓으면 언제든지 재사용 가능
            2. 중복된 코드 제거
            3. 프로그램의 구조화
                > 작업 단위로 코드를 묶어서 구조화 시킨다.

    [함수의 기본 구조]
    def 함수이름(매개변수):     def = define 정의하다
        수행문
        return 반환 값

1. 매개변수 (parameter)
    - 함수가 호출될 때 값을 받을 '변수'
    - 개수 제한이 없고, 필요 없으면 생략도 가능
    - 우리가 함수를 호출할 때 전달하는 '값'을 인수라고 부른다.
        > argument

2. 반환 값
    - return 뒤에 오는 값은 함수의 수행이 완료되고 되돌려주는 값
    - return 을 사용하면 함수의 수행이 끝난다.
        > 마치 반복문에서 break를 사용한 것과 느낌이 비슷하다.

    >>> 매개변수와 반환 값의 유/무에 따른 함수 형태 (4가지)
        1. 매개변수와 반환 값이 둘 다 있다.
        2. 매개변수와 반환 값이 둘 다 없다. (기능 수행만 한다)
        3. 매개변수만 있다.
        4. 반환 값만 있다.

'''








print("[함수]")

# 함수는 define 하기만 하면 프로그램 수행에 영향이 없다.
# 함수를 정의 한다 = 이 후 이 함수를 언제든 사용할 수 있도록 준비

print("[함수의 4가지 형태]")

# 1. 매개변수, 반환 값 둘 다 있다.

def add(a,b):
    return a + b 

# add함수는 매개변수가 2개 --> 사용하려면 값을 2개 전달 해줘야 한다.
# 호출할때는 함수이름(인수,인수)

result = add(1,2)  # 함수 호출 (1)


# 함수의 호출코드는 결국 return 뒤에 있는 값으로 변경된다고 생각
print(result)

print("{} + {} = {} ".format(10,20, add(10,20)))     # 함수 호출 (2)

# 반환 값이 있는 함수를 호출 했을 때는
# 함수의 기능 수행이 끝난 뒤 반환 값을 들고 온다.
# (1) add(1, 2) 는 함수의 반환 값인 3으로 대체 된다. ==> 변수에 대입
# (2) add(10, 20) 는 30으로 대체 된다 --> format() 함수에서 사용
print()

# 2. 매개변수 , 반환 값 둘 다 없다.

def sayHo():
    print("Ho~~~!!")
    print("Ho! Ho!")


print("sayHo 호출 전")
sayHo()                 
print("sayHo 호출 후")
print()

# 함수를 호출하면, 코드의 흐름이 내가 호출한 함수의 수행문으로 '점프'
# 함수의 수행문이 끝나면 함수를 호출했던 원래 위치로 되돌아 온다.
# 단, return 반환 값이 있다면 그 값을 들고 온다.

# 매개변수에 따라 함수를 호출 할 때는 그 규칙을 맞춰줘야 한다. (개수)

# 반환 값에 따라서는 규칙을 맞추지 않아도 사용은 가능하다.
# 반환 값이 있다 = 변수에 대입, 어딘가에 바로 사용

result = sayHo()  # sayHo 는 반환 값이 없기 때문에 호출 후 출력하고 사라져버림..

print("sayHo()의 결과 1:" , result)
print("sayHo()의 결과 2:" , sayHo())
print()
# 반환 값이 없는 함수는 그냥 호출만 하기
# 변수에 대입하거나 어딘가에 사용을 하면 None이라는 값이다.


# 3. 매개변수만 있다.

def say(talk):
    print(talk)

say("안녕하세요?")
say(1)
say([1,2,3])
print()
# 4. 반환 값만 있다.

def getHi():
    return "Hi~~!!"

hi = getHi()
print(hi)
print(getHi())

# return 뒤에 오는 값의 자료형에 따라 반환된 결과도 그 자료형이 된다.

# 함수의 기본 개념 끝!

# 여러 값 반환하기
print("[여러 개의 값 반환]")
def calc(a, b):
    return a+b, a-b, a*b, a/b # 여러 개처럼 보이지만, '튜플'

print(calc(10, 3))
print(type(calc(10, 3)))

a, b, c, d = calc(10, 3)
# a, b, c, d = (13, 7, 30, 3.333333333333)
print(a, b, c, d)
print()

# 매개변수에 초기 값 사용
def print_info(name, age, phone="010-xxxx-xxxx"):
    print("이름 :", name)
    print("나이 :", age)
    print("전화번호 :", phone)

print_info("홍길동", 20, "010-1111-2222")

print_info("홍길동", 20 ,"010-1111-2222")
print()
# 값을 안주면 초기값
# 값을 주면 내가 준 값으로 변경
# print함수의 sep = ' ' , end='\n' 초기 값이 적용된 매개변수

# 매개변수에 초기 값을 적용하려면, 초기 값이 들어가는 매개변수는 맨 뒤에 위치해야 한다.

# 키워드 인수 : 함수의 매개변수명을 키워드로 사용

def print_info(name, age, phone):
    print("이름 :", name)
    print("나이 : ", age)
    print("번호 : " , phone)

print_info(name= "홍길동", age = 20, phone = "112")

# sep , end에 값을 넣는 행위

print()

# 가변인수 : 전달하는 값의 개수가 변할 수 있다.

def add(*args):
    print(args)     # 튜플로 만들어줌 !!!!  적을때는 *표시하고 출력할때는 그냥 표시 !!!
    result = 0
    for i in args :
        result += i
    return result

add(1, 2, 3)
add(1, 2, 3, 4, 5, 6)
print(add(10,1,2,3,4))

# 일반 매개변수, 가변인수를 혼용할 때  가변인수는 마지막에 위치

def fn(*args,a,b,):
    print(a)

# fn(1, 2, 3, 4, 5, 6 , 7, 8)         # 오류남
# fn(1, 2, 3, 4, 5, 6 , 7, 8, a=3 , b= 5)    # 이렇게 표시하면 되기는 되지만 이런식으로 사용하지말자 !!!!

    

def fn(a,b, *args):
    print(a)

fn(1, 2, 3, 4, 5, 6 , 7, 8)  # 이렇게 사용하면 문제 없음 !!



# 재귀함수

def func3(num):
    print("func3 시작", num)
    print("func3 끝", num)
    
def func2(num):
    print("func2 시작", num)
    func3(num-1)
    print("func2 끝", num) 

def func1(num):  
    print("func1 시작", num) 
    func2(num-1)   
    print("func1 끝", num)


print("func1 호출 전") 
func1(3)
print("func1 호출 후")
print()


'''
    재귀함수
        - 함수의 수행문 안에서 나 자기 자신 함수를 다시 호출하는 함수
        - 수행문이 반복되기 때문에 반복문과 유사한 성격
        - 너무 많이 반복 수행하다보면 프로그램 오류 발생
        - 함수 호출 시  Stack 이라는 메모리 구조를 사용
            Queue : First in First Out(FIFO) - 입구/출구 따로
            Stack : First in Last Out(FILO) - 우물형태(출입구 하나)
                > Stack 용량이 초과될 정도로 많이 호출하면 오류 발생
                > StackOverFlow 오류
                > 함수 호출시 Stack을 사용하는 이유는
                  함수 수행이 끝난 후 돌아갈 위치를 저장

        - 재귀함수도 반복 호출이 끝날 수 있는 조건이 필요
'''

def func(num):
    print("func() 시작," ,num)
    if num ==1:
        print("func 끝" , num)
        return  # 함수에서 반환 값 없이 return만 쓰면 종료
    
    func(num-1)  # 내 함수를 다시 호출 = 재귀호출(재귀호출이 있으면 재귀함수)
    print("func 끝", num)


func(3)
print()

# 지역변수와 전역변수
#   지역변수 : 특정 지역에서만 사용가능한 변수
#   전역변수 : 전체 영역에서만 사용가능한 변수
#       > 우리는 여태 '전역변수'만 사용했다.


value = "전역 변수" # 어느 수행문에도 속하지 않는 위치
                    # 만들어진 뒤부터는 어디서든 사용 가능


def func1():
    print("func1() 호출 ")
    print(value)  # 전역변수는 어디서든 접근 가능


def func2():
    print("func2() 호출")
    value_func2 = "func2()의 지역변수"
    print(value_func2)

    value = "지역변수로 변경"
    print(value)
    # value 전역변수가 이미 있는데
    # 지역에서 value의 값을 대입하게 되면
    # 전역변수 value의 값이 변경되는게 아니라
    # 같은 이름으로 이 지역의 value 지역변수가 생성

def func3():
    print("func3() 호출")
    global value_func3        # 지역변수를 전역변수로 만드는 명령 
    value_func3 = "fuc3의 지역변수"
    


func1()
func2()       #  print(value_func2)  # func2에만 존재하는 지역변수 ... 바깥에서 사용 못함 !!!
print(value)
print()

func3()
print(value_func3)  # func3이 호출되어야 value_func3 변수가 만들어진다.


    


        



    
    





























































