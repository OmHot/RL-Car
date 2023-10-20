import pygame as pg
from autopilot.car import Car  # Import your Car class
from autopilot.highway import Highway  # Import your Highway class
from NPC import NPC
# Initialize pygame
pg.init()

# Set up display
screen_width, screen_height = 1320, 768
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Car on Highway")

# Create a highway
#self.highway = Highway((self.width // 2, self.height // 2), map_spread, map_complexity, width=30)
highway = Highway(position=(screen_width // 2, screen_height//2), spread=(150, 350), complexity=3, width=30)

# Create a car
#car = Car(spawn_position=highway.start_position, spawn_angle=highway.start_angle, scale=0.5,show_radars=True)
npc = NPC(spawn_position=highway.start_position, spawn_angle=highway.start_angle, scale=0.5,show_radars=True)

# Set up clock for controlling frame rate
clock = pg.time.Clock()
curve = list(highway.scale(1.07))
lenght = curve.__len__()
piterator = 0
speed = 0
# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Get user input (e.g., arrow keys or user-defined controls)
    # For example, you can use the arrow keys to control the car's movement.
    """keys = pg.key.get_pressed()
    movement = {
        "direction": 1 if keys[pg.K_UP] else (-1 if keys[pg.K_DOWN] else 0),
        "rotation": 1 if keys[pg.K_RIGHT] else (-1 if keys[pg.K_LEFT] else 0),
    }
    """
    # Update car and highway
    dt = 0.5#clock.tick(1000)/100
    #print(dt)  # Limit frame rate to 60 FPS
    #car.move(movement, dt, screen, highway) 
    if speed>=3:
        if piterator != -1:
            npc.translate(curve[piterator])
            print(curve[piterator])
            piterator-=1
        else:
            piterator =lenght-1
            npc.translate(curve[piterator])
        speed =0
    speed+=dt

    highway.draw(screen)

    # Draw the car on the screen
    #car.draw(screen)
    npc.draw(screen)
    # Update the display
    pg.display.flip()

pg.quit()
