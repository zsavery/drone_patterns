from easytello import tello
from my_drone_func import *


if __name__ == '__main__':
    # create drone object
    drone = tello.Tello()


    # get temp
    temp = drone.get_temp()
    print(f"Temperature: {temp}")

    # launch
    drone.takeoff()

    # fly up
    drone.up(50)

    # get temp
    temp = drone.get_temp()
    print(f"Temperature: {temp}")



    #

    # land
    drone.land()