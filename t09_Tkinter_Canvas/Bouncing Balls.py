import math
import random
import tkinter as tk

COLORS = ["blue", "orange", "red", "green", "yellow", "purple", "cyan"]

class Ball:

    def __init__(self, canvas, x, y):
        self.canvas = canvas

        self.radius = random.randint(15, 30)
        self.color = random.choice(COLORS)
        self.x = x
        self.y = y

        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(3, 6)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

        self.id = self.canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill=self.color,
            outline="black",
        )

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.id, self.dx, self.dy)

    def check_wall_collisions(self, width, height):
        collided = False

        if self.x - self.radius <= 0:
            self.x = self.radius
            self.dx = abs(self.dx)
            collided = True
        elif self.x + self.radius >= width:
            self.x = width - self.radius
            self.dx = -abs(self.dx)
            collided = True

        if self.y - self.radius <= 0:
            self.y = self.radius
            self.dy = abs(self.dy)
            collided = True
        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.dy = -abs(self.dy)
            collided = True

        if collided:
            self.change_color()

        return collided

    def change_color(self):
        self.color = random.choice(COLORS)
        self.canvas.itemconfig(self.id, fill=self.color)


class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bouncing Balls з фізикою")
        self.root.geometry("800x600")

        # Стан гри
        self.balls = []
        self.is_paused = False
        self.collision_count = 0
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.create_widgets()
        self.canvas.bind("<Button-1>", self.create_ball)
        self.canvas.bind("<Configure>", self.on_resize)

        self.animate()

    def create_widgets(self):
        self.control_panel = tk.Frame(self.root, bg="#f0f0f0")
        self.control_panel.grid(row=0, column=0, sticky="ew")
        self.pause_btn = tk.Button(
            self.control_panel, text="Пауза", command=self.toggle_pause
        )
        self.pause_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = tk.Button(self.control_panel, text="Очистити екран", command=self.clear_screen)
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        self.stats_label = tk.Label(
            self.control_panel,
            text="Кульок: 0 | Зіткнень: 0",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
        )
        self.stats_label.pack(side=tk.RIGHT, padx=10)
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky="nsew")

    def create_ball(self, event):
        if self.is_paused:
            return

        new_ball = Ball(self.canvas, event.x, event.y)
        self.balls.append(new_ball)
        self.update_stats()

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_btn.config(text="Продовжити")
        else:
            self.pause_btn.config(text="Пауза")
            self.animate()  # Відновлюємо анімацію

    def clear_screen(self):
        self.canvas.delete("all")
        self.balls.clear()
        self.collision_count = 0
        self.update_stats()

    def update_stats(self):
        self.stats_label.config(
            text=f"Кульок: {len(self.balls)} | Зіткнень: {self.collision_count}"
        )

    def on_resize(self, event):
        pass

    def check_ball_collisions(self):
        num_balls = len(self.balls)
        for i in range(num_balls):
            for j in range(i + 1, num_balls):
                b1 = self.balls[i]
                b2 = self.balls[j]

                dx = b2.x - b1.x
                dy = b2.y - b1.y
                distance = math.hypot(dx, dy)
                min_dist = b1.radius + b2.radius

                if distance < min_dist:
                    self.collision_count += 1
                    self.update_stats()
                    b1.change_color()
                    b2.change_color()

                    if distance == 0:
                        continue

                    nx = dx / distance
                    ny = dy / distance

                    overlap = min_dist - distance
                    b1.x -= nx * overlap * 0.5
                    b1.y -= ny * overlap * 0.5
                    b2.x += nx * overlap * 0.5
                    b2.y += ny * overlap * 0.5

                    kx = b1.dx - b2.dx
                    ky = b1.dy - b2.dy
                    p = nx * kx + ny * ky

                    if p > 0:
                        b1.dx -= p * nx
                        b1.dy -= p * ny
                        b2.dx += p * nx
                        b2.dy += p * ny

    def animate(self):
        if self.is_paused:
            return
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        for ball in self.balls:
            ball.move()

        for ball in self.balls:
            if ball.check_wall_collisions(canvas_width, canvas_height):
                self.collision_count += 1
                self.update_stats()

        self.check_ball_collisions()
        self.root.after(16, self.animate)

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    app = Application()
    app.run()