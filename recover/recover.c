#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// establish reading units
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // admin work & open input
    if (argc != 2)
    {
        printf("Usage: ./recover inputfile");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Unable to open file");
        return 2;
    }

    // make buffer
    BYTE buffer[512];

    // establish filename
    char filename[8];
    int filename_count = 0;

    // create and set output file to NULL
    FILE *output = NULL;

    while (fread(buffer, sizeof(BYTE) * 512, 1, input) == 1)
    {
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) &&
            ((buffer[3] & 0xf0) == 0xe0))
        {
            if (output != NULL)
            {
                fclose(output);
            }

            // settle updating filename
            sprintf(filename, "%03i.jpg", filename_count++);
            output = fopen(filename, "w");
        }
        if (output != NULL)
        {
            fwrite(buffer, sizeof(BYTE) * 512, 1, output);
        }
    }

    if (output != NULL)
    {
        fclose(output);
    }

    fclose(input);
    return 0;
}
