#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("string: ");

    int i = 0;
    while(s[i] != 0)
    {
        i++;
    }
    printf("%i\n",i);
}
