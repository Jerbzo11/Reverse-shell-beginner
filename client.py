import socket

host = '192.168.1.7'  # localhost
port = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

while True:
    # Get user input
    message = input("Enter message or command (type 'exit' to quit): ")

    # Send data to the server
    client_socket.sendall(message.encode())

    # If user types 'exit', close the connection
    if message.lower() == "exit":
        break

    # Receive a response from the server
    data = client_socket.recv(1024)
    print("Received from server:", data.decode())

# Close the connection
client_socket.close()
