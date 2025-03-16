#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{
    char *a = get_string("a:");
    int len = strlen(a);
    char *b = malloc(len + 1);

    for(int i = 0; i < len + 1; i++)
    {
        b[i] = a[i];
    }
    b[0] = toupper(b[0]);

    printf("%s\n", a);
    printf("%s\n", b);
}
