#include <cs50.h>
#include <stdio.h>


int main(void)


    {
        int n= get_int("height?\n");

        for(int a=0; a<(8-n); a++)
        {
            printf(" ");
        }
        for(int a=0; a<n; a++)
        {
            printf("#");
        }
        printf("  ");
        for(int a=0; a<n; a++)
        {
            printf("#");
        }
        for(int a=0; a<(8-n); a++)
        {
            printf(" ");
        }
        printf("\n");
    }
