# 11_module_package.py

'''
    [모듈과 패키지]
        모듈 (module)
            - 변수, 함수, 클래스 등을 모아 놓은 소스 파일
            - 간단한 기능을 담을 떄 사용
            - 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만들어진 소스 파일

        패키지 (package)
            - 여러 모듈을 묶은 것
            - 코드가 많고 복잡할 때 사용
            - 관련모듈(소스파일)들 끼리 한 폴더에 넣어 놓은 형태(폴더 = 패키지)

        - sys.path 안에 모듈이 위치해 있어야 사용이 가능
        - sys.path.append("C:\\~~\\~~\\")형태로 경로 추가 (path는 리스트)
        
'''

'''
import sys
print(sys.path)
'''

# 패키지의 모듈 사용 - 그외 as, from 사용은 동일
'''
import koreais.koreais_module 
# 폴더안에 또 다른 폴더가 있는 하위 구성일 때도 동일
# import pack1.pack2.pack3.koreais_module --> 점은 그안으로 들어가겠다 !! 이렇게 인지하자

print(koreais.koreais_module.my_str)
'''

'''
    패키지 안에 __init__.py 파일이 있어야 패키지가 됐었다 (없으면 패키지X)
    패키지를 호출 했을 때 무조건 호출 

'''

'''
# 1. from . import koreais_module
import koreais
print(koreais.koreais_module.my_str)
'''

# 2. from .koreais_module import *
'''
import koreais
print(koreais.my_str)
'''

from koreais import *
print(my_str)

# 3. __all__사용

print(add(10,20))















