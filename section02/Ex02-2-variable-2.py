'''
파일명: Ex02-2-variable-2.py

변수명 규칙:
    -영문, 한글, 숫자, _로 구성
    -특수문자 사용 불가
    -첫 글자는 숫자 불가
    -키워드(명령어) 사용 불가
     주석 단축기 -> Ctrl+/
'''
# 1. 여러 변수에 다른 값 할당
x,y,z ="피카츄", "라이츄", "파이리"
print('포켓폰1: ',x)
print('포켓폰2: ',y)
print('포켓폰3: ',z)
print('포켓몬1','포켓몬2','포켓몬3',x,y,z)
#  2. 여러 변수애 같은 값 할당
x =  y = z = '꼬북이'
print('변경된 포켓몬:', x)
print('변경된 포켓몬:', y)
print('변경된 포켓몬:', z)

# 잘못된 변수명 예시
"""
2myvar = 'Python1' # 변수 명이 숫자로 시작(변수명 속에는 숫자가 들어갈 수 있음)
my-var = 'Python2' # 특수 문자 포함
my var = 'Python3' # 공백 포함

"""

my_var= 'Python4' # _ 가능
