#include <stdio.h>
#include <pthread.h>

#define MAX_COUNT 1000000000
#define NUM_THREADS 10

int counter = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void* increment_counter(void* arg) {
    for (int i = 0; i < MAX_COUNT / NUM_THREADS; ++i) {
        pthread_mutex_lock(&mutex);
        counter++;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

void* decrement_counter(void* arg) {
    for (int i = 0; i < MAX_COUNT / NUM_THREADS; ++i) {
        pthread_mutex_lock(&mutex);
        counter--;
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];

    for (int i = 0; i < 5; ++i) {
        pthread_create(&threads[i], NULL, increment_counter, NULL);
    }

    for (int i = 5; i < 10; ++i) {
        pthread_create(&threads[i], NULL, decrement_counter, NULL);
    }

    // Join threads for increment
    for (int i = 0; i < 5; ++i) {
        pthread_join(threads[i], NULL);
    }

    printf("Incrementing counter from 0 to 1000000000 using 10 threads\n");
    printf("Final value is %d\n", counter);

    // Reset counter to 0
    counter = 0;

    // Join threads for decrement
    for (int i = 5; i < 10; ++i) {
        pthread_join(threads[i], NULL);
    }

    printf("Decrementing counter from 1000000000 to 0 using 10 threads\n");
    printf("Final value is %d\n", counter);

    return 0;
}