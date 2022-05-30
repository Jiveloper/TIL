#예외와 에러는 다르다 
#숫자만 입력해야하는데 문자 특수문자 같은게 입력되면 예상치못한 예외가 발생하는것
#아이디와 비밀번호가 틀리지 않았는데 로그인이 안되는 예측 가능한 예외
#OS에서 발생하는 예측 불가능한 예외
#에러는 운영환경에서 발생한다
#정전이된다거나 메인보드나 하드웨어가 고장이나거나

#Chapter07-1
#파이썬 예외처리의 이해
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('erro)
# print('error'))
# if True
#     pass

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[5])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError
# dic = {'name':'Lee', 'Age':29, 'City':'Busan'}
# print(dic['name'])
# print(dic.get('hobby'))

# 예외가 없는 가정하고 일단 프로그램을 작성해라 그다음 런타임(프로그램을 실행할때) 예외 발생 시 예외 처리를 권장한다(EAFP 문서 가이드)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# print(time.time())
# import time
# print(time.time2())

# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'
# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))
# print(x + list(z))

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
#finally : 항상 마지막에 실행
#try-except-finally

name = ['Jiwon', 'Kim', 'Park']

#예제1 ValueError
# try: #내코드는 정확해도 다른걸 가져올때 문제가생기는 코드를 넣어주기(외부 커넥션 연결, 크롤링, 다른쪽 서버 등등)
#     z = 'j'
#     x = name.index(z)
#     print('Found it! {} in {} name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print('pass')

# #예제2 모든에러 다잡기 Exception 쓰거나, 아무것도 안쓰기 단 어떤에러인진 예측 불가
# try: #내코드는 정확해도 다른걸 가져올때 문제가생기는 코드를 넣어주기(외부 커넥션 연결, 크롤링, 다른쪽 서버 등등)
#     z = 'j'
#     x = name.index(z)
#     print('Found it! {} in {} name'.format(z, x + 1))
# except Exception:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print('pass')

# #예제3 앨리아스 주고 출력하면 에러 나옴
# try: #내코드는 정확해도 다른걸 가져올때 문제가생기는 코드를 넣어주기(외부 커넥션 연결, 크롤링, 다른쪽 서버 등등)
#     z = 'z'
#     x = name.index(z)
#     print('Found it! {} in {} name'.format(z, x + 1))
# except Exception as e:
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else: #예외가 발생하지 않아야 실행함
#     print('Ok! else.')
# finally: # 예외가 발생해도 무조건 한번 실행함. 마지막에 꼭 작업해줘야할때 필요. 사이트에 연결했거나 소켓끼리 연결되었거나 데이터베이스에 연결되었을때 예외가 발생했을때 커넥션, 풀이 차기때문에 릭, 메모리누수 런타임때 에러 발생
#     print('Ok! finally')

# print('pass')

#예제4 
# 예외를 일부로 발생 raise
# raise 키워드로 예외 직접 발생
# 파이썬 문법의 에러가 아니라 회사 내부의 정책에 의해(논리적인 룰에 의해)발생시키고자 할때 사용
# 프로그램 설계 상 들어오면 안되는 값이 들어오거나, 숫자의 범위가 내가 생각한것보다 클 경우 예외로 간주해야해 할때 사용
try:
    a = 'Kim'
    if a == 'jn':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occured! Exception!')
else:
    print('Ok! else!')