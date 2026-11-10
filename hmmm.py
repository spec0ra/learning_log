exercise = "Push-ups"
reps = 15
sets = 4
rest_seconds = 60
divider = "-"

print(divider * 25)

total_reps = reps * sets

print(f"Exercise: {exercise} | Total reps: {total_reps}")

print(f"Total rest time: {rest_seconds * (sets - 1)}")

if total_reps >= 50:
    print("Solid session") 
else:
    print("Push harder next time")

print(len(exercise))

