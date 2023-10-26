#define _DEFAULT_SOURCE /* Get on_exit() declaration from <stdlib.h> */
// _BSD_SOURCE is deprecated but if you have issues,
// replace _DEFAULT_SOURCE with _BSD_SOURCE above
#include <stdio.h>
#include <stdlib.h>

#ifdef __linux__ /* Few UNIX implementations have on_exit() */
#define HAVE_ON_EXIT
#endif

static void atexitFunc1(void) { printf("atexit function 1 called\n"); }

static void atexitFunc2(void) { printf("atexit function 2 called\n"); }

#ifdef HAVE_ON_EXIT
static void onexitFunc(int exitStatus, void *arg) { printf("on_exit function called: status=%d, arg=%ld\n", exitStatus, (long)arg); }
#endif

int main(int argc, char *argv[])
{
#ifdef HAVE_ON_EXIT
    if (on_exit(onexitFunc, (void *)10) != 0) {
        perror("on_exit 1");
        exit(EXIT_FAILURE);
    }
#endif
    if (atexit(atexitFunc1) != 0) {
        perror("atexit 1");
        exit(EXIT_FAILURE);
    }
    if (atexit(atexitFunc2) != 0) {
        perror("atexit 2");
        exit(EXIT_FAILURE);
    }
#ifdef HAVE_ON_EXIT
    if (on_exit(onexitFunc, (void *)20) != 0) {
        perror("on_exit 2");
        exit(EXIT_FAILURE);
    }
#endif

    exit(2);
}
