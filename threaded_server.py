"""import socket
import threading
import subprocess

class ClientHandler(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        print(f"Connected by {self.addr}")
        try:
            # Receive command from the server
            command = self.conn.recv(1024).decode()
            if command:
                print(f"Received command from server: {command}")

                # Execute the command on the client shell
                try:
                    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    result = e.output

                # Send the result back to the server
                self.conn.sendall(result)
        except ConnectionResetError:
            print(f"Client {self.addr} disconnected unexpectedly")
        finally:
            self.conn.close()

def main():
    # Server configuration
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    COMMAND = input("Enter the command to send to clients: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server listening on", (HOST, PORT))

        # Accept connections from clients
        while True:
            conn, addr = server_socket.accept()
            client_handler = ClientHandler(conn, addr)
            client_handler.start()

            # Send command to each connected client
            conn.sendall(COMMAND.encode())

if __name__ == "__main__":
    main()
"""




"""import socket
import threading

class ClientHandler(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        print(f"Connected by {self.addr}")
        try:
            while True:
                command = input(f"Enter command for {self.addr}: ")
                if command.lower() == 'exit':
                    print(f"Disconnecting {self.addr}")
                    break

                # Send command to client
                self.conn.sendall(command.encode())

                # Receive response from client
                data = self.conn.recv(1024).decode()
                print(f"Response from {self.addr}: {data}")
        except ConnectionResetError:
            print(f"Client {self.addr} disconnected unexpectedly")
        finally:
            self.conn.close()

def main():
    # Server configuration
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server listening on", (HOST, PORT))

        while True:
            conn, addr = server_socket.accept()
            client_handler = ClientHandler(conn, addr)
            client_handler.start()

if __name__ == "__main__":
    main()"""



#over the network
"""import socket
import threading

class ClientHandler(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        print(f"Connected by {self.addr}")
        try:
            while True:
                command = input(f"Enter command for {self.addr}: ")
                if command.lower() == 'exit':
                    print(f"Disconnecting {self.addr}")
                    break

                # Send command to client
                self.conn.sendall(command.encode())

                # Receive response from client
                data = self.conn.recv(1024).decode()
                print(f"Response from {self.addr}: {data}")
        except ConnectionResetError:
            print(f"Client {self.addr} disconnected unexpectedly")
        finally:
            self.conn.close()

def main():
    # Server configuration
    HOST = ''  # Listen on all available interfaces
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print("Server listening on", (HOST, PORT))

        while True:
            conn, addr = server_socket.accept()
            client_handler = ClientHandler(conn, addr)
            client_handler.start()

if __name__ == "__main__":
    main()
"""



import socket
import threading
import logging

logging.basicConfig(level=logging.INFO)

class ClientHandler(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        logging.info(f"Connected by {self.addr}")
        try:
            while True:
                command = input(f"Enter command for {self.addr}: ")
                if command.lower() == 'exit':
                    logging.info(f"Disconnecting {self.addr}")
                    break

                # Send command to client
                self.conn.sendall(command.encode())

                # Receive response from client
                data = self.conn.recv(1024).decode()
                logging.info(f"Response from {self.addr}: {data}")
        except ConnectionResetError:
            logging.info(f"Client {self.addr} disconnected unexpectedly")
        finally:
            self.conn.close()

def main():
    # Server configuration
    HOST = ''  # Listen on all available interfaces
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        logging.info("Server listening on %s", (HOST, PORT))

        while True:
            conn, addr = server_socket.accept()
            logging.info("Accepted connection from %s", addr)
            client_handler = ClientHandler(conn, addr)
            client_handler.start()

if __name__ == "__main__":
    main()
