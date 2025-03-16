#include <cs50.h>
#include <stdio.h>
//prototype
long checksum_13(long x);
long checksum_15(long x);
long checksum_16(long x);
long step_2a(long z);
int main(void)
{
    // GET CARD NUMBER -> CLASSIFY CARD -> CALCULATE CHECKSUM -> PRINT
    long CC_number = get_long("Credit card Number(no dashes):\n");

    long i = 340000000000000;
    long j = 349999999999999;
    long k = 370000000000000;
    long l = 379999999999999;
    long m = 5100000000000000;
    long n = 5599999999999999;
    long o = 4000000000000;
    long p = 4999999999999;
    long q = 4000000000000000;
    long r = 4999999999999999;

    // if 15 digits & start 34/37 (AMEX)
    if ((i <= CC_number && CC_number <= j) || (k <= CC_number && CC_number <= l))
    {
        long c = checksum_15(CC_number);
        if (c % 10 == 0)
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    // if 16 digits & start 51/52/53/54/55 (MASTERCARD)
    else if (m <= CC_number && CC_number <= n)
    {
        long c = checksum_16(CC_number);
        if (c % 10 == 0)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    // if 13 digits & start 4 (VISA)
    else if (o <= CC_number && CC_number <= p)
    {
        long c = checksum_13(CC_number);
        if (c % 10 == 0)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    // if 16 digits & start with 4 (VISA)
    else if (q <= CC_number && CC_number <= r)
    {
        long c = checksum_16(CC_number);
        if (c % 10 == 0)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }

    // INVALID
    else
    {
        printf("INVALID\n");
    }
}
// FUNCTION - Checksum_13
long checksum_13(long x)
{
    // checksum step 1: every other digit *2
    long a = ((x % 100) - (x % 10)) / 10 * 2;
    long b = ((x % 10000) - (x % 1000)) / 1000 * 2;
    long c = ((x % 1000000) - (x % 100000)) / 100000 * 2;
    long d = ((x % 100000000) - (x % 10000000)) / 10000000 * 2;
    long e = ((x % 10000000000) - (x % 1000000000)) / 1000000000 * 2;
    long f = ((x % 1000000000000) - (x % 100000000000)) / 100000000000 * 2;

    // checksum step 2a: making product digits by seperation
    a = step_2a(a);
    b = step_2a(b);
    c = step_2a(c);
    d = step_2a(d);
    e = step_2a(e);
    f = step_2a(f);

    // checksum step 2b: adding product digits to find sum
    long g = (a + b + c + d + e + f);

    // checksum step 3: adding sum to digits that weren't multiplied by 2
    long h = g + (x % 10) + ((x % 1000) - (x % 100)) / 100 + ((x % 100000) - (x % 10000)) / 10000 +
             ((x % 10000000) - (x % 1000000)) / 1000000 +
             ((x % 1000000000) - (x % 100000000)) / 100000000 +
             ((x % 100000000000) - (x % 10000000000)) / 10000000000 +
             ((x % 10000000000000) - (x % 1000000000000)) / 1000000000000;
    return h;
}
// FUNCTION - CHECKSUM_15
long checksum_15(long x)
{
    // checksum step 1: every other digit *2
    long a = ((x % 100) - (x % 10)) / 10 * 2;
    long b = ((x % 10000) - (x % 1000)) / 1000 * 2;
    long c = ((x % 1000000) - (x % 100000)) / 100000 * 2;
    long d = ((x % 100000000) - (x % 10000000)) / 10000000 * 2;
    long e = ((x % 10000000000) - (x % 1000000000)) / 1000000000 * 2;
    long f = ((x % 1000000000000) - (x % 100000000000)) / 100000000000 * 2;
    long s = ((x % 100000000000000) - (x % 10000000000000)) / 10000000000000 * 2;

    // checksum step 2a: making product digits by seperation
    a = step_2a(a);
    b = step_2a(b);
    c = step_2a(c);
    d = step_2a(d);
    e = step_2a(e);
    f = step_2a(f);
    s = step_2a(s);

    // checksum step 2b: adding product digits to find sum
    long g = (a + b + c + d + e + f + s);

    // checksum step 3: adding sum to digits that weren't multiplied by 2
    long h = g + (x % 10) + ((x % 1000) - (x % 100)) / 100 + ((x % 100000) - (x % 10000)) / 10000 +
             ((x % 10000000) - (x % 1000000)) / 1000000 +
             ((x % 1000000000) - (x % 100000000)) / 100000000 +
             ((x % 100000000000) - (x % 10000000000)) / 10000000000 +
             ((x % 10000000000000) - (x % 1000000000000)) / 1000000000000 +
             ((x % 1000000000000000) - (x % 100000000000000)) / 100000000000000;
    return h;
}
// FUNCTION - CHECKSUM_16 xx xx xx xx xx xx xx xx
long checksum_16(long x)
{
    // checksum step 1: every other digit *2
    long a = ((x % 100) - (x % 10)) / 10 * 2;
    long b = ((x % 10000) - (x % 1000)) / 1000 * 2;
    long c = ((x % 1000000) - (x % 100000)) / 100000 * 2;
    long d = ((x % 100000000) - (x % 10000000)) / 10000000 * 2;
    long e = ((x % 10000000000) - (x % 1000000000)) / 1000000000 * 2;
    long f = ((x % 1000000000000) - (x % 100000000000)) / 100000000000 * 2;
    long s = ((x % 100000000000000) - (x % 10000000000000)) / 10000000000000 * 2;
    long t = ((x % 10000000000000000) - (x % 1000000000000000)) / 1000000000000000 * 2;

    // checksum step 2a: making product digits by seperation
    a = step_2a(a);
    b = step_2a(b);
    c = step_2a(c);
    d = step_2a(d);
    e = step_2a(e);
    f = step_2a(f);
    s = step_2a(s);
    t = step_2a(t);

    // checksum step 2b: adding product digits to find sum
    long g = (a + b + c + d + e + f + s + t);

    // checksum step 3: adding sum to digits that weren't multiplied by 2
    long h = g + (x % 10) + ((x % 1000) - (x % 100)) / 100 + ((x % 100000) - (x % 10000)) / 10000 +
             ((x % 10000000) - (x % 1000000)) / 1000000 +
             ((x % 1000000000) - (x % 100000000)) / 100000000 +
             ((x % 100000000000) - (x % 10000000000)) / 10000000000 +
             ((x % 10000000000000) - (x % 1000000000000)) / 1000000000000 +
             ((x % 1000000000000000) - (x % 100000000000000)) / 100000000000000;
    return h;
}
// checksum step 2a
long step_2a(long z)
{
    if (z > 9)
    {
        long y = (z % 10) + 1;
        return y;
    }
    else
    {
        return z;
    }
}
