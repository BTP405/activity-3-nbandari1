import socket
import pickle
from task_functions import task_multiply

def execute_task(task_data):
    """ Execute the task received from the client """
  try:
        task, args = pickle.loads(task_data)
        result = task(*args)
        return result
    except Exception as e:
        print("Error executing task:", e)
        return None

def main():
    HOST = '127.0.0.1'
    PORT = 12346
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Worker node is listening for incoming connections...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connection established from {addr}")
            with conn:
                task_data = conn.recv(4096)
                if not task_data:
                    print("No task data received")
                    continue
                  
                result = execute_task(task_data)
              
                if result is not None:
                    result_data = pickle.dumps(result)
                    conn.sendall(result_data)

if __name__ == "__main__":
    main()
