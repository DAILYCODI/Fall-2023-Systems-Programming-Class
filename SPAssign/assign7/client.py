import socket

# Server's IP address
HOST = '127.0.0.1'  
# Port to connect to
PORT = 65432      

# Creating a socket using IPv4 and TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

     # Loop to send and receive messages from the server
    while True:
        # User input to get a message to send to the server
        message = input("Msg to send: ")

        # Sending the message to the server after encoding it to bytes
        client_socket.sendall(message.encode('utf-8'))

        # Receiving data from the server, with a maximum buffer size of 1024 bytes
        data = client_socket.recv(1024)

        # Decoding the received bytes to a UTF-8 string (assuming it's a string)
        response = data.decode('utf-8')

        # Printing the response received from the server
        print(f"Server responded with: {response}")

        # Checking if the user input is 'exit' to close the connection and break the loop
        if message == 'exit':
            print("closing connection")
            break
