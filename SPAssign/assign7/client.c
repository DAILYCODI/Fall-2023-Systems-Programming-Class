#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char buffer[BUFFER_SIZE] = {0};
    char *exit_msg = "exit";

    // Creating socket file descriptor
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket creation error");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        perror("Invalid address/ Address not supported");
        return -1;
    }

    // Connecting to the server
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection Failed");
        return -1;
    }

    while (1) {
        printf("Msg to send: ");
        fgets(buffer, BUFFER_SIZE, stdin);
        buffer[strcspn(buffer, "\n")] = 0; // Remove newline character

        // Sending user input to server
        send(sock, buffer, strlen(buffer), 0);

        // Check for exit command
        if (strcmp(buffer, exit_msg) == 0) {
            break;
        }

        // Receiving server's response
        memset(buffer, 0, sizeof(buffer));
        if (recv(sock, buffer, BUFFER_SIZE, 0) <= 0) {
            perror("recv");
            break;
        }
        printf("Server responded with: %s\n", buffer);
    }

    // Closing the socket
    close(sock);
    printf("closing connection\n");
    return 0;
}
