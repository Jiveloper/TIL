# 클래스 개념
# OOP(객체 지향 프로그래밍란?, Self(인스턴스화 된 대상), 인스턴스 메소드(self를 인자로 받는 것들), 인스턴스 변수(self를 붙히고 선언)
# 왜사용하나? -> 생산성의 향상, 재사용을 극대화 시킴

# 클래스와 인스턴스 차이를 이해하는게 중요
# 네임스페이스는 객체를 인스터화 할때 저장된 공간(책상 서랍, 방)
# 클래스 변수는 직접 접근 가능하고 공유함
# 인스턴스 변수는 객체마다 별도로 존재함

# 예제1
# class Dog(): 이렇게 해도됨
# class Dog(object):
# class Dog:
#     pass
# class Dog():
#     pass
# class Dog(object):
#     pass
# 위 3가지 모두 상관없음 편안걸로 선언

class Dog: #object 상속
    # 클래스 속성
    species = 'firstdog' #클래스 변수 
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age): # name, age는 인스턴스 변수
        self.name = name
        self.age = age
# 클래스 정보
print(Dog)
    
# # 인스턴스화
# a = Dog("jiwon", 29)
# b = Dog("jiwonLee", 30)
# c = Dog("jiwon", 29)

# # 비교
# print(a == b, id(a), id(b), id(c))
# print(a == c)

# # 네임스페이스
# print('dog1', a.__dict__)
# print('dog2', b.__dict__)

# # 인스턴스 속성 확인
# print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))
# print(a.name)

# if a.species == 'firstdog':
#     print('{0} is a {1}'.format(a.name, a.species))

# print(Dog.species)
# print(a.species)
# print(b.species)
# 클래스 변수는 공유하고있음
# self는 별도 존재

# 예제2
# self의 이해
# class SelfTest: #여긴 왜 init 메소드가 없냐면, 없을경우 파이썬이 내부적으로 알아서 실행해줌. 위처럼 name 또는 age가 없고 기본적으로 사용할것임)
#     def func1():
#         print('Func1 called') #클래스메소드
#     def func2(self): #인스턴스 메소드
#         print(id(self))
#         print('Func2 called')

# f = SelfTest() #인스턴스화

# print(dir(f))
# print(id(f))
# # f.func1() #예외
# f.func2() #인스턴스를 호출
# # SelfTest.func1()
# # SelfTest.func2()
# SelfTest.func2(f) #인스턴스 메소드는 이렇게하던지

# 예제3
# 클래스 변수, 인스턴스 변수

class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고
    
    def __init__(self, name): #생성자
        #인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self): #소멸자
        Warehouse.stock_num -= 1
    
user1 = Warehouse('Lee') #인스턴스화
user2 = Warehouse('Cho') #인스턴스화

print(Warehouse.stock_num)
# Warehouse.stock_num = 50 # 직접 접근해서 수정하는건 좋지못함

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)
## 인스턴스 네임스페이스에 없으면 클래스 네임스페이스에 가서 찾아보고 거기에도 없으면 에러 발생
del user1 #인스턴스를 메모리에서 지우기
print('after', Warehouse.__dict__)

# 예제4
class Dog: #object 상속
    # 클래스 속성
    species = 'firstdog' #클래스 변수 
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age): # name, age는 인스턴스 변수
        self.name = name
        self.age = age
        
    def info(self): #메소드 생성
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스터스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)

# 메소드 호출
print(c.info())
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
