import socket

HOST = '127.0.0.1'  # Server's IP address
PORT = 65432        # Port to listen on

# Creating a socket using IPv4 and TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Binding the server socket to the specified HOST and PORT
    server_socket.bind((HOST, PORT))

    # Listening for incoming connections on the specified HOST and PORT
    server_socket.listen()

    # Printing a message to indicate that the server is listening
    print(f"Server is listening on {HOST}:{PORT}")

    # Accepting a connection when a client tries to connect
    conn, addr = server_socket.accept()

    # Printing a message indicating a successful connection with the client
    print(f"Connected by {addr}")

    # Communicating with the connected client inside a block
    with conn:
        # Continuously receiving and processing data from the client
        while True:
            # Receiving data from the client with a maximum buffer size of 1024 bytes
            data = conn.recv(1024)

            # Checking if no data is received (client closed the connection)
            if not data:
                break  # Exiting the loop if no data is received (client disconnected)

            # Decoding the received bytes data into a UTF-8 string
            message = data.decode('utf-8')

            # Printing the received message from the client
            print(f"Msg received from client: {message}")

            # Handling different messages received from the client
            if message == 'hello':
                # If the message is 'hello', responding with 'world' to the client
                print("Responding with: world")
                conn.sendall(b'world')  # Sending 'world' encoded as bytes
            elif message == 'exit':
                # If the message is 'exit', responding with 'exit' and breaking the loop
                print("Responding with: exit")
                conn.sendall(b'exit')  # Sending 'exit' encoded as bytes
                break  # Exiting the loop and closing the connection

    # Printing a message to indicate the closure of the connection with the client
    print("Closing connection")