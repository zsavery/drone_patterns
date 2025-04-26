from easytello import tello
from time import sleep
from my_drone_func import *

if __name__ == '__main__':

    drone = tello.Tello()

    get_tempReport(drone, 4)
    get_tempReport(drone, 4)
    get_tempReport(drone, 4)


