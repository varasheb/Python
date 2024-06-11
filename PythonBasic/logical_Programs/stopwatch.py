# 6. Simulate Stopwatch Program
# a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
# the start and end clicks
# b. I/P -> Start the Stopwatch and End the Stopwatch
# c. Logic -> Measure the elapsed time between start and end
# d. O/P -> Print the elapsed time.

import time

def start_stopwatch():
    start_time = time.time()
    return start_time

def stop_stopwatch(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def main():
    input("Press Enter to start the stopwatch")
    start_time = start_stopwatch()
    input("Press Enter to stop the stopwatch")
    elapsed_time = stop_stopwatch(start_time)
    print("Elapsed time:", elapsed_time, "seconds")

main()

