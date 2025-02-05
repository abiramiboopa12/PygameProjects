import math
import datetime
import pygame
from tkinter import *
class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("400x200")
        self.time_label = Label(root, text="", font=("Helvetica", 48))
        self.time_label.pack()
        self.update_clock()
    def update_clock(self):
        now = datetime.datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.time_label.after(1000, self.update_clock)
def run_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Analog Clock")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        center = (400, 300)
        pygame.draw.circle(screen, (255, 255, 255), center, 200, 5)
        for i in range(12):
            angle = i * math.pi / 6
            x = center[0] + 180 * math.cos(angle - math.pi / 2)
            y = center[1] + 180 * math.sin(angle - math.pi / 2)
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 10)
        now = datetime.datetime.now()
        hours = now.hour % 12
        minutes = now.minute
        seconds = now.second
        hour_angle = (hours + minutes / 60) * math.pi / 6
        minute_angle = (minutes + seconds / 60) * math.pi / 30
        second_angle = seconds * math.pi / 30
        hour_x = center[0] + 100 * math.cos(hour_angle - math.pi / 2)
        hour_y = center[1] + 100 * math.sin(hour_angle - math.pi / 2)
        minute_x = center[0] + 150 * math.cos(minute_angle - math.pi / 2)
        minute_y = center[1] + 150 * math.sin(minute_angle - math.pi / 2)
        second_x = center[0] + 170 * math.cos(second_angle - math.pi / 2)
        second_y = center[1] + 170 * math.sin(second_angle - math.pi / 2)
        pygame.draw.line(screen, (255, 0, 0), center, (hour_x, hour_y), 10)
        pygame.draw.line(screen, (0, 255, 0), center, (minute_x, minute_y), 5)
        pygame.draw.line(screen, (0, 0, 255), center, (second_x, second_y), 2)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
root = Tk()
clock = DigitalClock(root)
root.after(0, run_pygame)
root.mainloop()