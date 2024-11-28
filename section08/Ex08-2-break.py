'''
파일명: Ex08-2-break.py
'''
'''
i = 0
while i < 7:
    j = 0
    while j < i+1:
        print('*', end= '')
        j = j+1

    print()
    i = i+1

i = 7
while i > 0:
    j = 0
    while j < i :
        print('*', end='')
        j = j + 1

    print()
    i = i - 1
'''
i = 7
while i > 0:
    j = 0
    while j < i :
        print('a', end='')
        j = j + 1

    print()
    i = i - 1