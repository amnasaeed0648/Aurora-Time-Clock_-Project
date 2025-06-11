import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Brown & White Analog Clock")
        self.canvas_size = 400
        self.center = self.canvas_size // 2
        self.radius = self.canvas_size // 2 - 20

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")

        # Draw clock face (white inside with brown outline)
        self.canvas.create_oval(
            self.center - self.radius, self.center - self.radius,
            self.center + self.radius, self.center + self.radius,
            fill='white', outline='sienna', width=8
        )

        # Draw clock numbers in brown
        for num in range(1, 13):
            angle = math.pi / 6 * (num - 3)
            x = self.center + int(self.radius * 0.8 * math.cos(angle))
            y = self.center + int(self.radius * 0.8 * math.sin(angle))
            self.canvas.create_text(x, y, text=str(num), fill='sienna', font=('Arial', 18, 'bold'))

        # Get current time
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec

        # Calculate hand angles
        second_angle = math.pi/30 * second - math.pi/2
        minute_angle = math.pi/30 * minute + second_angle/60 - math.pi/2
        hour_angle = math.pi/6 * hour + math.pi/360 * minute - math.pi/2

        # Draw hour hand (blue)
        hour_length = self.radius * 0.5
        hour_x = self.center + hour_length * math.cos(hour_angle)
        hour_y = self.center + hour_length * math.sin(hour_angle)
        self.canvas.create_line(self.center, self.center, hour_x, hour_y, fill='blue', width=8)

        # Draw minute hand (blue)
        minute_length = self.radius * 0.7
        minute_x = self.center + minute_length * math.cos(minute_angle)
        minute_y = self.center + minute_length * math.sin(minute_angle)
        self.canvas.create_line(self.center, self.center, minute_x, minute_y, fill='blue', width=6)

        # Draw second hand (blue)
        second_length = self.radius * 0.9
        second_x = self.center + second_length * math.cos(second_angle)
        second_y = self.center + second_length * math.sin(second_angle)
        self.canvas.create_line(self.center, self.center, second_x, second_y, fill='blue', width=2)

        # Draw center pin (blue circle)
        self.canvas.create_oval(
            self.center - 10, self.center - 10,
            self.center + 10, self.center + 10,
            fill='blue', outline='blue'
        )

        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
