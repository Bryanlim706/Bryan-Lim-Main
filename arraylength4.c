#include <cs50.h>
#include <stdio.h>
#include <string.>

int main(void)
{
    string before = get_string("Before: ");
    printf("after: ");

    for(int i = 0, n = strlen(before); i < n; i++)
    {
        if(s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
