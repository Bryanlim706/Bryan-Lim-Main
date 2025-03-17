#include <cs50.h>
#include <stdio.h>
void print_row(int n);

int main(void)
{
    // ask for height of pyramid allowing 1-8
    int h;
    do
    {
        h = get_int("Between 1 to 8, how tall is the pyramid?\n");
    }
    while (h < 1 || h > 8);

    // make pyramid
    for (int n = 1; n < (h + 1); n++)
    {
        print_row(n);
    }
}

void print_row(int n)
{
    for (int a = 0; a < (8 - n); a++)
    {
        printf(" ");
    }
    for (int a = 0; a < n; a++)
    {
        printf("#");
    }
    printf("  ");
    for (int a = 0; a < n; a++)
    {
        printf("#");
    }
    printf("\n");
}
