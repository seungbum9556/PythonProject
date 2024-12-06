'''
파일명: Ex14-5-jsonWriter.py

Json (javaScript Object Notation)
    데이터를 키와 값의 쌍을 중괄호({})로 묶어 표현하는 방식
    -딕셔너리와 비슷하다
    -구조 {K : V}
'''

import json
from idlelib.iomenu import encoding

dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]

    },
    {
        'name' : 'alice',
        'age' : 21,
        'spec' : [
            168.5,
            60.5
            ]
    }

]

json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)

with open('dictlist.json', 'w', encoding = 'UTF-8') as file:
    file.write(json_string)

print('dictlist.json 파일이 생성되었습니다.')