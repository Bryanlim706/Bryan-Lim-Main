#include <cs50.h>
#include <stdio.h>

int add(int a, int b);
int main(void)
{
    int x = get_int("what is x?\n");
    int y = get_int("what is y?\n");
    printf("%i\n", add(x,y));
}

int add(int a, int b)
{
    return (a+b);
}
