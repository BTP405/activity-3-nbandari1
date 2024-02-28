import socket
import pickle
from task_functions import perform_multiplication_task

def distribute_task(task, arg, worker_address):
    """ Distribute a task to multiple worker nodes and collect results """
    results = []
    for address in worker_address:
        try:
            #create socket connection to the worker node
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                #set timeout for connection
                client_socket.settimeout(5)  
                #connect to worker node
                client_socket.connect(address)
                #prepare task data (function and arguments) for transmission
                task_data = pickle.dumps((task, arguments))
                #send all the task data to worker node
                client_socket.sendall(task_data)
                response = client_socket.recv(4096)
                if response:
                    #unpickle the result and append it to results list
                    result = pickle.loads(response)
                    results.append(result)
                else:
                    print(f"No response received from {address}")
        except socket.timeout:
            print(f"Connection to {address} timed out.")
        except ConnectionRefusedError:
            print(f"Connection to {address} refused.")
    return results

def main():
    worker_address = [('127.0.0.1', 12346), ('127.0.0.1', 12347)] 
    task_arguments = (5, 10)
    results = distribute_task(perform_multiplication_task, task_arg, worker_addresses)
    print("Results:", results)

if __name__ == "__main__":
    main()
