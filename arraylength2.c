#include <cs50.h>
#include <stdio.h>

int string_length(string s);

int main(void)
{
    //ask name and print length
    string name = get_string("name: \n");
    printf("%i\n", string_length(name));
}

int string_length(string s)
{
    //function for length of string
    int i = 0;
    while(s[i] != 0)
    {
        i++;
    }
    return i;
}
