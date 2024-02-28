import os
import socket

def recv_file(data, dir, filename):
  """ Saves the received file data to a specified directory with the provided filename """
  os.makedirs(dir, exist_ok = True)
  f_path = os.path.join(dir, filename)
  with open(f_path, 'wb') as f:
    f.write(data)

def main():
""" Main function which starts the server and handles incoming connections """
host = '127.0.0.1'
port = 12345
buffer_size = 4096
dir = "received_files"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server.socket.listen(1)
print("Server is listening at", (host, port))

while True:
  client_socket, client_address = server_socket.accept()
  print("Connected to ", client_address)

  try:
    data = client_socket.recv(buffer_size)
    if not data:
      print("No data received.")
      continue
    filename = input("Enter the filename: ")
    save_file(data, dir, filename)
    print("File saved successfully as", filename)
  except Exception as err:
    print("Error: ", err)
  finally:
    client_socket.close()

if __name__ == "__main__":
  main()
