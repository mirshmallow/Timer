# Timer

import time

is_running = True
seconds = 0


while is_running:
    time_unit = input("Hours, minutes or seconds (Press Q to quit and S to start): ").lower()
    if time_unit == "seconds":
        add_seconds = input("How many seconds?: ")
        while add_seconds.isalpha():
            print("You must put a number")
            add_seconds = input("How many seconds?: ")
        seconds += int(add_seconds)
        add_time = input("Add time? (Y/N):").lower()
        if add_time == "y":
            pass
        elif add_time == "n":
            for x in range(seconds, 0, -1):
                second = x % 60
                minute = int(x / 60) % 60
                hour = int(x / 3600)
                print(f"{hour:02}:{minute:02}:{second:02}")
                time.sleep(1)
            print("Time's up!")
            seconds = 0
            time.sleep(3)
    elif time_unit == "minutes":
        add_minutes = input("How many minutes?: ")
        while add_minutes.isalpha():
            print("You must put a number")
            add_minutes = input("How many minutes?: ")
        seconds += int(add_minutes) * 60
        add_time = input("Add time? (Y/N):").lower()
        if add_time == "y":
            pass
        elif add_time == "n":
            for x in range(seconds, 0, -1):
                second = x % 60
                minute = int(x / 60) % 60
                hour = int(x / 3600)
                print(f"{hour:02}:{minute:02}:{second:02}")
                time.sleep(1)
            print("Time's up!")
            seconds = 0
            time.sleep(3)
    elif time_unit == "hours":
        add_hours = input("How many hours?: ")
        while add_hours.isalpha():
            print("You must put a number")
            add_hours = input("How many hours?: ")
        seconds += int(add_hours) * 3600
        add_time = input("Add time? (Y/N):").lower()
        if add_time == "y":
            pass
        elif add_time == "n":
            for x in range(seconds, 0, -1):
                second = x % 60
                minute = int(x / 60) % 60
                hour = int(x / 3600)
                print(f"{hour:02}:{minute:02}:{second:02}")
                time.sleep(1)
            print("Time's up!")
            seconds = 0
            time.sleep(3)
    elif time_unit == "q":
        while True:
            confirm = input("Wanna quit? (Y/N):").lower()
            if confirm == "y":
                is_running = False
                break
            elif confirm == "n":
                is_running = True
                break
            else:
                print("You must press Y or N")