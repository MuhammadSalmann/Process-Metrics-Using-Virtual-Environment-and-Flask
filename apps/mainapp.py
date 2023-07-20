from flask import Flask, render_template, request
import time
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def simulate_process(process_id, results):
    wait = random.randint(1, 9)
    wait2 = random.randint(1, 5)
    arrival_time = time.time()
    print('===================================')
    print('\nProcess:', process_id)
    print('Arrived at:', arrival_time)
    print('*waiting***')
    time.sleep(wait)
  
    start_time = time.time()
    print('Started Execution at:', start_time)
    
    sum_x = 0
    for i in range(1000000):
        sum_x += i
    time.sleep(wait2)
    print('\nSum of first 1 million numbers is:', sum_x)

    end_time = time.time()
    print('\nEnded Execution at:', end_time)

    execution_time = end_time - start_time
    burst_time = execution_time
    turnaround_time = end_time - arrival_time
    waiting_time = start_time - arrival_time

    results[process_id] = (arrival_time, burst_time, execution_time, waiting_time, turnaround_time)

@app.route('/process', methods=['POST'])
def process():
    num_processes = int(request.form['num_processes'])
    results = {}
    
    # executing processes sequentially
    for i in range(1, num_processes + 1):
        simulate_process(i, results)
        
  #results = {
  #1: (10, 5, 3, 2, 8),
  #2: (15, 7, 4, 3, 11),
  #3: (20, 10, 6, 4, 14)
#}
    # Extract only the values from the sorted results
    final_results = [result for process_id, result in results.items()]
    
 #final_results = [
  #(10, 5, 3, 2, 8),
  #(15, 7, 4, 3, 11),
  #(20, 10, 6, 4, 14)
#]

    return render_template('results.html', results=final_results)

if __name__ == '__main__':
    app.run(debug=True)

