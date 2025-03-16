#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    string number;
}person;

int main(void)
{
    person people[3];

    people[0].name = "Bryan";
    people[0].number = "+65-83568883";
}
