from easytello import tello
from time import sleep


def move_and_log_data(d: tello.Tello, coord: dict) -> dict:
    d.go(coord["x"], coord["y"], coord["z"], speed=10)

    try:
        coord["temperature"].append(d.get_temp())
        coord["pressure"].append(d.get_temp())
        sleep(1)
    except Exception as e:
        print(e, "\nSomething went wrong!")
    return coord

if __name__ == '__main__':
    drone = tello.Tello()

    coordinates = {"x": [0, 0, 5 , 10 , 15, 25],
            "y": [0, 10, 20, 30, 35, 20],
            "z": [10, 25, 40, 60, 30, 10],
            "temperature": [],
            "pressure": [],
                   "size": 6}


    drone.takeoff()

    for index in range(coordinates["size"]):
        coordinate = move_and_log_data(drone, coordinates)

    drone.land()

