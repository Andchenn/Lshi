import turtle

# 绘制图形时的宽度
turtle.pensize(3)
# 移动时不绘制图形,提起笔，用于另起一个地方绘制时用
turtle.penup()
# 将画笔移动到坐标为x,y的位置
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()
