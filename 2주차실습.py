# 다음 프로그램을 실행한 결과 화면을 캡쳐하여 하나의 pdf 파일로 제출
# 1 주차의 강의 자료에 있는 샘플 프로그램, Lab, 연습문제, 실습문제 중 50% 이상
# 첨부 파일에 있는 실습 문제는 100%


# Lab : print() 함수 실습

print("파이썬에 오신 것을 환영합니다.")
print("파이썬은 쉽습니다.")
print("파이썬으로 빅데이터, 인공지능 프로그램을 작성할 수 있습니다.")

# Lab : 간단한 계산

print("2+3=",2+3)
print("2-3=",2-3)
print("2*3=",2*3)
print("2/3=",2/3)

# Lab : 오류를 처리해보자

print("안녕하세요?")
print("이번 코드에는 많은 오류가 있다네요")
print("제가 다 고쳐 보겠습니다.")


# Lab : 원기둥의 부피 계산

PI = 3.14
radius = 5
height = 10

volume = PI * radius * radius * height

print("반지름=", radius, "높이=", height, "원기둥의 부피=", volume)


# 지수 계산
a = 1000
r = 0.05
n = 10
result = a*(1+r)**n

print("원리금 합계=", result)


# Lab : 복리 계산

init_money = 24
interest = 0.06
years = 382
print(init_money*(1+interest)**years)


# 반올림 - 물건 값의 7.5%가 부가세라고 하자. 물건값이 12345원일 때, 부가세를 소수점 2번째 자리까지 계산하는 프로그램

price = 12345
tax = price * 0.075
tax = round(tax, 2)
print(tax)


# Lab : 로봇 기자 만들기 - 사용자에게 경기장, 점수, 이긴 팀, 진 팀, 우수 선수를 질문하고 변수에 저장한다. 이들 문자열에 문장을 붙여서 기사를 작성한다.

stadium = input("Where is stadium?")
winner = input("Which team wins?")
loser = input("Which team loses?")
vip = input("Who is the MVP?")
score = input("What's the result of the game?")

print("")
print("====================================")
print("오늘", stadium, "에서 야구 경기가 열렸습니다.")
print(winner, "과", loser, "은 치열한 공방전을 펼쳤습니다.")
print(vip, "이 맹활약을 하였습니다.")
print("결국", winner, "가", loser, "를", score, "로 이겼습니다.")
print("====================================")


# 변수와 문자열을 동시에 출력할 때

x = 100
y = 200
print(f"{x}와 {y}의 합 = {x+y}")


# 형식화된 출력

SQMETER_PER_P = 3.3

area = eval(input("면적(제곱미터):"))
py = area / SQMETER_PER_P
print("%.2f평" % py) # 출력 7.76평



# Lab : 대화하는 프로그램 만들기 - 변수를 사용하여 사용자의 이름과 나이를 문자열 형태로 기억했다가 출력할 때 사용하는 프로그램을 작성해보자.

print("안녕하세요?")
name = input("이름이 어떻게 되시나요?")
print("만나서 반갑습니다. "+name+"씨")

print("이름의 길이는 다음과 같군요:", len(name))

age = int(input("나이가 어떻게 되나요?"))
print("내년이면"+str(age+1)+"이 되시는군요.")


# Lab : BMI 계산하기 - 사용자로부터 신장과 체중을 입력받아서 체질량지수 값을 출력하는 프로그램을 작성해 보자

weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))

bmi = (weight / (height**2))
print("당신의 BMI=", bmi)


# Lab : 구의 부피 계산하기 - 반지름이 5m인 구의 부피를 계산하는 프로그램을 작성해보자.

r = float(input("반지름을 입력하시오: "))

volume = (4.0/3.0) * 3.141592 * r**3

print("구의 부피 =", volume)



# Lab : 자동판매기 프로그램 - 자동 판매기를 시뮬레이션 하는 프로그램을 작성하여 보자.

itemPrice = int(input("물건값을 입력하시오: "))
note = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))

change = note*1000 + coin500*500 + coin*100 - itemPrice

# 거스름돈(500원동전개수)을 계산한다
nCoin500 = change//500
change = change%500
# 거스름돈(100원동전개수)을 계산한다
nCoin100 = change//100
change = change%100
# 거스름돈(10원동전개수)을 계산한다
nCoin10 = change//10
change = change%10
# 거스름돈(1원동전개수)을 계산한다
nCoin1 = change

print("500원=", nCoin500, "100원=", nCoin100, "10원=", nCoin10, "1원=", nCoin1)



# 실습파일(전부 해야 함)
# 1. 1+2+3을 계산하면 6이 된다.



# 2. 전체 다리의 수는?

print('닭의 수:')
x = int(input())
print('돼지의 수:')
y = int(input())
print('소의 수:')
z = int(input())
print('전체 다리의 수:', x*2+y*4+z*4)


# 3. 시간과 분을 입력 받아, 초로 변환하라

# 4. 두 점의 좌표를 받아 두 점 사이의 거리 계산

# 5. 4자리의 정수를 입력 받아 자리수 합 계산

# 6. 100000~999999인 정수 입력 받아 천단위 구분 쉼표 넣어서 화면에 출력