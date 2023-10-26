#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    printf("Hello world\n");
    write(STDOUT_FILENO, "Ciao\n", 5);

    if (fork() == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    /* Both child and parent continue execution here */

    exit(EXIT_SUCCESS);
}
