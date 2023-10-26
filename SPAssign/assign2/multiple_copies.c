//Dazarus Chapman - Vos210
#include <stdio.h>
#include <stdlib.h>

// Function to check if a file exists
int fileExists(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file) {
        fclose(file);
        return 1; // The file exists
    }
    return 0; // The file doesn't exist
}
int main(int argc, char *argv[]) {
    // Check if exactly three arguments are provided
    if (argc != 4) {
        // Display usage error message
        printf("Usage: %s input copy copy1\n", argv[0]);
        return 1; // Exit with an error code
    }
     // Check if the source file exists
    if (!fileExists(argv[1])) {
        // Display an error message and exit
        printf("Opening Error!: %s does not exist\n", argv[1]);
        return 1; // Exit with an error code
    }
    // Define source and destination file pointers
    FILE *input, *copy, *copy1;

    // Open the source file in read mode
    input = fopen(argv[1], "r");

    // Check if the source file opened successfully
    if (input == NULL) {
        perror("Error opening source file");
        return 1; // Exit with an error code
    }

    // Open the first destination file in write mode
    copy = fopen(argv[2], "w");

    // Check if the first destination file opened successfully
    if (copy == NULL) {
        perror("Error opening destination file 1");
        fclose(input); // Close the source file
        return 1;      // Exit with an error code
    }

    // Open the second destination file in write mode
    copy1 = fopen(argv[3], "w");

    // Check if the second destination file opened successfully
    if (copy1 == NULL) {
        perror("Error opening destination file 2");
        fclose(input); // Close the source file
        fclose(copy);  // Close the first destination file
        return 1;      // Exit with an error code
    }

    // Copy contents from source to destination files
    int ch;
    while ((ch = fgetc(input)) != EOF) {
        fputc(ch, copy);  // Copy to the first destination file
        fputc(ch, copy1); // Copy to the second destination file
    }

    // Close all files
    fclose(input);
    fclose(copy);
    fclose(copy1);

    // Display success message
    printf("Files copied successfully.\n");

    return 0; // Exit with success
}
