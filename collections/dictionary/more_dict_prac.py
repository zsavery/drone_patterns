from temp_and_attitude.my_drone_func import *

import matplotlib.pyplot as plt


if __name__ == '__main__':
    drone = tello.Tello()

    cord = {"x": [0, 0, 5 , 10 , 15, 25],
            "y": [0, 10, 20, 30, 35, 20],
            "z": [10, 25, 40, 60, 30, 10],
            "temp": [],
            "press": []}

    '''
    for k, v in cord.items():
        pass

    for i in cord:
        pass

    for k in cord.keys():
        pass
    '''

    drone.takeoff()

    for i in range(6):
        drone.go(cord["x"][i], cord["y"][i],
                 cord["z"][i], 10)
        sleep(1)
        cord["temp"].append(drone.get_temp())
        cord["press"].append(drone.get_baro())

    drone.land()


    for i in range(6):
        print(f"Temp: {cord['temp'][i]} \nPressure: {cord['press'][i]}")

    # create a bar graph from drone data
    # https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
    names = ["Temp", "Pressure"]
    plt.bar(names, cord["temp"], cord["press"], color='g')