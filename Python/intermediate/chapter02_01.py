# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트 등
# 규모가 큰 프로젝트(프로그램) -> 과거에는 함수 중심으로 코딩을 함. -> 데이터가 방대해짐 -> 복잡해진다
# 클래스 중심 -> 데이터를 중심으로 코딩을하면 -> 여러 구성 요소들이 객체로 관리

# 일반적인 코딩
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 위 구조를 보완하기 위해 이번엔 리스트 구조로 하기
# 관리하기 불편함
# 인덱스 접근 시 실수 가능성, 삭제가 불편함(인덱스를 알아야함)
# 딕셔너리는 키값으로 조회 가능하지만, 리스트는 인덱스(번호)를 알아야함 따라서 관리하는 함수를 따로 작성해야함
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White','horsepower': 400,'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조(중첩 딕셔너리 구조)
# 코드 반복 지속, 중첩 문제가 있음(키), 키 조회 예외 처리 등 
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White','horsepower': 400,'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}},
]

print(car_dicts)
del car_dicts[1]
print(car_dicts)

print()
print()
print('----------')
# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용



class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 나중에 str랑 차이 좀 더 자세히 알아보기
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def __reduce__(self):
        pass
        
car1 = Car('Ferrari', {'color': 'White','horsepower': 400,'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})
print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# print(dir(car1))

print()
print()

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복((__str__)
for x in car_list:
    print(repr(x))
    # print(x)
    

