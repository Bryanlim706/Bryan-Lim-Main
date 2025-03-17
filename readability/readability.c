#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// prototypes
float L_calc(string text);
float S_calc(string text);
int no_words(string text);
int no_letters(string text);
int no_sentences(string text);
int no_char(string text);

int main(void)
{
    string text = get_string("text: ");
    int index = round(0.0588 * L_calc(text) - 0.296 * S_calc(text) - 15.8);
    if (index > 15)
    {
        printf("Grade 16+\n");
    }
    else if (index <= 15 && index >= 1)
    {
        printf("Grade %i\n", index);
    }
    else
    {
        printf("Before Grade 1\n");
    }
}

// calculate average number of letters per 100 words, L
float L_calc(string text)
{
    float c = no_letters(text);
    return ((100 * c) / (no_words(text)));
}

// calculate the average number of sentences per 100 words, S
float S_calc(string text)
{
    float c = no_sentences(text);
    return ((100 * c) / (no_words(text)));
}

// calculate number of words
int no_words(string text)
{

    // calculate number of spaces
    int c = no_char(text);
    int score = 0;
    for (int i = 0; i < c; i++)
    {
        if (text[i] == ' ')
        {
            score += 1;
        }
    }

    // calculate number of words
    return (score + 1);
}

// calculate number of letters
int no_letters(string text)
{
    int c = no_char(text);
    int score = 0;
    for (int i = 0; i < c; i++)
    {
        if (text[i] > 64 && text[i] < 123)
        {
            score += 1;
        }
    }
    return score;
}

// calculate number of sentences
int no_sentences(string text)
{
    int c = no_char(text);
    int score = 0;
    for (int i = 0; i < c; i++)
    {
        if ((text[i] == '.' && text[i + 1] == '\0') | (text[i] == '.' && text[i + 1] == ' ') |
            (text[i] == '.' && text[i + 1] == '"') | (text[i] == '?') | (text[i] == '!'))
        {
            score += 1;
        }
    }
    return score;
}

// calculate number of characters
int no_char(string text)
{
    return strlen(text);
}
