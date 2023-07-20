from flask import Flask, render_template, request
import os
import platform
import datetime
import time
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def simulate_process(process_id, results):
    start_time = time.time()

    # Simulate the execution of a process
    # Replace this with your actual code for running a process in the Flask app

    end_time = time.time()

    # Calculate the times for this process
    execution_time = end_time - start_time
    arrival_time = start_time
    burst_time = execution_time
    waiting_time = 0
    turnaround_time = burst_time + waiting_time

    # Add the times to the results list
    results[process_id] = (arrival_time, burst_time, execution_time, waiting_time, turnaround_time)

@app.route('/process', methods=['POST'])
def process():
    # Get the number of processes to run from the form
    num_processes = int(request.form['num_processes'])

    # Create a dictionary to hold the results of each process
    results = {}

    # Create a list to hold the threads
    threads = []

    # Run each process in a separate thread
    for i in range(num_processes):
        thread = threading.Thread(target=simulate_process, args=(i+1, results))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Sort the results based on process ID
    sorted_results = sorted(results.items())

    # Extract only the values from the sorted results
    final_results = [result for process_id, result in sorted_results]

    # Render the results template with the list of times and make 'enumerate' available in the template context
    return render_template('results.html', results=final_results, enumerate=enumerate)

@app.context_processor
def inject_current_year():
    year = datetime.datetime.now().year
    return dict(current_year=year)

if __name__ == '__main__':
    app.run(debug=True)

