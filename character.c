#include <cs50.h>
#include <stdio.h>

int main(void)

{
    char c= get_char("do you agree?\n");

    if(c=='y'||c=='Y')
    printf("agreed\n");

    else if (c=='n'||c=='N')
    printf("disagreed\n");

    else
    printf("invalid\n");


}
