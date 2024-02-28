import socket
import threading
import pickle

def handle_client(client_socket, client_address):
    try:
        while True:
            pickled_message = client_socket.recv(4096)
            if not pickled_message:
                break
              
            message = pickle.loads(pickled_message)

            for c in clients:
                if c != client_socket:
                    c.sendall(pickled_message)
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")
        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    clients = []
    main()
