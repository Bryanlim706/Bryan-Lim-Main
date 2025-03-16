#include <stdio.h>
#include <string.h>

int main (void)
{
    //declaring
    int L_s = strlen(s);
    int L_t = strlen(t);
    int normal_char_in_t = 0;
    char *NORMALCHARS[counter];
    int counter = 0;


    for (int i = 0; i < 2; i++)
    {
        buffer[i] = 0;
    }

    //calculating normal_char_in_t
    for (int i = 0; i < L; i++)
    {
        normal_char_in_t += 1;

        if (t[i] == “*”  | t[i] == “.”)
        {
            normal_char_in _t  -= 1;
        }
    }

    //scan down t, storing normal chars
    for (int i = 0; i < L_t ; i++)
    {
        if (t[i + 1] != “*” && t[i] != “.”)
        {
           NORMALCHARS[counter] = t[i];
           counter += 1;
        }
    }
    counter = 0;

    //now NORMALCHARS[counter] stores back to back normal chars in t
}




