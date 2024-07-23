import time

def alarm(seconds):

    time_elapsed = 0

    while time_elapsed < seconds:
        time_elapsed += 1
        time.sleep(1)

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600
        minutes_left = (time_left % 3600) // 60
        seconds_left = time_left % 60

        print(f"\r{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}", end='')

hours = int(input("How many hours to wait: "))
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = hours * 3600 + minutes * 60 + seconds

alarm(total_seconds)
