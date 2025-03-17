#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// prototypes
int word_score(string P);
char *to_uppercase(string P);

int main(void)
{
    // ask user for words
    string P1 = get_string("player 1: ");
    string P2 = get_string("player 2: ");

    // make all to upper case
    for (int i = 0, l = strlen(P1); i < l; i++)
    {
        P1 = to_uppercase(P1);
        P2 = to_uppercase(P2);
    }

    // printing the player that won
    int S1 = word_score(P1);
    int S2 = word_score(P2);
    if (S1 > S2)
    {
        printf("Player 1 wins!\n");
    }
    else if (S2 > S1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

// to uppercase functiom
char *to_uppercase(string P)
{
    for (int i = 0, l = strlen(P); i < l; i++)
    {
        if (islower(P[i]))
        {
            P[i] = (toupper(P[i]));
        }
        else
        {
            P[i] = P[i];
        }
    }
    return P;
}

// word to score function
int word_score(string P)
{
    int score = 0;

    for (int i = 0, l = strlen(P); i < l; i++)
    {
        if (P[i] == 'A' || P[i] == 'E' || P[i] == 'I' || P[i] == 'L' || P[i] == 'N' ||
            P[i] == 'O' || P[i] == 'R' || P[i] == 'S' || P[i] == 'T' || P[i] == 'U')
        {
            score += 1;
        }
        else if (P[i] == 'D' || P[i] == 'G')
        {
            score += 2;
        }
        else if (P[i] == 'B' || P[i] == 'C' || P[i] == 'M' || P[i] == 'P')
        {
            score += 3;
        }
        else if (P[i] == 'F' || P[i] == 'H' || P[i] == 'V' || P[i] == 'W' || P[i] == 'Y')
        {
            score += 4;
        }
        else if (P[i] == 'K')
        {
            score += 5;
        }
        else if (P[i] == 'J' || P[i] == 'X')
        {
            score += 8;
        }
        else if (P[i] == 'Q' || P[i] == 'Z')
        {
            score += 10;
        }
    }
    return score;
}
