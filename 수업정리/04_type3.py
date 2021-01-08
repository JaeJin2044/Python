#04_type3.py

'''
    [4. 튜플(Tuple)자료형]
        리스트와 비슷하다.
            -차이점
                1. 생성법
                    리스트 []
                    튜플 ()

                2. 튜플은 한번 만들면 변경 할 수 없다.

            -프로그램이 수행되는 동안 요소가 변경되지 않게 하고 싶다면
             리스트 대신 튜플을 사용한다. 일반적으로는 '리스트' 사용

'''

print("[튜플 만들기]")
a = ()     # 빈 튜플
b = (1,)   # 요소가 1개 일때는 뒤에다가 ,를 찍어야 한다.
c = (1, 2, 3, "A", "B", "C")   # 혼합해서 사용 가능 
d = 1, 2, 3, 4  # 튜플은 괄호를 안쳐도 튜플로 만들어짐 !!!!
e = (1, "A", (2, "B"))



print(a)
print(b)
print(c)
print(d)
print(e)
print()

a= (1, 2, 3, 4)
print(a[0])   # 인덱싱 가능
print(a[0:2])

c= a+ b
print(c)
print(a*3)
print()

print("="*50)
'''
    [5. 딕셔너리(Dictionary) 자료형]
        사전
        형태 : {key1 : value1, key2: value2, ...}
            > key와 value 는 한 쌍
            key = 단어, value = 뜻

        -요소가 여러 개 나열된 자요형이지만
        문자열, 리스트 , 튜플은 순서가 있어서 인덱스로 인덱싱 가능
        딕셔너리는 순서가 없고 key를 가지고 인덱싱

        -주의사항
            1. key값은 중복되면 안 된다.
            2. key값으로는 리스트 , 딕셔너리를 사용할 수 없다.
                > key : 변하지 않는 성질의 자료
                > value : 아무거나 상관없음
'''
print("[딕셔너리 만들기]")
my_dict = {"축구" : "Soccer", 2002:"한일", (1,2) :("원","투"),"16강":[2002,2010]}
print(my_dict)

# 딕셔너리 [key] 를 통해 value 를 얻는다 !!!!!
print(my_dict["축구"])
print(my_dict[2002])
print(my_dict[(1,2)])
print(my_dict["16강"])
print(my_dict["16강"][0])  #이런식으로 가능 !!! 가져온 value 값이 리스트이기 때문에 순서를 가진다.
print(my_dict["16강"][1])
print()

# 추가 , 삭제
my_dict = {1: "a"}
my_dict[2] = "b"   #[]에 key값이 들어가고 , 그 key의 value를 대입
print(my_dict)

my_dict[2] = "c"   # key 값은 변경할 수 없다 ...
print(my_dict)     # value 값 변경 ...


del(my_dict[2])
print(my_dict)
print()

'''
    [ 6.집합(Set) 자료형]
        - 수학에서의 집합을 의미
            > 교집합, 합집합 , 차집합 등을 구할 수 있다.
        - 중복된 값을 허용하지 않는다.
            > 중복 제거 용도로 사용
        - 순서가 없다. (인덱싱 불가능)
'''

print("[집합 만들기]")
my_set = {1, 0, 9, 4, 5, 6, 7, 1, 2, 3, 5, 6, 6, 5, 4}

print(my_set)

my_set2 = {2, 1, 2, 1, 1, "B","B","A","A"}
print(my_set2)


'''
int()   : 정수로 변환
float() : 실수로 변환
숫자끼리 변환 가능

str()   : 문자열로 변환
list()  : 리스트로 변환
tuple() : 튜플로 변환
dict()  : 딕셔너리로 변환
set()   : 집합으로 변환

'''

my_num = int("123")
print(my_num +10)

my_num2 = float(my_num)
print(my_num2)

my_str = str("123")
print(my_str + "입니다.")

my_list = list(my_str)
print(my_list)

my_dict = dict(a=10 , b=20)  # k=v 형태로 작성 .... key 값은 무조건 문자열만 작성 가능 ...,따옴표 안씀
print(my_dict)

my_set = set(my_list)
print(my_set)

print()

'''
    [7. bool 자료형]
        - 참(True)과 거짓(False)을 표현하는 자료형
        - 자료형의 값에 따른 참과 거짓
            값             True / False
         ==========================================
            0               False
            1               True
            -1              True
            "abc"           True
            ""              False
            []              False
            [1,2]           True
            (1,2)           True
            ()              False
            None            False    
         ==========================================
         거짓인 경우
             1. 요소가 없다. (문자열, 리스트, 튜플 등등)
             2. 숫자가 0이다.
             3. None :  값이 없다는걸 의미하는 '자료형/값'
'''

print("[bool 자료형]")
# bool() : 값이 참인지 거짓인지 판별
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(""))
print(bool(" "))
print(bool([1,2]))
print(bool([]))
print(bool(None))


# bool 자료형은 True / False 2개의 값만 존재한다.
# 조건식을 다룰 때 나오는 개념.

# 숫자 : 그냥 쓰면 됨
# 문자열 : 따옴표로 묶는다.(4가지)
# 리스트 :  []
# 튜플   : ()
# 딕셔너리 : {k:v}
# 집합 :{}
# bool : True/False


















