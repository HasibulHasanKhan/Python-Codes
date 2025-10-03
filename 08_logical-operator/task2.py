temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside.")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")