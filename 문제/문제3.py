'''
    3. 문자열 슬라이싱 연습
        - phone_number 에서 숫자만 가져와서 새로운 변수에 저장
'''

phone_number = "010-1111-2222"
# only_number 변수 만들기
#print(only_number) #--> 01011112222
only_number = phone_number[0:3] + phone_number[4:8]+phone_number[-4:]
print(only_number)


'''



    4. 문자열 슬라이싱 연습
        - info 에서 이름과 성별을 각각 변수에 저장
'''


info = "홍길동 - 남자"
# name 만들기
# gender 만들기
#print(name)   #--> 홍길동
#print(gender) #--> 남자

name = info[0:3]
gender = info[-2:]
print(name)
print(gender)



print("="*40)

'''
    5. 문자열 포매팅 연습
        - 아래 3개의 변수를 미리 만들어 놓고, 포매팅을 사용하여 출력
name  = "홍길동"
age   = 20
phone = "010-1111-2222"
        
        (1) 포매팅 -> .format 사용 X(%d같은것들 ..)기본 으로만
        (2) 포매팅 -> .format 사용 O
        (3) 포매팅 사용하지 않고 출력 -> 아마도 제일 복잡한..^^;
        
[출력결과]
이름 : 홍길동
나이 : 20
전화 : 010-1111-2222

'''
name = "홍길동"
age = 20
phone = "010-1111-2222"

#1
print("이름 : %s"%name)
print("나이 : %d"%age)
print("전화 : %s"%phone)
#2
print("="*40)

print("이름 : {} ".format(name))
print("나이 : {} ".format(age))
print("전화 : {} " .format(phone))

print("="*40)

#3

print("이름 :"+name)
print("나이 :"+ str(age))
print("전화 :"+phone)




'''
    6. 문자열 포매팅 연습
        - 문자열.format() 을 이용하여 20칸 크기 확보 후 가운데 정렬! (방식 자유)
        - 문자열 곱셈 연산은 사용하지 않기

[출력결과]
====================
       String
====================


'''
print("====================")
print("{:^20}".format("String"))
print("====================")


#정답
print()
print("{:=^20}".format("="))
print("{:^20}".format("String"))
print("{:=^20}".format("="))

















