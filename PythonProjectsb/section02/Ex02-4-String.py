'''
파일명: Ex02-4-String.py

문자열(string, str)
    -문자들의 순서가 있는 나열
    -작은 따옴표(') 또는 큰 따옴표(")로 표현
    -문자열은 변경 불가능(immutable)

'''

# 1. 문자열 생성 방법
str1 = 'Hello Python' #작은 따옴표
str2 = "Hello Python" #작은 따옴표
# 여러줄 문자열 작은 따옴표
str3 = '''Hello 
Python
'''
# 여러줄 문자열 큰 따옴표
str4 = """Hello
Python
"""

# 줄 복사 단축키 Ctrl + d
# 줄 삭제 단축키 Ctrl + y
print(str1)
print(str2)
print(str3)
print(str4)

# 2. 문자열 인덱싱
'''
         /h /e /l /l /o
index     0  1  2  3  4
역순 번호 -5 -4 -3 -2 -1
'''

str = 'hello'
print('1번째 문자:',str[0])
print('마지막 문자:',str[4])
print('-1번째 문자:',str[-1])
print('문자:',str[1],str[2])

# 3.문자열 슬라이싱

str = 'Python Programing'
print('처음 부터 4글자:', str[0:4])
print('처음 부터 4글자:', str[:4])
print('7번째 부터 :', str[7:])
print('마지막 5글자:', str[-11:])

# 4. 주요 문자열 메소드(함수)
str = '   P y t h o n   '
print('공백 제거:', str.strip()) #글자 사이 사이 공백 제거 아니고 앞뒤 공백만 제거
print('글자 사이 공백 제거:', str.replace(' ',''))
print('모두 대문자:', str.upper())
print('모두 소문자:', str.lower())
print('문자 교체:', str.replace('P','J'))
print('  가나다라   '.replace(' ',''))


