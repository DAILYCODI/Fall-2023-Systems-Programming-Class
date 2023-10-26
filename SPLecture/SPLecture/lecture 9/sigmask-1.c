#include <signal.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
    sigset_t blockSet;
    sigset_t prevMask;

    // create an empty set
    sigemptyset(&blockSet);
    // add SIGINT to the empty set
    sigaddset(&blockSet, SIGINT);

    int result = sigprocmask(SIG_BLOCK, &blockSet, &prevMask);
    if (result == -1)
    {
        printf("error with blocking\n");
        exit(-1);
    }
    // code that should not be interrupted
    sleep(10);

    result = sigprocmask(SIG_SETMASK, &prevMask, NULL);
    if (result == -1)
    {
        printf("error with restoring\n");
        exit(-1);
    }

    for (int i = 0; i < 20; i++)
    {
        printf("counter: %d\n", i);
        sleep(1);
    }
}