#include <cs50.h>
#include <stdio.h>

int main( void)
{
    int x = get_int("what is x?\n");
    int y = get_int("what is y?\n");

    if (x > y)
    {
        printf("x is greater than y\n");
    }
    else if (x < y)
    {
        printf("x is smaller than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    }
}
