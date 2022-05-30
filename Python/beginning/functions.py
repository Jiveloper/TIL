# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법 
# def function_name(parameter):
#   code

# 예제1
def first_func(w):
    print("Hellow", w)

word = "Goodboy"

first_func(word)
print(first_func)

# 예제2
def return_func(w1):
    value = "Hello, " + str(w1)
    return value

test = return_func("Goodboy2")
print(test)


# 예제3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), q, list(q))

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul2(30)
print(type(p), p, set(q))

# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}

d = func_mul3(30)
print(type(d), d.get('v2'))

# 중요
# *args, **kwargs

# *args(언팩킹) 튜플
def args_func(*args): # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('--------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs(언팩킹) 딕셔너리 
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-------')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Kim', sendSMS=True)

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)

# 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)

# 람다식 예제
# 메모리 절약, 가독성, 이해하기 쉽고, 코드가 간결해진다 
# 일반적으로 함수는 객체를 생성하고 리소스(메모리) 할당
# 하지만 람다는 즉시 실행 함수로써 Heap 영역에 저장되고(Heap 초기화) -> 메모리 초기화
# 람다식은 효율적으로 메모리를 사용하는구나 정도로만 이해하고 넘어가기
# 다만 너무 남발 시 가독성이 오히려 감소되니 참고할것
# 함수가 좋으냐, 람다식이 좋으냐는 정답이 없는 문제

# def mul_func(x, y):
#     return x * y


# a = lambda x, y: x*y 
# print(a(5, 6))

# 일반적 함수에서 변수에 할당하는 상황
def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20,50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y:x*y 
print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print('>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x,y:x * y)

#파이썬 사용자 입력
#input 사용법
#기본 타입(str)

# 예제 1
# name = input("Enter Your Name: ")
# grade = input("Enter Your Grade: ")
# company = input("Enter Your Company Name: ")

# print(name, grade, company)

# 예제 2
# number = input("Enter number : ")
# name = input("Enter name : ")

# print("type of number", type(number))
# print("type of name", type(name))

# 예제 3(계산)
# first_number = int(input("Enter number : "))
# second_number = int(input("Enter number : "))

# total = first_number + second_number
# print("first_number + second number : ", total)

# 예제 4
# float_number = float(input("Enter a float number : "))
# print("input_float : ", float_number * 1.234)
# print("input_type : ", type(float_number))

# 예제 5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))