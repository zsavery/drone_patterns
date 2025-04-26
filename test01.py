from typing import Any
from easytello import tello
from my_drone_func import *

my_drone = tello.Tello()

my_drone.takeoff()


get_height_attitude(my_drone)
get_temp(my_drone)

# my_drone.go(0, 0, 15, 5)
# my_drone.wait(1)
# my_drone.forward(40)

# Travel
my_drone.go(0, 0, 15, 5)
my_drone.go(20, -5, 15, 5)
my_drone.go(40, 5, 15, 5)

#
# for i in range(4):
#     my_drone.forward(40)
#     my_drone.wait(1)
#
# my_drone.ccw(90)
# for i in range(2):
#     my_drone.back(60)
#
# my_drone.back(20)
# my_drone.wait(4)
# my_drone.land()
# my_drone.takeoff()
#
# my_drone.cw(720)
# my_drone.wait(1)
# my_drone.right(60)




# Square
distance = 15  # cm
for i in range(4): # 0 ,1, 2, 3
    my_drone.forward(distance)
    right_turn(my_drone, 90)
    print()


my_drone.land()
