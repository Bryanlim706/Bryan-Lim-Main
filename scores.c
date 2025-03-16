#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get scores
    int score[3];
    score[0] = get_int("score 1: ");
    score[1] = get_int("score 2: ");
    score[2] = get_int("score 3: ");

    //print average
    printf("average: %f\n", (score[0] + score[1] + score[2]) / 3.0);
}
