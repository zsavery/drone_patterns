import matplotlib.pyplot as plt
import numpy as np


# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots
if __name__ == '__main__':
    names = ["Location 1", "Location 2", "Location 3"]
    cord = {
        "temp": [30, 45, 60],
        "press": [10, 25, 40]
    }

    width = 0.25
    multiplier = 0
    fig, ax = plt.subplots(1,1)

    x = np.arange(len(names))

    for attribute, measurement in cord.items():
        offset = width * multiplier
        sect = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(sect, padding=3)
        multiplier+=1


    ax.set_title("Temperature and Pressure")
    ax.set_xticks(x + width, names)
    fig.legend(loc='upper right', ncol=2)
    fig.show()