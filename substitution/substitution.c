#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Ensuring command-line arguments are valid
    if (argc != 2)
    {
        printf("usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("key must contain 26 characters\n");
        return 1;
    }
    for (int i = 0; i < 26; i++)
    {
        if (argv[1][i] < 'A' || argv[1][i] > 'z')
        {
            printf("key must only contain alphabetical charaters\n");
            return 1;
        }
        else if (argv[1][i] < 'a' && argv[1][i] > 'Z')
        {
            printf("key must only contain alphabetical charaters\n");
            return 1;
        }
    }
    int score = 0;
    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < 26; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                score += 1;
            }
        }
    }
    if (score != 26)
    {
        printf("key must not contain repeated letters\n");
        return 1;
    }

    // prompt for plaintext
    string plaintext = get_string("plaintext: ");

    // converting plaintext to ciphertext
    int l = strlen(plaintext);
    for (int i = 0; i < l; i++)
    {
        if (isupper(plaintext[i]))
        {
            int c = plaintext[i] - 'A';
            plaintext[i] = toupper(argv[1][c]);
        }
        else if (islower(plaintext[i]))
        {
            int c = plaintext[i] - 'a';
            plaintext[i] = tolower(argv[1][c]);
        }
    }
    // printing ciphertext
    printf("ciphertext: %s\n", plaintext);
    return 0;
}
