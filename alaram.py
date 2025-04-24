import winsound
import time

def play_alarm():
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 1000   # Set duration to 1000 milliseconds (1 second)
    
    # Play sound for 1 second
    winsound.Beep(frequency, duration)

# Example of playing an alarm after a countdown
Time = int(input("Enter countdown time in second."))
time.sleep(Time)
play_alarm()
