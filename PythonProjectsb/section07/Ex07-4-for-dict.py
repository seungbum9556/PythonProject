'''
파일명: Ex07-4-for-dict.py

이름      국어 영어 수학
John     90  85  95
Emily    92  88  96
Michael  98  90  92
Jessica  88  82  78
'''

'''
세로 편집모드 단축키
Alt + Shift + Ins
'''
students = [
    {'이름' : 'John', '국어' : 90, '영어' : 85, '수학' : 95},
    {'이름': 'Emily', '국어': 92, '영어': 88, '수학': 96},
    {'이름': 'Michael', '국어': 98, '영어': 90, '수학': 92},
    {'이름': 'Jessica', '국어': 88, '영어': 82, '수학': 78}
]
for student in students:
    print(f'{student['이름']}\n', end= ' ')
    print(f'{student['국어']}\n', end=' ')
    print(f'{student['영어']}\n', end=' ')
    print(f'{student['수학']}\n', end=' ')

mike = students[2]
for k,v in mike.items():
    print(f'{k} : {v}')
