'''
파일명 : Ex02-7-set.py

세트(set)
    - 중복을 허용치 않는 자료 구조
    - 순서가 없음(인덱싱 불가)
    - 집합 연산 가능


'''
from os import remove

# 1. 세트 생성과 기본 기능
pokemon_type = {'불꽃','물','전기','풀'}
print('포켓몬 속성:', pokemon_type)

# 2. 세트 수정
fire_type = {'파이리','마그마','브케인'}

# 단일 추가
fire_type.add('리자몽')
fire_type.add('마그마')  #중복 허용치 않는다
print('불꽃 타입 단일 추가:', fire_type)

# 여러 항목 추가
new_fire = {'마그케인','불케니온'}
fire_type.update(new_fire)
print('불꽃 타입 여러 항목 추가:', fire_type)

# 요소 뺴오기
removed = fire_type.pop() # 임의 제거 및 변환
print('방출된 포켓몬:', removed)
print('현재 포켓몬:', fire_type)

# 3. 세트 요소 전체 출력
water_type = {'꼬부기','잉어킹','라프라스'}

for pokemon in water_type :
    print(pokemon)

# 4. 세트 제거 메서드
water_type = {'꼬부기','잉어킹','라프라스'}
water_type.remove('잉어킹') # 세트의 값이 없으면 에러 ex: water_type.remove('피카츄')
print('remove 후:', water_type)

water_type.discard('라프라스') #값이 없어도 에러 없음
print('discard 후:', water_type)

water_type.pop() #임의 제거
print('pop 후:', water_type)

#water_type.pop() #값이 없으면 에러 발생 KeyError: 'pop from an empty set'

new_type = {'메가 이브이','뮤'}
new_type.clear() # 전체 제거
print('clear 후:', new_type)
