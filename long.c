#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long x = get_long("What is x?\n");
    long y = get_long("what is y?\n");

    printf("%li\n" , x/y);
}
