
# x - axis
my_drone.forward(distance)
my_drone.back(distance)

# y - axis
my_drone.left(distance)
my_drone.right(distance)

# z - axis
my_drone.up(distance)
my_drone.down(distance)

# flip
my_drone.flip('l')
my_drone.flip('r')

# camera
my_drone.streamon()
camera_state = my_drone.stream_state
print(camera_state)
my_drone.streamoff()
camera_state = my_drone.stream_state
print(camera_state)

# battery