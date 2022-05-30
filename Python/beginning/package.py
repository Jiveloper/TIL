# 파이썬 패키지(폴더의 개념임)
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리), (현재 디렉토리) -> 모듈 내부에서만 사용

# 사용방법
#풀네임
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

#자주씀
from sub.sub1 import module1
module1.mod1_test1()
module1.mod1_test2()

#간단하게 쓸수도있음 별칭으로
from sub.sub2 import module2 as m2 # alias 별칭 
m2.mod2_test1()
m2.mod2_test2()

#모든 파일 접근
#간편하긴한데 모두 임포트하기때문에 필요한것만 사용하는게 좋음 
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module1.mod2_test1()
module1.mod2_test2()

# 파이캐시는 런타임환경때 빠른 실행을 위해 파이썬이 만들어주는거임 지워도 괜찮음 실행하면 또생김
#패키지에 있는 __init__py 용도는  python 3.3부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성을 추천함
#파이썬한테 이건 패키지이고 임포트해서 쓸수있어라고 빈 init 파일을 만들어놔야함(파이썬 3.3까지)
#아니면 임포트할때 가지고오지 못함
#근데 3.7부터는 없어도됨. 다 지워도 동작함
#다만 만든것들을 누군가한테 줄때 하위호환을 위해 빈 init 파일 생성해주면 좋음
#파이썬이 init 파일을 먼저 검사함
#__all__ = ['module2', 'module3']
# 버그가 많은 모듈은 위처럼 제한