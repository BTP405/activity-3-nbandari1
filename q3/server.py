import socket
import threading
import pickle

def handle_client(client_socket, client_address):
    """ Function handles client connections """
    try:
        while True:
            #receives pickled messages from client
            pickled_message = client_socket.recv(4096)
            #check if message is empty or not
            if not pickled_message:
                break
            #unpickling message  
            message = pickle.loads(pickled_message)
            #send message to all clients except the sender client
            for c in clients:
                if c != client_socket:
                    c.sendall(pickled_message)
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

def main():
    #create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind socket
    server_socket.bind(('localhost', 12345))
    #listen for incoming connections
    server_socket.listen(5)
    print("Server is listening for incoming connections...")

    while True:
        #accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")
        #add the client socket to the list of connected clients
        clients.append(client_socket)
        #creating a thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    clients = []
    main()
