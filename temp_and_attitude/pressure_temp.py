from easytello import tello
from time import sleep


def get_tempReport(d: tello.Tello, t) -> None:
    try:
        temp = d.get_temp()
        print("air temp: {}".format(temp))
        sleep(t)
    except (AttributeError, TypeError) as  e:
        print("None temperature is found, check if drone is running properly." +
              "\nError: {}".format(e))

def get_pressureReport(d: tello.Tello, t) -> None:
    try:
        pressure = d.get_baro()
        print("air pressure: {}".format(pressure))
        sleep(t)
    except (AttributeError, TypeError) as e:
        print("None atmospheric pressure is found, check if drone is running properly." +
              "\nError: {}".format(e))

if __name__ == '__main__':

    # create drone object
    drone = tello.Tello()
    # how long the drone waits after a command in addition to waiting for a command to timeout or complete
    SLEEP_LENGTH = 2
    DISTANCE = 10

    # collect data on the ground
    get_tempReport(drone, SLEEP_LENGTH)
    get_pressureReport(drone, SLEEP_LENGTH)

    # start drone
    drone.takeoff()

    # collect data at 10
    drone.up(DISTANCE)
    get_tempReport(drone, SLEEP_LENGTH)
    get_pressureReport(drone, SLEEP_LENGTH)

    # collect data at 20
    drone.up(DISTANCE)
    get_tempReport(drone, SLEEP_LENGTH)
    get_pressureReport(drone, SLEEP_LENGTH)



