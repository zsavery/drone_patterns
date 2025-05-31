def power_of(num, power, power_dict:dict = {}):
    if power in power_dict:
        return power_dict[power]
    if power == 0:
        return 1
    return num * power_of(num, power - 1)

def power_of_2(num, power):

    if power == 0:
        return 1
    return num * power_of(num, power - 1)

if __name__ == '__main__':
    base = 2
    power = 0
    my_powers = {}
    for _ in range(500_000_000):
        my_powers[power] = power_of(base, power)
        print(f"{base}^{power} = {my_powers[power]}")
        power += 1

