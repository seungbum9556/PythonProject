'''
파일명: Ex15-1-object.py

클래스(class)
    클래스는 객체를 생성하기 위한 템플릿
    객체를 만드는 설계도
    붕어빵 틀, 와플 기계

    객체화(인스턴스화) - 메모리에 올리는 것

객체(object)
    현실 또는 가상 세계 존재하는 물리적, 추상적 개념을
    프로그램으로 표현한 것
    예) 물리적 - 컴퓨터, 자동차, 휴대폰
        추상적 -  용, 포켓몬, 주문, 배송


객체 구성
    초기화용 메서드 - 생성자
    속성 - 변수
    기능 - 매서드(method)

가비지 컬렉터(Garbage Collector)
    메모리 관리를 자동으로 처리하여 사용하지 않는 객체를 식별하고 제거

자동차
    속성
        브랜드: 현대, 이아, 테슬라
        색상: 빨강, 검정
    기능
        드라이브: 운전을 하면 빠르게 이동!
        자율 주행: 혼자 운전
'''

class Computer:

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU: {self.cpu}')
        print(f'RAM: {self.ram}')
        print(f'VGA: {self.vga}')
        print(f'SSD: {self.ssd}')

desktop = Computer()   # Computer 객체 생성
desktop.set_spec('i7','32G','GTX3060', '512GB')
desktop.hardware_info()

print(desktop.cpu)
print(desktop.ram)
print(desktop.vga)
print(desktop.ssd)

macbook = Computer()   # Computer 객체 생성
macbook.set_spec('M2','16G','M2', '512GB')
macbook.hardware_info()
