import turtle #라이브러리 사용

t=turtle.Turtle()
t.shape("turtle") #모양설정

#사각형
# t.forward(100) #픽셀이동
# t.left(90)    #왼쪽각도
# t.forward(100) #그전의 명령어 끝난 기준에서 거북이 머리에서 각도 재설정
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

#삼각형
# t.forward(100)
# t.left(135)
# t.forward(80)
# t.left(90)
# t.forward(75)
#
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

#원그리그
# t.circle(100) #반지름이 100px인 원
t.circle(50)
t.forward(100)
t.circle(50)
t.forward(100)
t.circle(50)
t.forward(100)
t.right(45)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.exitonclick()
