# Python Study
<br>

## **Python Study basic**
<br>

##  **[chapter1. 자료형](https://github.com/jong-seoung/Python/blob/main/SelfStudy/dataType.py)**
<details>
<summary>상세 보기</summary>

**숫자형 자료형** 
<details>
<summary>코드 보기</summary>

```
print(5)
print(-10)
print(3.14)
print(1000)
print("5+3")
print(2*8)
print(3*(3+1))
```
</details>
<br>

**문자형 자료형**

<details>
<summary>코드 보기</summary>

```
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
```
</details>
<br>

**boolean 자료형** - 참과 거짓을 나타내줌

<details>
<summary>코드 보기</summary>

```
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not (5 > 10))
```
</details>
<br>

**변수**
<details>
<summary>코드 보기</summary>

```
animal = "강아지"
name = "연탄이"
age= 4
hobby = "산책"
is_adult= age > 3
print("변수 사용 X")
print("우리집 강아지이름은 연탄이에요.")
print("연탄이는 4살이며, 산책을 아주 좋아해요.")
print("연탄이는 어른일까요? True")

print("변수 사용 O")
print("우리집" + animal + "이름은" + name + "에요.")
print(name + "는" + str(age)+ "살이며," + hobby +"을 아주 좋아해요.")
print(name + "는 어른일까요?" + str(is_adult))
``` 
</details>
<br>

**주석**
```
# 주석 처리 하는법
```
**[퀴즈#1](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz1.py)**
```
변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수 값 : "사당", "신도림", "인천공항" 순서대로 입력
출력 문장 : OO 행 열차가 들어 오고 있습니다.
```
</details>

<br>

##  **[chapter2. 연산자](https://github.com/jong-seoung/Python/blob/main/SelfStudy/operatorEx.py)**
<details>
<summary>상세 보기</summary>

**연산자** - 제곱수, 나머지, 몫 구하는 방법 / and,or 연산자 사용법
<details>
<summary>코드 보기</summary>

```
print(1+1) 
print (3-2)
print(5*2)
print(6/3)


print(2**3) # 제곱수 구하기
print(5%3) # 나머지 구하기
print(5//3) #몫 구하기

print(10 > 3) # True
print( 4 >= 7) # False

print(3 == 3) # True
print(3 == 4) # False
print( 3 + 4 == 7) # True

print(1 != 3) # True 
print(not(1 != 3)) #False

#둘다 참일경우 참
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

#둘중 하나만 참이여도 참
print((3>0) or (3>5)) # True
print((3>0) | (3>5)) # True
```
</details>
<br>

**숫자 처리함수** - 절대값, 제곱수, 최대값, 최소값, 반올림, 버림, 올림, 제곱근
<details>
<summary>코드 보기</summary>

```
print(abs(-5)) # 절대값
print(pow(4,2)) # 제곱수 4^2
print(max(5,13)) # 최대값
print(min(5,12)) # 최소값
print(round(3.14)) # 반올림

from math import * 
print(floor(4.99)) # 버림
print(ceil (3.14)) # 올림
print(sqrt (16)) # 제곱근
```
</details>
<br>

**랜덤함수** - 랜덤 함수 불러오는 방법
<details>
<summary>코드 보기</summary>

```
from random import *

#미만과 이하 잘 보기
print(random()) # 0.0부터 1.0미만의 임의의 값 생성
print(random() * 10 ) # 0.0부터 10.0미만의 임의의 값 생성
print(int(random())) # 0부터 10미만의 임의의 값 생성 - 정수만
print(int(random()* 10 ) + 1 ) # 1부터 10이하의 임의의 값 생성
print(int(random() * 45 ) + 1 ) # 1부터 45이하의 임의의 값을 생성

print(randrange(1,46)) # 1부터 45이하의 임의의 값을 생성
print(randint(1,45)) # 1부터 45이하의 값을 생성해줌
```
</details>
<br>

**[퀴즈#2](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%232.py)**
```
당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로하고 1번은 오프라인으로 하기로 했습니다. 
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터터디 모임 날짜는 매월 X일로 선정되었습니다
```
</details>
<br>

## **[chapter3. 문자열 처리](https://github.com/jong-seoung/Python/blob/main/SelfStudy/stringEx.py)**
<details>
<summary>상세 보기</summary>

**문자열**
<details>
<summary>코드 보기</summary>

```
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고
파이썬은 쉬워요
"""
print(sentence3)
```
</details>
<br>

**슬라이싱** - 처음부터 n번째자리까지의 값 가지고 오기, 뒤에서부터 n번째자리까지의 값 가지고오기
<details>
<summary>코드 보기</summary>

```
jumin = "000516-1234567"

print("성별 : " + jumin[7])
print("출생년도 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) #처음부터 6자리 직전까지 가지고오기
print("뒤 7자리 : " + jumin[7:]) # 7자리부터 끝까지
print("뒤7자리 (뒤에서부터) : " + jumin[-7:] ) #맨뒤에 7번째부터 끝까지
```
</details>
<br>

**문자열처리함수** - 전부 소문자, 대문자 표시하는법 / 첫번째 자리 숫자가 대문자인지 / n이 있는 위치를 알아내는법 / 두번째 n이 있는 위치를 알아내는법 / 원하는 문자가 몇번 나오는지 알아내는법

<details>
<summary>코드 보기</summary>

```
Python = "Python is Amazing"
print(Python.lower()) # 전부 소문자로 표시
print(Python.upper()) # 전부 대문자로 표시
print(Python[0].isupper()) # 첫번째 자리 숫자가 대문자인지?
print(len(Python)) # 길이를 알려줌
print(Python.replace("Python","Java")) # Python이란 글자를 Java라는 글자로 바꿔줌

index = Python.index("n") # n이 있는 위치를 알려줌
print(index)
index = Python.index("n",index + 1) # 두번째 n이 있는 위치를 알려줌
print(index)

print(Python.find("n")) # index와 같은 역할을 하지만 원하는 글자가 없을경우 -로 표시해줌

print(Python.count("n")) #n이 몇번 나오는지 알려줌
```
</details>
<br>

**문자열포맷** - format함수 관련 
<details>
<summary>코드 보기</summary>

```
print("a","b")
print("a"+"b")

# 방법 1
print("나는 %d살입니다." %20) # %d뒤에는 정수 값만 넣을수 있음
print("나는 %s을 좋아해요" %"파이썬") 
print("Apple은 %c로 시작해요" %"A") # %c뒤에는 문자 값만 넣을수 있음
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

#방법2
print("나는{}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

#방법3
print("나는 {age}살이며,{color}색을 좋아해요".format(age= 20, color="빨간"))
print("나는 {age}살이며,{color}색을 좋아해요".format(color="빨간",age = 20))

#방법4 (v 3.6이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며,{color}색을 좋아해요")
```
</details>
<br>

**탈출문자** - 줄바꿈, 커서이동, 벡스페이스, 탭 관련 코드 
<details>
<summary>코드 보기</summary>

```
print("백문이 불여일견  \n 백견이 불여일타") # \n은 줄바꿈
print("저는 '백종성' 입니다.")
print('저는 "백종성" 입니다.')
print("저는 \"백종성\" 입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\jongseoung\\Documents\\Python\\SelfStudy>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple \rPine")

# \b : 백스페이스 열활(한글자 지움)
print("Redd\bApple")

# \t : 탭
print("Red \t Apple")
```
</details>
<br>

**[퀴즈#3](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%233.py)**
```
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예)
http://naver.com

조건1 : http://을 제외 -> naver.com
조건2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
조건3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자내 'e'의 갯수 + "!" 로 구상

생성된 비밀번호 예 : nav51!
```
</details>
<br>

##  **[chapter4. 자료구조](https://github.com/jong-seoung/Python/blob/main/SelfStudy/datastructure.py)**
<details>
<summary>상세 보기</summary>

**리스트** - [] 리스트 관련 명령어
<details>
<summary>코드 보기</summary>

```
from traceback import print_tb


subway = [10,20,30]
print(subway)

subway = [ "유재석" , "조세호" , "박명수"]
print(subway)

#조세호씨는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list=[ 3,4,6,1,2,5]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list= [ "조세호", 20 ,True]
print(mix_list)

#리스트 확장
num_list= [1,2,3,4,5]
num_list.extend(mix_list)
print(num_list)

cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) 
# print(cabinet[5]) 변수에 원하는 값이 없으면 오류가 나타나고 프로그램이 중지됨
# print(cabinet.get(5)) 변수에 값이 없으면 none이 표시되고 프로그램이 진행됨
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # True, False로 표시됨 ( 값이 있으면 True)

# 새로운 손님
print(cabinet)
cabinet["c-20"] = "조세호"

# 원래 있던 값에 넣으면 덮어쓰기 됨

# 간 손님
del cabinet["c-20"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key,value 쌍으로 출력
print(cabinet.items())

# 값 초기화
cabinet.clear()
print(cabinet)
```
</details>
<br>

**튜플** - () 튜플 관련 명령어
<details>
<summary>코드 보기</summary>

```
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") - 튜플은 add가 불가능함

#튜플 사용 예시
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
```
</details>
<br>

**세트** {} 세트 관련 명령어
<details>
<summary>코드 보기</summary>

```
# 중복이 안됨, 순서 없음
my_set={1,2,3,3,3}
print(my_set)

java= { "유재석", "김태호", "양세형"}
python = {"유재석","박명수"}

#교집합 (java와 python을 모두 할수 있는 개발자)
print(java&python)
print(java.intersection(python))

#합집합 (java나 python중 하나라도 할수 있는 개발자)
print(java | python)
print(java.union(python)) #순서가 없음

#차집합 (java는 할수있지만 python은 할수 없는 개발자)
print(java - python)
print(java.difference(python))

#python을 할 줄 아는사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹은 개발자
java.remove("김태호")
print(java)
```
</details>
<br>

**자료구조의 변경** - 자료 확인법, 자료구조 변경법
<details>
<summary>코드 보기</summary>

```
#자료 구조 확인
menu={"커피", "우유", "주스"}
print(menu, type(menu))

# 리스트로 변경
menu=list(menu)
print(menu, type(menu))

# 튜플로 변경
menu= tuple(menu)
print(menu, type(menu))

#세트로 변경
menu= set(menu)
print(menu, type(menu))
```
</details>
<br>

**[퀴즈#4](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%234.py)**

```
당신의 학교에서는 파이썬 코딩 대회를 추최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.

추천 프로그램을 작성하시오.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2: 댓글 내용과 상관없이 무작위로 추천하되 중복불가
조건3 random모듈의 shuffle와 sample을 활용

출력 예제
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
--축하합니다--
```

</details>
<br>

##  **[chapter5. 제어문](https://github.com/jong-seoung/Python/blob/main/SelfStudy/ControlStatement.py)**
<details>
<summary>상세 보기</summary>

**if 문** 
<details>
<summary>코드 보기</summary>

```
if weather == "비" or weather == "눈" :
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

temp = int(input("기온은 어때요?"))
if temp >= 30 :
    print("너무 더워요. 나가지마세요")
elif 10<= temp <30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else :
    print("너무 추워요 나가지마세요")
```
</details>
<br>

**for 문**
<details>
<summary>코드 보기</summary>

```
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in[0,1,2,3,4] :
    print("대기번호 : {0} ".format(waiting_no))

for waiting_no in range(7) :
    print("대기번호 : {0} ".format(waiting_no))

starbuck = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbuck :
    print("{0}, 커피가 준비되었습니다.".format(customer))
```
</details>
<br>

**while 문** - while문 과 무한반복문
<details>
<summary>코드 보기</summary>

```
customer = "토르"
index = 5
while index >= 1 :
    print("{0},커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")


<무한 반복>
customer= "아이언맨"
index=1
while True :
print("{0},커피가 준비되었습니다..호출{1}회".format(customer,index))
index -= 1

<조건까지 반복>
customer= "토르"
person = "unknown"

while person != customer :
    print("{0},커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
```
</details>
<br>

**cntinue 와 break**
<details>
<summary>코드 보기</summary>

```
absent = [2,3] #결석
no_book = [7] #책을 안가지고 옴
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(no_book))
        break
    print("{0}야, 책읽어봐".format(student))
``` 
</details>
<br>

**한줄로 for 문**
<details>
<summary>코드 보기</summary>

```
#출석 번호가 1 2 3 4, 앞에 100을 붙이기로함 -> 101. 102 ,103, 104
student = [1,2,3,4,5]
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
students=["Iron man", "Thor"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students=["Iron man", "Thor"]
students= [i.upper() for i in students]
print(students)
```
</details>
<br>

**[퀴즈#5](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%235.py)**
```
당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을때, 총 탑승 승객수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다
조건2 : 당신은 소요시간 5분~15분 사이의 승객만 매칭해야합니다.

(출력문예제)
[0] 1번째 손님 (소요시간 : 15분)
[0] 2번째 손님 (소요시간 : 9분)
[ ] 3번째 손님 (소요시간 : 27분)
[ ] 4번째 손님 (소요시간 : 35분)
[ ] 5번째 손님 (소요시간 : 34분)
...
[ ] 50번째 손님 (소요시간 : 45분)
총 탑승 승객 : 2분
```
</details>
<br>

##  **[chapter6. 함수](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Function.py)**
<details>
<summary>상세 보기</summary>

**함수** - 함수 정의하는법
<details>
<summary>코드 보기</summary>

```
def opena_ccount():
    print("새로운 계좌가 생성되었습니다.")
opena_ccount()
```
</details>
<br>

**전달값과 반환 값**
<details>
<summary>코드 보기</summary>

```
#입금
def deposite(balance,money):
    print("입금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance+money))
    return balance+money

#출금
def withdraw(balance, money):
    if balance >= money:  #잔액이 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("잔액이 부족합니다. 남은 잔액은 {0}입니다.".format(balance))

#출금 수수료
def withdraw_night(balance, money):
    commission = 100 #수수료100원
    return commission, balance - money - commission
balance =  0  #잔액

#1000원 입금
balance = deposite(balance,1000)

#500원 출금
balance = withdraw(balance, 500)

#저녘에는 수수료가 제외되고 출금되게
commission, balance = withdraw_night(balance, 300)
print("수수료는 {0}이며, 잔액은 {1}원 입니다.".format(commission, balance))

#1000원 출금 / 잔액이 부족할 경우
balance = withdraw(balance, 1000)
```
</details>
<br>

**기본 값**
<details>
<summary>코드 보기</summary>

```
def profile(name, age, main_lang):
    print("이름: {0}\t 나이: {1}\t 주 사용 언어: {2}"\
        .format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 27, "자바")

#같은 나이 같은 학년 같은반 같은수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t 나이: {1}\t 주 사용 언어: {2}"\
        .format(name,age,main_lang))

profile("유재석")
profile("김태호")
```
</details>
<br>

**키워드 값** - 가변인자
<details>
<summary>코드 보기</summary>

```
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(name="김태호", age=20, main_lang="파이썬")
#순서가 뒤 섞여 있어도 함수가 잘 전달됨

#가변인자 
# *을 사용하여 변수 선언 해주기
def profile(name,age,*language):
    print("이름: {0} \t나이: {1}\t".format(name,age),end="")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석",20,"파이썬","자바","c","c++")
profile("김태호",15,"파이썬","자바","","")
``` 
</details>
<br>

**지역변수와 전역변수**
<details>
<summary>코드 보기</summary>

```
gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun을 사용
    gun=gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계 근무를 나감
print("남은 총 : {0}".format(gun))

#return 사용
gun = 10

def checkpoint_ret(gun, soldiers): #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
```
</details>
<br>

**[퀴즈#6](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%236.py)**
```
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) X 키(m) x 22
여자 : 남자 : 키(m) X 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)

조건2 :  표준 체중은 소수점 둘째자리 까지 표시

출력 예제
키 175cm의 남자의 표준 체중은 67.38kg입니다.
```
</details>
<br>

##  **[chapter7. 입출력](https://github.com/jong-seoung/Python/blob/main/SelfStudy/InputOutput.py)**
<details>
<summary>상세 보기</summary>

**표준 입출력** - 정렬 하는 방법
<details>
<summary>코드 보기</summary>

```
print("python","Java", sep=",")
print("python","Java", sep=" vs ")
print("python","Java","JavaScript", sep=",")
print("python","Java", sep=",",end="?") #end의 문장의 끝부분을 " " 값으로 바꿔달라
print("무엇이 더 재미있을까요?")

from ast import While
from pickle import TRUE
import profile
import sys
print("python","Java", file=sys.stdout) #표준 출력으로 문장이 찍힘
print("python","Java", file=sys.stderr) #표준 에러로 문장이 찍힘

# 시험 성적
scores= {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":") # ljust - ()의 수 만큼 공간을 만들고 왼쪽으로 정렬 / rjust - ()의 수 만큼 공간을 만들고오른쪽으로 정렬 

#은행 대기 순번표
#001,002,003,004,...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # Zfill(3) - 3만큼의 공간을 확보하고 빈공간에는 0으로 채우기

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 {0} 입니다.".format(answer))
print(type(answer)) #사용자 입력을 통해 정해진 값은 항상 문자열 형태로 정해짐
```
</details>
<br>

**다양한 출력 포맷** - 빈공간 확보, +-표시, 정렬, n자리마다 콤마, 소수점 출력
<details>
<summary>코드 보기</summary>

```
# 빈자리는 빈 공간으로 두고, 오른쪽 정렬하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일때는 +로 표시, 음수 일때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽으로 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 세자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000))

# 세자리마다 콤마를 찍어주기, +-부호도 붙여주기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))

# 세자리마다 콤마를 찍어주기, +-부호도 붙여주기, 자리수 확보 
print(("{0:^<+30,}").format(10000000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))
```
</details>
<br>

**파일 입출력** - 파일 쓰기, 읽기, 덮어쓰기 관련 코드
<details>
<summary>코드 보기</summary>

```
# "w"는 쓰기 용도
score_file = open("score.txt","a",encoding= "utf-8") 
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# "a"는 덮어쓰기 용도
score_file = open("score.txt","a",encoding= "utf-8") 
score_file.write("과학:80")
score_file.write("\n코딩:100")
score_file.close()

# 파일에 있는 내용을 한번에 읽어줌
score_file = open("score.txt","r",encoding="utf-8")
print(score_file.read())
score_file.close()

#파일에 있는 내용을 한줄씩 읽어줌
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline() #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
    if not line:
        break
    print(line,end="")
score_file.close()

# list 형태로 저장
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
```
</details>
<br>

**pickle**
<details>
<summary>코드 보기</summary>

```
import pickle
profile_file = open("profile.pickle","wb")
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
profile_file.close

# file에 있는 정보를 profile에 불러오기
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close
``` 
</details>
<br>

**with** - 간편하게 파일을 읽고 쓰는법
<details>
<summary>코드 보기</summary>

```
#파일을 읽고 쓰는데 두줄로 해결되고 매번 close를 사용하지 않아도 되서 좋음

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf-8") as study_file:
    study_file.write("파이썬 공부를 열심히 하고있어요.")

with open("study.txt","r",encoding="utf-8") as study_file:
    print(study_file.read())
```
</details>
<br>

**[퀴즈#7](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%237.py)**
```
당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- x 주차 주간보고 - 
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
```
</details>
<br>

##  **[chapter8. 클래스](https://github.com/jong-seoung/Python/blob/main/SelfStudy/InputOutput.py)**
<details>
<summary>상세 보기</summary>

**클래스** - 클래스 설정
<details>
<summary>코드 보기</summary>

```
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
from ast import Pass


name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다".format(name))
print("체력은 {0}, 공격력{1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드/ 시즈모드가 있음
tank_name = "탱크"
tank_hp= 150
tank_damage = 35

tank2_name =  "탱크"
tank2_hp= 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다".format(tank_name))
print("체력은 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(name,location,damage))

attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)
attack(tank2_name,"1시",tank2_damage)
```
</details>
<br>

**__init__** - 
<details>
<summary>코드 보기</summary>

```
class Unit:
    def __init__(self, name, hp, damage): # __init__ 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다".format(self.name))
        print("체력은 {0}, 공격력{1}".format(self.hp, self.damage))

marine1 = Unit("마린",40, 5)
marine2 = Unit("마린",40, 5)
tank = Unit("탱크",150, 35)
```
</details>
<br>

**멤버변수**
<details>
<summary>코드 보기</summary>

```
# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80,5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것 (빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))  / wraith1은 클로킹 상태가 아니기때문에 오류가 뜸
```
</details>
<br>

**메소드**
<details>
<summary>코드 보기</summary>

```
class Unit:
    def __init__(self, name, hp, damage): # __init__ 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다".format(self.name))
        print("체력은 {0}, 공격력{1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def Attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : {1} 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#파이어뱃 : 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.Attack("5시")

#공격을 2번 받는다고 가장
firebat1.damaged(25)
firebat1.damaged(25)
``` 
</details>
<br>

**상속**
<details>
<summary>코드 보기</summary>

```
class Unit:
    def __init__(self, name, hp, speed): # __init__ 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage,speed):
        Unit.__init__(self, name, hp,speed) # Unit의 클래스를 상속 받아서 사용

        # self.name = name
        # self.hp = hp
        self.damage = 
```
</details>
<br>

**다중상속**
<details>
<summary>코드 보기</summary>

```
#날수있는 기능을 가진 클라스
class Flyable:
    def __init__(self, flying_speed):
        self.fly_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.fly_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, fly_speed)

    def move (self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#발키리 : 공중유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name , "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture= AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500,25,3)

vulture.move("11시")
battlecruiser.move("9시")
```
</details>
<br>

**메소드 오버라이딩 , pass**
<details>
<summary>코드 보기</summary>

```
#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Pass

# 서플라이 디폿 : 건물, 1개 건물 = 8유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

#super

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) #다중 상속을 받을경우 마지막에 상속받는 클라쓰에 대해서만 임의 상수가 호출됨
        self.location = location
```
</details>
<br>

**[스타크래프트 프로젝트](https://github.com/jong-seoung/Python/blob/main/SelfStudy/StarCraft.py)**
<details>
<summary>코드 보기</summary>

```
# 일반 유닛
from random import randint


class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : {1} 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage,speed):
        Unit.__init__(self, name, hp,speed) # Unit의 클래스를 상속 받아서 사용

        # self.name = name
        # self.hp = hp
        self.damage = damage

    def Attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("현재 {0}의 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.fly_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.fly_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, fly_speed)

    def move (self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    #스팀팩 : 일정시간동안 이동 및 공격 속도를 증가, 체력 10감소
    def stimpack(self):
        if self.hp >=10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다.(HP 10감소)".format(self.name))
        else:
            print("{0} : 스팀팩을 사용할수 없습니다.(최소 HP : 10)".format(self.name))

#탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동불가.
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 2)
        self.seize_developed = False

    def set_seize_developed(self):
        if Tank.seize_developed == False:
            return
        
        #현재 시즈모드가 아닐때 --> 시즈모드
        if self.seize_developed == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        #현재 시즈모드 일때, 시즈 모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        
#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,5,2)
        self.clocked = False # 클로킹 모드 (해제 상태)
    
    def clocking(self):
        if self.clocked == True:  #클로킹 모드 --> 모드 해제
            print("{0} : 클로킹 모드를 해제 합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 시작 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player :  GG")
    print("[Player]님이 퇴장하셨습니다.")

game_start()
#마린 3기 생성
m1= Marine()
m2= Marine()
m3= Marine()

#탱크 2기 생성
t1=Tank()
t2=Tank()

#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리 (생성된 모든 유닛 append)
Attack_Unit = []
Attack_Unit.append(m1)
Attack_Unit.append(m2)
Attack_Unit.append(m3)
Attack_Unit.append(t1)
Attack_Unit.append(t2)
Attack_Unit.append(w1)

# 전군 이동
for Unit in Attack_Unit:
    Unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed =True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린: 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for Unit in Attack_Unit:
    if isinstance(Unit, Marine):
        Unit.stimpack()
    if isinstance(Unit, Tank):
        Unit.set_seize_developed()
    if isinstance(Unit, Wraith):
        Unit.clocking()

# 전군 공격
for Unit in Attack_Unit:
    Unit.Attack("1시")

# 전군 피해
for Unit in Attack_Unit:
    Unit.damaged(randint(5,21)) #공격은 랜덤으로 받음(5~20)

# 게임 종료
game_over()
```
</details>
<br>

**[퀴즈#8](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%238.py)**
```
주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파드 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
```
</details>
<br>

##  **[chapter9. 예외 처리](https://github.com/jong-seoung/Python/blob/main/SelfStudy/exceptionHandling.py)**
<details>
<summary>상세 보기</summary>

**예외 처리** - try, except 관련 코드
<details>
<summary>코드 보기</summary>

```
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 오류가 발생하였습니다.")
    print(err)
```
</details>
<br>

**에러 발생 시키기** - 에러 발생시 원하는 동작 실행하는법
<details>
<summary>코드 보기</summary>

```
try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = (int(input("첫 번째 숫자를 입력하세요 : ")))
    num2 = (int(input("두 번째 숫자를 입력하세요 : ")))
    if num1 >= 10 or num2 >=10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
```
</details>
<br>

**사용자 정의 예외처리 / finally** - 에러 발생시 원하는 동작 실행하는법 / 마지막 동작 실행하는법 
<details>
<summary>코드 보기</summary>

```
class BigNumberError(Exception):
    pass
#출력하기 원하는 메시지를 나타내는법
    # def __init__(self, msg):      
    #     self.msg = msg

    # def __str__(self):
    #     return self.msg
        
try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = (int(input("첫 번째 숫자를 입력하세요 : ")))
    num2 = (int(input("두 번째 숫자를 입력하세요 : ")))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError  #("입력값 : {0}, {1}".format(num1, num2)) 출력하기 원하는 메시지를 나타내는법
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except BigNumberError : # as err 출력하기 원하는 메시지를 나타내는법
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
#   print(err) 출력하기 원하는 메시지를 나타내는법
finally:
    print("계산기를 이용해주셔서 감사합니다.")
```
</details>
<br>

**[퀴즈#9](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%239.py)**
```
동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동주문 시스템을 제작하였습니다
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오

조건 1: 1보다 작거나 숫자가 아닌 입력값이 들어올때는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건 2: 대기 손님이 주물할수 있는 총 치킨량은 10마리로 한정
        치킨 소진시 사용자 정의 에러[SoldOutError]를 발생 시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다." 
```
</details>
<br>

##  **chapter10. 모듈과 패키지** 
<details>
<summary>상세 보기</summary>

- **모듈 : 하나의 파이썬 파일**
- **패키지: 모듈이 여러개 모여있는 것**
- **[모듈 과 패키지](https://github.com/jong-seoung/Python/tree/main/SelfStudy/theater_module)**
(영화관 입장료 계산)

**[내장함수 & 외장함수(os)](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Internal%2CExternalFunction.py)**
<details>
<summary>코드 보기</summary>

```
# 내장 함수

input : 사용자 입력을 받는 함수
dir : 어떤 객채를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

# 외장 함수

#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
from email.utils import localtime
import glob
print(glob.glob("*.py")) #파일 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더 입니다.")
    os.rmdir(folder)
    print(folder,"폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) #폴더 생성
    print(folder,"폴더를 생성하였습니다.")

#시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H%m%S"))

import datetime
print("오늘 날짜는",datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() #오늘의 날짜
td = datetime.timedelta(days=100) #100일 저장
print("우리가 만난지 100일은",today + td) #오늘로 부터 100일 뒤
```
</details>
<br>

**[퀴즈#10](https://github.com/jong-seoung/Python/blob/main/SelfStudy/Quiz%2310.py)** 
<br>
**[퀴즈# 10모듈 파일](https://github.com/jong-seoung/Python/blob/main/SelfStudy/byme.py)**
```
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

#조건 : 모듈 파일명은 byme.py로 작성 

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 000에 의해 만들어 졌습니다.
# 유튜브 :
# 이메일 :
```

</details>
<br>