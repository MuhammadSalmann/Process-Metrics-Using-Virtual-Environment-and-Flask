from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    num_processes = 5

    for i in range(num_processes):
        start_time = time.time()  # Start time of the Flask app
        arrival_time = start_time  # Arrival time is the same as the start time

        # Process execution
        # Simulating some delay to represent the execution time
        time.sleep(2)  # Execution time of the process

        end_time = time.time()  # End time of the Flask app

        burst_time = end_time - start_time
        waiting_time = arrival_time - start_time
        turnaround_time = end_time - arrival_time

        print(f"Process {i+1}:")
        print(f"Burst Time: {burst_time} seconds")
        print(f"Arrival Time: {arrival_time} seconds")
        print(f"Execution Time: 2 seconds")  # Assuming a fixed execution time of 2 seconds
        print(f"Waiting Time: {waiting_time} seconds")
        print(f"Turnaround Time: {turnaround_time} seconds")
        print("\n")

