from turtle import Turtle


class Snake:
    def __init__(self):
        squares = []
        self.squares = squares
        self.length = length = 0
        for _ in range(0, 3):
            square = Turtle(shape="square")
            square.color("green")
            square.penup()
            squares.append(square)
            if _ > 0:
                length -= 20
                squares[_].goto(length, 0)
        self.head = self.squares[0]

    def move(self):
        for num in range(len(self.squares) - 1, 0, -1):
            self.squares[num-1].shapesize(stretch_len=1, stretch_wid=1)
            new_x = self.squares[num - 1].xcor()
            new_y = self.squares[num - 1].ycor()
            self.squares[num].goto(new_x, new_y)
        self.squares[0].forward(20)

    def tail(self):
        square = Turtle(shape="square")
        square.shapesize(stretch_len=0.01, stretch_wid=0.01)
        square.color("green")
        square.penup()
        self.squares.append(square)

    def up(self):
        self.squares[0].setheading(90)

    def down(self):
        self.squares[0].setheading(270)

    def right(self):
        self.squares[0].setheading(0)

    def left(self):
        self.squares[0].setheading(180)
