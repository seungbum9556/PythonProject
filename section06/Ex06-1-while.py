'''
파일명: Ex06-1-while.py

1. while 문
    특정 조건을 만족하는 동안 반복해서 수행하는 명령어

    while 조건식:
        반복 수행할 코드
'''
n = 10
while n != 0:
    print(n)
    n -= 1 # n = n - 1

print(f'while문 끝나고 n의 값: {n}')