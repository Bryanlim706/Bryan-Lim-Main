#include <stdio.h>

void meow(int n);
int main(void)
{
    meow(3);
}
void meow(int n)
{
    for(n=0; n<3; n++)
    {
        printf("meowwww!\n");
    }
}
