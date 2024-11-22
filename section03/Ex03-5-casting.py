'''
파일명 : Ex03-5-casting.py

형변환(casting)
    -변수에 유형을 지정하려는 경우 형변환으로 가능
    주요 함수 : int(), float(), str(), list(), tuple()
'''

# 1. 숫자 형변환
str_num1 = '15'
str_num2 = '20'

result1 = str_num1 + str_num2
print(f'결과: {result1}')
result2 = int(str_num1)+ int(str_num2)
print(f'형 변환 후 결과: {result2}')

# 2. 실수 형변환
x = float('1')
y = float(3)
print(x)
print(y)

z = int(3.141592)
print(z)
print(float(z))

strX =  str(1)
strY = str(2)
result = strX + strY
print(result)