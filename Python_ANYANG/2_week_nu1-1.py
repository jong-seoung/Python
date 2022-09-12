import turtle as t

t.shape("turtle")

# 제일 큰 사각형
t.fillcolor("orange")
t.begin_fill()
t.goto(300,0)
t.goto(300,200)
t.goto(0,200)
t.goto(0,0)
t.end_fill()

# 위치 조정
t.penup()
t.goto(10,10)
t.pendown()

# 중간 사각형
t.fillcolor("blue")
t.begin_fill()
t.goto(290,10)
t.goto(290,150)
t.goto(10,150)
t.goto(10,10)
t.end_fill()

# 위치 조정 2
t.penup()
t.goto(20,20)
t.pendown()

# 작은 사각형
t.fillcolor("pink")
t.begin_fill()
t.goto(200,20)
t.goto(200,130)
t.goto(20,130)
t.goto(20,20)
t.end_fill()


t.done() #종료