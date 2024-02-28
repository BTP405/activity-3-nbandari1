import socket
import pickle
import threading

def receive_messages():
    try:
        while True:
            pickled_message = client_socket.recv(4096)
            if not pickled_message:
                break
              
            message = pickle.loads(pickled_message)
            print(message)
          
    except Exception as e:
        print(f"Error receiving messages: {e}")

def send_message():
    try:
        while True:
            message = input("Enter your message: ")
            pickled_message = pickle.dumps(message)
            client_socket.sendall(pickled_message)
          
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()
    send_message()

if __name__ == "__main__":
    main()
