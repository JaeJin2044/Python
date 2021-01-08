#03_type2.py

#파이썬의 자료형들 : 숫자 ,문자, 리스트, 튜플, 집합, 딕셔너리, bool  (총 7가지)

'''
    [3. 리스트(List)자료형]
        - 데이터들의 목록
        - 편리하다.

        리스트명(변수) = [요소1, 요소2, 요소3, ... ]
'''

print("[리스트 만들기]")
a = [] #요소가 없는 빈 리스트
b = [1, 2, 3] #요소가 정수
c = ["A", "B", "C"] #문자열 
d = [1, 2, "A", "B"] #혼합
e = [1, "A", 2, "C",[2,"B"]] #혼합 + 리스트 안에 또 다른 리스트 가능 !

print(a)
print(b)
print(c)
print(d)
print(e)
print()
# type() : 자료의 종류를 가르켜준다.
print(type(a))
print(type(7))
print(type(1.1))
print(type("안녕"))
print()

print("[리스트 인덱싱, 슬라이싱]")
# 문자열 : 하나 하나 문자들이 순서대로 나열된 형태
# 리스트 : 하나 하나 요소들이 순서대로 저장된 형태
# 순서가 있으면 인덱싱, 슬라이싱 사용 가능

my_list = ["아이유", "수지", "박서준"]
print(my_list)
print("첫 번째 사람 : " + my_list[0])
print()
# 첫 번째 요소가 문자열이기 때문에 인덱싱해서 가져온 값도 문자열이다.


# 이중 리스트 인덱싱(리스트 안에 또 다른 리스트를 요소로 가짐)
my_list = ["아이유", "수지", ["박서준", "공유"]]

# my_list의 3번째 요소는 '리스트'이다.

print(my_list[2])
print(my_list[2][0][1])
print(my_list[2][1])
print(my_list[0][2])
print(my_list[2][0][2])
print(my_list[-1][0])
# 인덱스 범위 초과, 음수 사용 이런 개념은 동일

a = [2, "2"]

print(a[0] *2)   # 4가 나옴 
print(a[1] *2)   # 22가 나옴
print()

# 슬라이싱
print(a[0:2])
print(a[0:1])   # 요소가 하나밖에 없어도 슬라이싱의 결과는 '리스트'이다.
print()
print("="*50)
print("[리스트 연산하기]")

a = [1, 2, 3]
b = [4, 5, 6]

print(a+b) # 연결해서 하나의 리스트로 만듬
print(a*2) # 문자열처럼 요소가 반복된다 생각 !!
c = a + b
print(c)
print()
print("="*50)
print("[리스트 수정하기]")   #문자열은 수정이 불가능하나 리스트는 수정이 가능하다..

a = [1, 2, 3, 4, 5, 6]

a[2] = -1  #문자열에서는 오류가 나는 코드 ... 리스트에서는 값을 바꿔 준다.
print("변경 후 :",a)

# 연속된 범위의 값을 수정
a[0:2] = [0]
print("변경 후 :",a)

a[0:2] = [6, 7, 8] # 순서대로 하나씩 대입
print("변경 후 :",a)

#인덱싱
a[0] = [1, 2] #첫 번째 요소에 '리스트'를 대입
print("변경 후 :",a)

# 리스트 요소 삭제
a[0] = []     #빈 리스트를 대입 삭제하는 것이 아니라 변경
print("변경 후 :",a)

a[0:2] = []     #슬라이싱을 통해 빈 리스트를 대입하면 제거 
print("변경 후 :",a)


del(a[0])   #해당 요소 제거
print("변경 후 :",a)

del(a[0:1])
print("변경 후 :",a)
print()
print("="*50)

print("[리스트 관련 함수]")

#리스트.함수()
a = [1, 2, 3]

#append(value) : 리스트 가장 뒤에 value(요소)를 추가

a.append(4)
print(a)
# 리스트 자체가 수정된다.
# append는 하나의 '요소'만 추가 할 수 있다.
a.append([5,6])   # 리스트는 그 자체로 하나의 값이라고 생각!
print(a)
print()
#sort() : 리스트 정렬 하기 (숫자, 알파벳 등등)
a = [3, 1, 4, 2]
a.sort()
print("변경 후: ",a) #기본 오름차순
a.sort(reverse=True)
print("변경 후: ",a) #내림차순
print()

# reverse() : 리스트 뒤집기 (정렬x)

a = [3, 1, 2, 4]
a.reverse()
print("변경 후: ",a)
print()

# index(value) : 리스트에서 value를 찾아 그 위치를 반환

a = [1,2,3]
print(a.index(3))
print()

# insert(index, value) : 지정한 위치(index)에 값(value) 삽입
a = [1, 2, 3]
a.insert(1,"굿")
print("변경 후: ",a)


# remove(value) : 리스트에서 '처음' 찾은 값 (value)제거
a = [1,2,3,1]
a.remove(3)
print("변경 후: ",a)   #a.remove(6) 없는 것을 지우려고 하면 오류가 남
print()

# count(value) : 리스트에 존재하는 value의 개수 반환

a = [1, 2, 3,1,1,1, 11, 33, 5, 6, 7, 1, 3, 5, 11, 22, 2, 5]
print(a.count(1))   #없으면 오류나지 않고 0 이나옴 !!
print()

# pop(index) : 리스트에서 (index)번째 값을 '뽑아 낸다'
#   1. 뽑아낸 값을 반환 해준다.
#   2. 리스트에서 해당 값을 제거

a = [1, 2, 3]
print(a.pop(1))
print("변경 후: ",a)
print(a.pop())    # 맨 뒤(기본)
print("변경 후: ",a)
print(a.pop(0))
print("변경 후: ",a)

# len() : 요소의 갯수를 구하는 함수
a = [1, 2, 3, 4]
b = "1234"
c = 1234

print(len(a))
print(len(b))
# print(len(c)) # 오류
# a = 리스트  = 어떤 값들이 여러 개 존재
# b = 문자열 = 문자들이 여러개 준조
# c = 정수 = 하나의 값
# 값이 여러개 존재하는 자료형만 len() 사용할 수 있다.
print()

# copy() : 모든 값들을 '복제'하여 새로운 리스트 생성
a = [1, 2, 3, 4]
b = a.copy()
c = a

print("기존 a :",a)
print("복제 b :",b)
print("대입 c :",c)

a[0] = -20
print()
print("기존 a :",a)
print("복제 b :",b)
print("대입 c :",c)
print()
# a,c는 똑같은 번지를 가리키는 것이고 b는 새로운 b라는 공간을 만들어서 값만 같은 값을 받아온것이다.

# clear() : 리스트의 모든 요소 제거

a = [1, 2, 3, 4, 5]
a.clear()
print("a =",a)

#list의 요소들이 '문자열'로만 이루어진 경우
#문자열 관련 함수 중 join()을 이용하여 하나의 문자열을 만들 수 있다.

my_list = ["대", "한", "민", "국"]
print("".join(my_list))
































