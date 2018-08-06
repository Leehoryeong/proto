import turtle
t=turtle.Turtle( )

screen = turtle.Screen()
a = screen.textinput("입력", "반지름")
# print(answer)
r= int(a)
# print(type(answer))
t.circle(r)
t.write(r**2*3.14) #반지름 값 표시
turtle.exitonclick()
