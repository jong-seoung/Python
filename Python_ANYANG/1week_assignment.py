import turtle # 함수 라이브러리 불러오기

t = turtle.Turtle() 

# 수학적 xy좌표 사용 , x축 -600~600 / y축 -600~600

t.shape("turtle") # 아이콘 모양을 결졍
t.forward(200) # x축으로 200px만큼 이동
t.left(90) # 좌측으로 90도 만큼 회전 / 이동하지않고 방향만 전환
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

turtle.done() #종료