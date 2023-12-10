// Dazarus Chapman #vos210
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid_child; // Declared the variable pid_t to store the child process ID

    pid_child = fork(); // Fork a child process

    if (pid_child == -1) { // Determine if fork was success

        perror("Fork failed"); // Print Error for fork
        return 1;
    }

    // Check if this is the child process
    if (pid_child == 0) { // Child Process
        // Print information regarding the child process
        printf("[PID %d] Child process. Parent PID = %d.\n", (int) getpid(), (int) getppid());
    } 
    else // Parent Process
    { 
        // Print information regarding the parent process and Child PID
        printf("[PID %d] Parent process. Child PID = %d.\n", (int) getpid(), (int) pid_child);
    }

    return 0;
}