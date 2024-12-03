'''
파일명: Ex12-2-module.py

모듈 사용법
from 모듈명 import 함수
from 모듈명 import 함수1, 함수2
from 모듈명 import *


'''
from converter import kilometer_to_miles
# 전체 다 불러 오려면 from converter import *
miles = kilometer_to_miles(150)
print(f'150km = {miles}miles')
