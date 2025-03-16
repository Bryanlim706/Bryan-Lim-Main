#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//prototype
bool check(const char *s, const char *t);

int main(void)
{
    //string s is in NORMALCHARS sequence. string t is the normal word

    //declare
    char *s = malloc(20 *sizeof(char));
    char *t = malloc(20 *sizeof(char));

    const char *p_s = get_string("s: ");
    const char *p_t = get_string("t: ");
    if (check(s, t) == true)
    {
        printf("yes");
    }
    else
    {
        printf("no");
    }
}

// Function to check if s is a subsequence of t
bool check(const char *s, const char *t)
{
    // Pointers for the strings
    const char *p_s = s;
    const char *p_t = t;

    // Iterate through the target string t
    while (*p_t)
    {
        // If current characters match, move the pointer in s
        if (*p_s == *p_t)
        {
            p_s++;
        }
        // Move the pointer in t regardless of match
        p_t++;
    }

    // If we've matched all characters in s, return true
    return *p_s == \0;
}

