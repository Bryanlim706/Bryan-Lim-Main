#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{
    char *s = get_string("s:");
    if (s == NULL)
    {
        return 1;
    }
    int len = strlen(s);
    char *t = malloc(len + 1);
    if (t == NULL)
    {
        return 1;
    }
    strcpy(t, s);
    t[0] = toupper(t[0]);

    printf("%s\n", s);
    printf("%s\n", t);

    free(t);
    return 0;

}
