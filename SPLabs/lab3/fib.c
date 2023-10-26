//Dazarus Chapman
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Naive recursive Fibonacci implementation in C
unsigned long long fibonacci_naive(int n) {
    if (n < 2) {
        return n;
    } else {
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
    }
}

// Memoization for Fibonacci in C
unsigned long long memo[100]; // Adjust the size as needed

unsigned long long fibonacci_memo(int n) {
    if (n < 2) {
        return n;
    } else if (memo[n] != 0) {
        return memo[n];
    } else {
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2);
        return memo[n];
    }
}

int main() {
    clock_t start_time, end_time;
    double elapsed_time;

    // Naive approach
    start_time = clock();
    unsigned long long result_naive = fibonacci_naive(40);
    end_time = clock();
    elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Naive approach: F(40) = %llu, Time taken: %f seconds\n", result_naive, elapsed_time);

    // Memoized approach
    start_time = clock();
    unsigned long long result_memo = fibonacci_memo(40);
    end_time = clock();
    elapsed_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Memo approach: F(40) = %llu, Time taken: %f seconds\n", result_memo, elapsed_time);

    return 0;
}