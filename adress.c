#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = 50;
    printf("%p\n", &x);
    int *p = &x;
    printf("%p\n", p);
    printf("%i\n\n\n", *p);

    string s = "HI!";
    printf("%p ", &s[0]);
    printf("%p ", &s[1]);
    printf("%p ", &s[2]);
    printf("%p ", &s[3]);

}
