from flask import Flask, render_template, request
import datetime
import time
import threading
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def simulate_process(process_id, results):
    wait = random.randint(1, 9)
    wait2 = random.randint(1, 5)
    arrival_time = time.time()      
    #process has arrived
    #waiting area start from here till start time
    print('===================================')
    print('\nProcess:', process_id)
    print('Arrived at:',arrival_time)
    print('\n***Process:', process_id,' is Waiting****')
    time.sleep(wait)  
    
    # Process Starts here               
    start_time = time.time()
    print('Started Execution of Process ', process_id, ' at :', start_time)
    
    sum_x = 0
    for i in range(1000000):
        sum_x += i
    time.sleep(wait2) # waiting to see diff in execution time
    print('\nSum of first 1 million numbers is:', sum_x)

    end_time = time.time()
    print('\nEnded Execution of Process ', process_id,' at:',end_time)

    # Calculate the times for this process
    execution_time = end_time - start_time
    burst_time = execution_time
    turnaround_time = end_time - arrival_time
    waiting_time = start_time - arrival_time

    # Add the times to the results dictionary
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
        thread = threading.Thread(target=simulate_process, args=(i+1, results))   #creating the thread
        thread.start()
        threads.append(thread)		#storing the object in the thread list

    # Wait for all threads to complete
    for thread in threads:
        thread.join()		#makes the threads wait to complete execution and then goes to next line

    # Sort the results based on process ID
    sorted_results = sorted(results.items())

    # Extract only the values from the sorted results
    final_results = [result for process_id, result in sorted_results]

    # Render the results template with the list of times
    return render_template('results.html', results=final_results)

if __name__ == '__main__':
    app.run(debug=True)
