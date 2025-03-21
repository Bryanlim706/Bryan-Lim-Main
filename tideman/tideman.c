#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool check_cyclical(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    int candidates_left = candidate_count - 1;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidates_left; j++)
        {
            preferences[ranks[i]][ranks[i + 1 + j]] += 1;
        }
        candidates_left -= 1;
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO

    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] - preferences[j][i] > 0)
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count += 1;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    pair a;
    for (int i = 0; i < pair_count - 1; i++)
    {
        for (int j = 0; j < pair_count - 1; j++)
        {
            if (preferences[pairs[j].winner][pairs[j].loser] <
                preferences[pairs[j + 1].winner][pairs[j + 1].loser])
            {
                a = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = a;
            }
        }
    }
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
// TODO
{
    // 1.lock[0][0]
    locked[pairs[0].winner][pairs[0].loser] = true;

    int i = 1;
    while ((check_cyclical() == true) && (i < (candidate_count * (candidate_count - 1) / 2)))
    {
        // 2.lock[i][i], i = 1
        locked[pairs[i].winner][pairs[i].loser] = true;
        // 3.check if graph is cyclical (return false if cyclical)
        // 4.if true, proceed. if false, terminate
        check_cyclical();
        // 5. i increases by 1, repeat to step 2
        i += 1;
    }
}

// Print the winner of the election
void print_winner(void)
// TODO
{
    int check = 0;
    int x = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == true)
            {
                check += 1;
            }
        }
        if (check == 0)
        {
            printf("%s\n", candidates[i]);
        }
        check = 0;
    }
}

// function returns false if left one winner not being pointed at
bool check_cyclical(void)
{
    int score1 = 0;
    int score = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == true)
            {
                score += 1;
            }
        }
        if (score == 0)
        {
            score1 += 1;
        }
        score = 0;
    }
    if (score1 == 1)
    {
        return false;
    }
    else
    {
        return true;
    }
}
