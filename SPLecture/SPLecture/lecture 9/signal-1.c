#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static void sig_int_handler(int sig)
{
    printf("Ouch sigint!\n");
}

// static void sig_term_handler(int sig)
// {
//     printf("Ouch sigterm!\n");
// }

int main()
{
    sig_t result1 = signal(SIGINT, sig_int_handler);
    if (result1 == SIG_ERR)
    {
        printf("SIGINT handler error\n");
        exit(-1);
    }

    // sig_t result2 = signal(SIGTERM, sig_int_handler);
    // if (result2 == SIG_ERR)
    // {
    //     printf("SIGTERM handler error\n");
    //     exit(-1);
    // }

    for (int i = 0;; i++)
    {
        printf("%d\n", i);
        sleep(3);
    }
}