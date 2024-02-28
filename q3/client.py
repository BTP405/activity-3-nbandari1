import socket
import pickle
import threading

def recv_messages():
    """ Function handles receving messages from server """
    try:
        while True:
            #receives pickled message from server
            pickled_message = client_socket.recv(4096)
            #check if message is not empty
            if not pickled_message:
                break
            #unpickle message 
            message = pickle.loads(pickled_message)
            print(message)
          
    except Exception as e:
        print(f"Error receiving messages: {e}")

def send_message():
    """ Function handles sending messages to server """
    try:
        while True:
            message = input("Enter your message: ")
            #pickling the input message
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
