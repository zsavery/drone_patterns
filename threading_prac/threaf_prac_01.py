import threading
from time import sleep

def travel(name, distance):
    sleep(distance/100)
    print(f"Traveling to {name} for a distance of {distance} miles.")

if __name__ == '__main__':
    # list -> my_list = [0, 1, 2, 3, 4, 5]
    # my_list[0] -> 0

    # dictionary - dict ->
    """
    my_dict = {'name': 'Carter',
                'age': 21 }
    my_dict['name'] -> Carter
    """
    cities = [
        {"name": "Frisco", "distance": 575},
        {"name": "El Paso", "distance": 1150},
        {"name": "Houston", "distance": 25}
    ]

    """
    for city in cities:
        print(f"Traveling to {city['name']} by {city['distance']}")
    """

    journey_1 = threading.Thread(target=travel, args=(cities[0]['name'], cities[0]['distance']))
    journey_1.start() # start thread 1

    journey_2 = threading.Thread(target=travel, args=(cities[1]['name'], cities[1]['distance']))
    journey_2.start()

    journey_3 = threading.Thread(target=travel, args=(cities[2]['name'], cities[2]['distance']))
    journey_3.start()

    journey_1.join()
    journey_2.join()
    journey_3.join()

    print("Completed traveling!")




