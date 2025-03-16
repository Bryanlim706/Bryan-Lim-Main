#include <stdio.h>

void try(void);
int main(void)
{
    for(int i=0; i<3; i++)
    {
        try();
    }

}
void try(void)
{
    printf("meowww!\n");
}

