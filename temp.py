
park_time = input("how many hours")
park_time = int(park_time)
print("user has entered hours", park_time)


if park_time > 4:
    cost = 4*3 + 2*1
    print("cost", cost)

elif park_time <= 4:
    cost = 5*3 + 3*1
    print("cost", cost)

else:
    print("good, as gold")


