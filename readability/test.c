#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("text: ");
    int c = strlen(text);
    int score = 0;
    for(int i = 0; i < c; i++)
    {
        if(text[i] == '.' && text[i + 1] == ('\0'))
        {
            score += 1;
        }


    }
    printf("%i", score);

}
