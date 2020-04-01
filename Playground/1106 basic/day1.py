# 입력
age = input('당신의 나이는 ? ')

# 출력
print("age is " + age)

# 변수
my_int = 1           # my_int 에 1을 넣는 것이 아니라, 1에 my_int 를 할당하는 것.
print(my_int + 4)


# 변수는 대소문자 구분
my_int = 'abc'
MY_int = 555
print(my_int, MY_int)

age = 2
print(age**10)      #  **은 제곱의 기능, age의 10제곱

# Boolean 자료형
tr = False


# 리스트
my_list = []
my_list = [1, 2, 3]
student = ['메이', 'Kelly', 'hwan', 'Philip']

for std in student:
    print(std)


# 랜덤을 import하고, 아래 random.choice를 통해서 임의로 선택할 수 있음.
import random
print(random.choice(student))


student.append("문지환")
for std in student:
    print(std)


student[0] = "바뀜"
print(student)


# tuple은 list랑 비슷한데, 안에있는 값을 바꿀 수 없음.
my_tuple = ('현선', '해웅', '지환', '지원')
# my_tuple[0] = "은지"  -> 이렇게 하면 에러가 난다.


# list, tuple, dictionary를 container라고한다.
# dictionary 는 key과 value의 쌍으로 이루어져 있음.
my_dic = {'지환': '여자', '현선': '남자', '지원': '여자'}
print(my_dic['지환']) # 여자 가 출력됨.

my_dic['지환'] = '남자'        # 지환이라는 key의 value 를 수정
print(my_dic['지환'])          # 수정된 value 출력


my_int = 1
print(type(my_int))     # 현재 my_int의 타입이 출력 'int'

print(float(my_int))    # 형변환이 이루어져서 float 형태로 1.0이 출력
print(str(my_int)*3)    # 여기서는 my_int가 string이라서 1을 3번 출력
print(my_int*3)         # 여기서는 my_int가 정수1이라서 1*3의 결과인 3이 출력


my_str = 'coding'
print(list(my_str))     # ['c', 'o', 'd', 'i', 'n', 'g']


