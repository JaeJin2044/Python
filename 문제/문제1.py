'''
	1. 아래의 결과가 나오도록 코드 작성
	[출력결과]
	Hello Python!!
'''

print("Hello Python!!")
print("====================================================")
'''
	2. 아래의 결과가 나오도록 코드 작성
	    단, 프로그램명, 제작일자, 제작자에 들어가는 데이터는 변수로 만들어서 출력
	[출력결과]
	프로그램명 : Python
	제작일자 : 2020년3월20일
	제작자 : 홍길동

        name = "Python"
        year = 2020
        month = 3
        day = 20
        
'''
name = "Python"
year = 2020
month = 5
day = 21
Producer="홍길동"

print("프로그램명 : "+name)
print("제작일자 : " ,year,"년" ,month,"월",day,"일" , sep='')
print("제작자 : "+Producer)
print("====================================================")

#한줄로 나오게 해보자 !!
print("프로그램명 : " +name+"\n제작일자 : ",year,"년",month,"월",day,"일\n","제작자 : "+Producer,sep='')
print("====================================================")



'''
	3.  *_@@@_*
	   @*%@*@%*@
	  @(*- _ -*)@
	    /     /	
	     | | |          이렇게 나오도록 출력
'''

print("	    *_@@@_*")
print("	   @*%@*@%*@")
print("	  @(*- _ -*)@")
print("	    /     /	")
print("	     | | |          ")

print("====================================================")


'''
4. 이름,나이,전화번호를 name ,age ,phone 변수에 대입

그리고 아래와 같이 출력

[출력결과]
이름 : 홍길동
나이 : 20세
전화번호 : 010-1111-2222

'''
name="홍길동"
age=20
phone_number= "010-1111-2222"    #-같은 기호 있으므로 문자열로 묶어 주자 


print("이름 : "+name)       #문자열 끼리는 +연산으로 가능 
print("나이 : ",age,"세",sep='')  #문자열과 숫자는 연산이 안되므로 (,꼭 붙여주자)
print("전화번호 : "+phone_number) 









	    

	  
