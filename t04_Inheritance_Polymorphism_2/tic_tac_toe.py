import turtle


class Figure:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def draw(self, color):
        pass

    def show(self):
        self.draw("black")

    def hide(self):
        self.draw("white")


class Board(Figure):
    def draw(self, color):
        self.t.pencolor(color)
        self.t.pensize(5)
        for i in range(2):
            self.t.penup()
            self.t.goto(-50 + i * 100, 150)
            self.t.pendown()
            self.t.goto(-50 + i * 100, -150)
            self.t.penup()
            self.t.goto(-150, 50 - i * 100)
            self.t.pendown()
            self.t.goto(150, 50 - i * 100)

class Cross(Figure):
    def draw(self, color):
        self.t.pencolor(color)
        self.t.pensize(3)
        size = 30
        self.t.penup()
        self.t.goto(self.x - size, self.y - size)
        self.t.pendown()
        self.t.goto(self.x + size, self.y + size)
        self.t.penup()
        self.t.goto(self.x - size, self.y + size)
        self.t.pendown()
        self.t.goto(self.x + size, self.y - size)



class Zero(Figure):
    def draw(self,color):
        self.t.pencolor(color)
        self.t.pensize(3)
        self.t.penup()
        self.t.goto(self.x, self.y - 35)
        self.t.pendown()
        self.t.circle(35)

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(400, 400)
        self.board = Board()
        self.board.show()
        self.game_over = False

        self.turn = "X"
        self.grid = [None] * 9
        self.screen.onclick(self.handle_click)
        self.screen.listen()


    def check_winner(self):
        win_coords = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in win_coords:
            if self.grid[a] == self.grid[b] == self.grid[c] and self.grid[a] is not None:
                print(f"Гравець {self.grid[a]} переміг!")
                return True

        if None not in self.grid:
            print("Нічия!")
            return True

        return False

    def handle_click(self, x, y):
        if self.game_over:
            return
        col = int((x + 150) // 100)
        row = int((150 - y) // 100)

        if 0 <= col < 3 and 0 <= row < 3:
            index = row * 3 + col
            if self.grid[index] is None:
                cx = -100 + col * 100
                cy = 100 - row * 100

                if self.turn == "X":
                    fig = Cross()
                    self.grid[index] = "X"
                    self.turn = "O"
                else:
                    fig = Zero()
                    self.grid[index] = "O"
                    self.turn = "X"

                fig.setPosition(cx, cy)
                fig.show()
            else:
                cx = -100 + col * 100
                cy = 100 - row * 100
                if self.grid[index] == "X":
                    fig = Cross()
                    self.grid[index] = None
                    self.turn = "O"
                else:
                    fig = Zero()
                    self.grid[index] = None
                    self.turn = "X"
                fig.setPosition(cx, cy)
                fig.hide()
            if self.check_winner():
                self.game_over = True



if __name__ == "__main__":
    game = Game()
    turtle.done()