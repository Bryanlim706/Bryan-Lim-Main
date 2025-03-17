// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// for load function
char *buffer;

// for size function
int counter;

// for hash function
int return_counter = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// prototype
bool unloader(node *n);

// TODO: Choose number of buckets in hash table
const unsigned int N = 456975;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_value1 = 0;
    hash_value1 = hash(word);

    node *cursor = table[hash_value1];

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number - from online
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return_counter = 0;
    if (strlen(word) == 1)
    {
        return (toupper(word[0]) - 'A');
    }
    else if (strlen(word) == 2)
    {
        return ((26 * (toupper(word[0]) - 'A')) + (toupper(word[1]) - 'A'));
    }
    else if (strlen(word) == 3)
    {
        return (26 * 26 * (toupper(word[0]) - 'A') + (26 * (toupper(word[1]) - 'A')) +
                (toupper(word[2]) - 'A'));
    }
    else if (strlen(word) > 3)
    {
        for (int i = 3; i < strlen(word); i++)
        {
            return_counter += (toupper(word[i]) - 'A');
        }
        return (26 * 26 * 26 * (toupper(word[0]) - 'A') + (26 * 26 * (toupper(word[1]) - 'A')) +
                (26 * (toupper(word[2]) - 'A')) + (toupper(word[3]) - 'A') + return_counter);
    }
    else
    {
        return (toupper(word[0]) - 'A');
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *source = fopen(dictionary, "r");

    if (source == NULL)
    {
        printf("unable to open %s", dictionary);
        return false;
    }

    buffer = malloc(46 * sizeof(char));

    if (buffer == NULL)
    {
        return false;
    }

    int hash_value = 0;

    // copy word from dictionary to hash table
    while (fscanf(source, "%s", buffer) != EOF)
    {
        hash_value = 0;
        hash_value = hash(buffer);
        node *a = NULL;

        if ((table[hash_value]) == NULL)
        {
            node *buffer1 = malloc(sizeof(node));
            if (buffer1 == NULL)
            {
                return false;
            }
            strcpy(buffer1->word, buffer);
            buffer1->next = NULL;

            table[hash_value] = buffer1;
        }
        else
        {
            node *buffer1 = malloc((sizeof(node)) * (LENGTH + 1));
            if (buffer1 == NULL)
            {
                return false;
            }
            strcpy(buffer1->word, buffer);
            buffer1->next = NULL;

            a = table[hash_value];
            buffer1->next = a;
            table[hash_value] = buffer1;
        }

        counter += 1;

        for (int i = 0; i < LENGTH + 1; i++)
        {
            buffer[i] = '\0';
        }
    }
    fclose(source);

    // check hash table to return true
    int returnvalue_checker = 0;
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            returnvalue_checker += 1;
        }
    }
    if (returnvalue_checker > 0)
    {
        return true;
    }

    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *tmp = NULL;
    node *cursor = NULL;

    for (int i = 0; i < N; i++)
    {
        tmp = table[i];
        cursor = table[i];
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    free(buffer);
    return true;
}
