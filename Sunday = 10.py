times = [10, 15, 20, 25, 30, 35, 40]

total_time = sum(times)

print(total_time)

average_time = (total_time// len(times))

print(average_time)

if average_time >= 40:
    print("You passed")
else:
    print("You failed")

print(times[2])

print(times[0:4])

print(times[:5])