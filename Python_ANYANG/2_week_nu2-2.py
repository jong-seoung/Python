# 변수 course에 ‘python’을 저장하고, time에 3을 저장한 후 아래와 같이 출력하는 구문 3개를 대화형 모드에서 작성하고 화면을 캡처하세요.
# (f-string, +, ,를 이용한 3가지 구문)출력예) >>> 과목명은 python이고, 시수는 3시간입니다.

course = "python"
time = 3
print(f"과목명은 {course}이고, 시수는 {time}시간 입니다")
print("과목명은 " + course + "이고, 시수는" + str(time) +"시간 입니다")
print("과목명은",course,"이고, 시수는",time,"시간 입니다")