#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    x[0] = 22;
    x[1] = 23;
    x[2] = 24;
    free(x);
}
