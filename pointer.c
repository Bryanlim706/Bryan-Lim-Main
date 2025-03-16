#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
    printf("%c\n", *(s + 3));

    char *t = get_string("t:");
    char *u = get_string("u:");

    if(strcmp(t,u) == 0)
    {
        printf("same\n");
    }
    else
    {
        printf("different\n");
    }

    printf("%p\n", t);
    printf("%p\n", u);
}

