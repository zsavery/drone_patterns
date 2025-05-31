from easytello import tello

if __name__ == '__main__':
    drone = tello.Tello()
    drone.takeoff()
    SPD = 10

    drone.go(0, 0, 15, SPD)
    drone.go(20, -5, 15, SPD)
    drone.go(40, -15, 25, SPD)
    drone.go(0, 0, 15, SPD)
    drone.go(20, -5, 15, SPD)
    drone.go(10, 0, 5, SPD)
    drone.go(0, 0, 0, SPD)

    drone.land()