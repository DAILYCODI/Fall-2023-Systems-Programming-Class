#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    char *hello = "world";
    char *exit_msg = "exit";

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Binding the socket to the provided port
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // Listening for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    // Accepting incoming connection
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    // Receiving messages from client
    while (1) {
        memset(buffer, 0, sizeof(buffer));
        if (read(new_socket, buffer, BUFFER_SIZE) <= 0) {
            perror("read");
            break;
        }
        printf("Msg received from client: %s\n", buffer);

        // Check received message and respond accordingly
        if (strcmp(buffer, "hello") == 0) {
            send(new_socket, hello, strlen(hello), 0);
            printf("Responding with: %s\n", hello);
        } else if (strcmp(buffer, exit_msg) == 0) {
            send(new_socket, exit_msg, strlen(exit_msg), 0);
            printf("Responding with: %s\n", exit_msg);
            break;
        }
    }

    // Closing sockets
    close(new_socket);
    close(server_fd);
    printf("closing connection\n");
    return 0;
}
