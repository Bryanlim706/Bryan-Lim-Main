#include <cs50.h>
#include <stdio.h>

//constant
const int N = 3;

//prototype
float average(int length, int array[]);

int main(void)
{
    //get scores
    int score[N];
    for (int i = 0; i < N; i++)
    {
        score[i] = get_int("score: ");
    }
    printf("average: %f\n", average(N, score));
}

    //average function
float average(int length, int array[])
{
    int sum = 0;
    for(int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length ;
}

