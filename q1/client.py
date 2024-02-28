#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.
import socket
import pickle
import os

def load_file(filepath):
  """ Load the content of a file and return its binary data. """
  with open(filepath, 'rb') as f:
    return f.read()

def main():
  """ Main function which connects to server and sends a pickled file """
  server_host = '127.0.0.1'
  server_port = 12345
  buffer_seize = 4096
  #create socket object for client
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    client_socket.connect((server_host, server_port))
  except Exception as error:
    print("ERROR connecting to server: ", error)
    return
  try:
    #get file path from user
    file_path = input("Enter path: ")
    #check if file exists
    if not os.path.exists(file_path):
      print("File not found")
      return
    #load file data
    file_data = load_file(file_path)
    #pickle file data to serialize it
    serialized_data = pickle.dumps(file_data)
    #send the pickled data to server
    client_socket.sendall(serialized_data)
    print("File sent successfully!")
  except Exception as error:
    print("ERROR: ", error)
  finally:
    client_socket.close()

if __name__ == "__main__":
  main()
  
