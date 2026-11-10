cardio_minutes = 45
calories_burned = cardio_minutes * 8

print(f"Total cardio duration: {cardio_minutes} minutes | Total calories burned: {calories_burned} calories")

if cardio_minutes >= 50:
    print("Elite effort")

elif cardio_minutes >= 30:
    print("Solid effort")

elif cardio_minutes >= 15:
    print("Light effort")

else:
    print("Under target")
    

