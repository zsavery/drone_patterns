from easytello import tello

if __name__ == "__main__":
    distance = 15
    my_drone = tello.Tello()

    my_drone.takeoff()
    '''
    # movement on x-axis
    my_drone.forward(distance)
    my_drone.back(distance)

    # movement on y-axis
    my_drone.left(distance)
    my_drone.right(distance)

    # movement on z-axis
    my_drone.up(distance)
    my_drone.down(distance)
    '''

    # flips
    my_drone.flip('f')

    my_drone.land()