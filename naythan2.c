#include <stdio.h>
#include <stdbool.h>

//naythan.c - string s is in NORMALCHARS sequence. string t is the normal word.

int t_char_counter = 0;
int position_normalchar_t[20];
int counter = 0;

bool check(const char *s, const char *t)
{
    //empty position_normalchar
    for (int i = 0; i < 20; i++)
    {
        position_normalchar_t[i] = 0;
    }
    // Pointers for the strings
    const char *s_pointer = s;
    const char *t_pointer = t;

    // move down string t
    while (*t_pointer)
    {
        // If current characters same, move to next char in s
        if (*s_pointer == *t_pointer)
        {
            s_pointer++;
            position_normalchar_t[counter] = t_char_counter;
            counter += 1;

        }
        // move to next char in t
        t_pointer++;

        t_char_counter += 1;
    }


    // If all char in s matched, return true
    return *s_pointer == '\0';
}

//get input s and t, print response
int main(void)
{
    char s[21];
    char t[21];
    printf("s: ");
    scanf("%20s", s);
    printf("t: ");
    scanf("%20s", t);

    if (check(s, t))
    {
        printf("yes.\n");
    }
    else
    {
        printf("no.\n");
    }

    return 0;
}
