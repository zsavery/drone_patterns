# Drone Patterns - Code Examples

## import module
```python
from easytello import tello
```

## Connecting to the Drone
```python
my_drone = tello.Tello()
```

## Start and End Flight
### Start
```python
my_drone.takeoff()
```
### End
```python
my_drone.land()
```

### Emergency Stop
```python
my_drone.emergeny()
```
## Directional Movement 

### x - axis

```python
my_drone.forward(distance)
my_drone.back(distance)
```

### y - axis

```python
my_drone.left(distance)
my_drone.right(distance)
```

### z - axis

```python
my_drone.up(distance)
my_drone.down(distance)
```

### flip

```python
my_drone.flip('l')
my_drone.flip('r')
```


## camera

```python
my_drone.streamon()
camera_state = my_drone.stream_state
print(camera_state)
my_drone.streamoff()
camera_state = my_drone.stream_state
print(camera_state)
```


## Status 

### battery
```python
result = my_drone.get_battery()
print("Battery Level: {}".format)
```

### temperature
```python
result = my_drone.get_battery()
print("Battery Level: {}".format)
```

### atmospheric pressure
```python
result = my_drone.get_battery()
print("Battery Level: {}".format)
```

### height
```python
result = my_drone.get_height()
print("Battery Level: {}".format)
```

### attitude
In reference to a drone, attitude refers to the orientation of the drone relative to the Earth’s surface. It describes how the drone is tilted or rotated in three-dimensional space, typically using three angles:
1.	Pitch – Tilt forward or backward (nose up/down).
2.	Roll – Tilt left or right (wing up/down).
3.	Yaw – Rotation around the vertical axis (turning left or right like a compass direction).

```python
result = my_drone.get_attitude()
```