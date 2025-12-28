import turtle as tl
import time
import winsound   # Windows only sound

class PONG:
    def __init__(self):
        self.player_name = input("Enter your name: ")
        self.level_speed = self.select_level()

        self.player_score = 0
        self.computer_score = 0
        self.start_time = time.time()
        self.game_paused = False
        self.game_over = False

        self.create_window()
        self.leftpaddle()
        self.rightpaddle()
        self.create_ball()
        self.create_scoreboard()
        self.keys()
        self.game()

    # ---------------- LEVEL ----------------
    def select_level(self):
        print("\nSelect Level:")
        print("1. Easy\n2. Medium\n3. Hard")
        ch = input("Enter choice: ")
        return {"1": 0.08, "2": 0.15, "3": 0.25}.get(ch, 0.15)

    # ---------------- WINDOW ----------------
    def create_window(self):
        self.root = tl.Screen()
        self.root.title("PONG GAME | Player vs Computer")
        self.root.bgcolor("black")
        self.root.setup(width=600, height=400)
        self.root.tracer(0)

    # ---------------- PADDLES ----------------
    def leftpaddle(self):
        self.left_paddle = tl.Turtle()
        self.left_paddle.shape("square")
        self.left_paddle.color("cyan")
        self.left_paddle.shapesize(5, 1)
        self.left_paddle.penup()
        self.left_paddle.goto(-280, 0)

    def rightpaddle(self):
        self.right_paddle = tl.Turtle()
        self.right_paddle.shape("square")
        self.right_paddle.color("red")
        self.right_paddle.shapesize(5, 1)
        self.right_paddle.penup()
        self.right_paddle.goto(280, 0)

    # ---------------- BALL ----------------
    def create_ball(self):
        self.ball = tl.Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball_dx = 0.2
        self.ball_dy = 0.2

    # ---------------- SCORE & TIMER ----------------
    def create_scoreboard(self):
        self.score = tl.Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 160)
        self.update_score()

    def update_score(self):
        remaining = max(0, 60 - int(time.time() - self.start_time))
        self.score.clear()
        self.score.write(
            f"{self.player_name}: {self.player_score}   Computer: {self.computer_score}   Time: {remaining}s",
            align="center",
            font=("Arial", 14, "bold")
        )

    # ---------------- CONTROLS ----------------
    def left_up(self): self.left_paddle.sety(self.left_paddle.ycor() + 20)
    def left_down(self): self.left_paddle.sety(self.left_paddle.ycor() - 20)

    def pause_game(self):
        self.game_paused = not self.game_paused

    def restart_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.start_time = time.time()
        self.ball.goto(0, 0)
        self.game_over = False

    def keys(self):
        self.root.listen()
        self.root.onkeypress(self.left_up, "w")
        self.root.onkeypress(self.left_down, "s")
        self.root.onkeypress(self.pause_game, "p")     # Pause
        self.root.onkeypress(self.restart_game, "r")   # Restart

    # ---------------- AI ----------------
    def computer_ai(self):
        if self.right_paddle.ycor() < self.ball.ycor():
            self.right_paddle.sety(self.right_paddle.ycor() + self.level_speed * 50)
        elif self.right_paddle.ycor() > self.ball.ycor():
            self.right_paddle.sety(self.right_paddle.ycor() - self.level_speed * 50)

    # ---------------- WINNER ----------------
    def show_winner(self):
        self.game_over = True
        msg = "DRAW!"
        if self.player_score > self.computer_score:
            msg = f"{self.player_name} WINS 🎉"
        elif self.player_score < self.computer_score:
            msg = "COMPUTER WINS 🤖"

        self.score.goto(0, 0)
        self.score.write(msg, align="center", font=("Arial", 20, "bold"))

    # ---------------- GAME LOOP ----------------
    def game(self):
        while True:
            self.root.update()

            if self.game_paused or self.game_over:
                continue

            # Timer
            if time.time() - self.start_time >= 60:
                self.show_winner()
                continue

            self.ball.setx(self.ball.xcor() + self.ball_dx)
            self.ball.sety(self.ball.ycor() + self.ball_dy)
            self.computer_ai()

            # Wall collision
            if self.ball.ycor() > 190 or self.ball.ycor() < -190:
                self.ball_dy *= -1
                winsound.Beep(800, 100)

            # Score
            if self.ball.xcor() > 290:
                self.ball.goto(0, 0)
                self.ball_dx *= -1
                self.player_score += 1
                winsound.Beep(1000, 150)
                self.update_score()

            if self.ball.xcor() < -290:
                self.ball.goto(0, 0)
                self.ball_dx *= -1
                self.computer_score += 1
                winsound.Beep(400, 150)
                self.update_score()

            # Paddle collision
            if (-260 < self.ball.xcor() < -240 and
                self.left_paddle.ycor() - 50 < self.ball.ycor() < self.left_paddle.ycor() + 50):
                self.ball_dx *= -1
                winsound.Beep(900, 100)

            if (240 < self.ball.xcor() < 260 and
                self.right_paddle.ycor() - 50 < self.ball.ycor() < self.right_paddle.ycor() + 50):
                self.ball_dx *= -1
                winsound.Beep(900, 100)

            self.update_score()


def main():
    PONG()

if __name__ == "__main__":
    main()
