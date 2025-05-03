from easytello import tello
from time import sleep


def move_and_log_data(d: tello.Tello, coord: dict) -> dict:
    """
    Move drone to coordinate and log temperature/pressure data
    
    Args:
        d: Tello drone object
        coord: Dictionary containing coordinates and sensor data lists
        
    Returns:
        Updated coordinates dictionary with appended sensor readings
    """
    # Move drone to specified x,y,z coordinates 
    d.go(coord["x"], coord["y"], coord["z"], speed=10)

    # Get temperature reading and append to list
    try:
        coord["temperature"].append(d.get_temp())
    except Exception as e:
        print(e, "\nSomething went wrong!")
    finally:
        sleep(1)

    # Get pressure reading and append to list 
    try:
        coord["pressure"].append(d.get_temp())
        sleep(1)
    except Exception as e:
        print(e, "\nSomething went wrong!")
    finally:
        sleep(1)

    return coord

if __name__ == '__main__':
        # Create drone object
        drone = tello.Tello()

        # Define flight coordinates and data storage
        coordinates = {"x": [0, 0, 5, 10, 15, 25],
                       "y": [0, 10, 20, 30, 35, 20],
                       "z": [10, 25, 40, 60, 30, 10],
                       "temperature": [],  # List to store temperature readings
                       "pressure": [],  # List to store pressure readings
                       "size": 6}  # Number of waypoints

        drone.takeoff()

        # Move through each waypoint and collect sensor data
        for index in range(coordinates["size"]):
            coordinate = move_and_log_data(drone, coordinates)
    
        # Land the drone
        drone.land()
