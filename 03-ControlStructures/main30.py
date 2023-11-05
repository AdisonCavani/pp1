time = input("Enter time (24-hour format): ")

hour = int(time.split(":")[0])
minutes = int(time.split(":")[1])

time_of_day = "am"

if hour >= 12:
    time_of_day = "pm"
if hour > 12:
    hour = hour - 12

print(f"Time in 12-hour format: {hour}:{minutes}{time_of_day}")