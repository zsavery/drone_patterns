from typing import Any
from easytello import tello
from time import sleep

def get_battery(drone: tello.Tello) -> Any:
    return drone.get_battery()

def print_battery(drone: tello.Tello) -> None:
    print(drone.get_battery())

def get_height_attitude(drone: tello.Tello) -> None:
    height = drone.get_height()
    print(f"Current Height: {height}")
    drone.wait(1)

    attitude = drone.get_attitude()
    print(f"Current Attitude: {attitude}")
    drone.wait(1)
    print_battery(drone)

def get_temp(drone: tello.Tello) -> None:
    temp = drone.get_temp()
    print(f"Temperature: {temp}")
    # print("Temperature: %s".format(temp))
    drone.wait(1)
    print_battery(drone)

def get_pressure(drone: tello.Tello) -> None:
    pressure = drone.get_baro()
    print(f"Pressure: {pressure}")
    drone.wait(1)
    print_battery(drone)

def right_turn(drone: tello.Tello, degree: int) -> None:
    drone.cw(degree)
    drone.wait(.5)

def get_pressureReport(d: tello.Tello, t) -> None:
    pressure = d.get_baro()
    print("air pressure: {}".format(pressure))
    sleep(t)

def get_tempReport(d: tello.Tello, t) -> None:
    temp = d.get_temp()
    print("air temp: {}".format(temp))
    sleep(t)