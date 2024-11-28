'''
파일명: Ex07-2-for-range.py

for 문과 range() 함수

range()
    연속된 숫자를 만들어주는 함수

    예) range(1,10) => 1, 2, 3, 4, 5, 6, 7, 8, 9

'''
dan = 2
# range(stop)
for n in range(10):
    print(f'{dan} X {n} = {dan * n}')

dan = 3
# range(start,stop)
for n in range(1,10):  # range(1,10); 1 ~ 9
    print(f'{dan} X {n} = {dan * n}', end = " ")
print()


range_list = list(range(1,6))
print(range_list[0])

dan = 4
# range(start, stop, step)
for n in range(1, 10, 2): # 1부터 2씩 증가, 10보다 작을 때까지
    print(f'{dan} X {n} = {dan * n}', end=" ")
    print()