#1.2.9---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def sum_recur(term, a, next, b):
    return 0 if a > b else term(a) + sum_recur(term, next(a), next, b)
   
def simpsons_rule_integral(f, a, b, n):
    h = (b - a) / n
    def next(x):
        k = round((x - a) / h)
        return a + (k + 1) * h
    def term(y):
        k = round((y - a) / h)
        return f(y) if k == 0 or k == n else 4 * f(y) if k % 2 == 1 else 2 * f(y)
    return (h / 3) * sum_recur(term, a, next, b)


def test_simpsons():
    print(simpsons_rule_integral(lambda x: x ** 3, 0, 1, 3))
    print(simpsons_rule_integral(lambda x: x ** 3, 0, 1, 10))
    print(simpsons_rule_integral(lambda x: x ** 3, 0, 1, 50))
    print(simpsons_rule_integral(lambda x: x ** 3, 0, 1, 100))
    print(simpsons_rule_integral(lambda x: x ** 3, 0, 1, 200))
    print(simpsons_rule_integral(lambda x: x ** 3, 0, 1, 500))
    print(simpsons_rule_integral(lambda x: x ** 3, 0, 1, 800))


#1.3.0---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def sum(term, a, next, b):
    def iterate(counter, result):
        return result if counter > b else iterate(next(counter), result + term(counter))
    return iterate(a, 0)


#1.3.1 Q1---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def product_recur(term, a, next, b):
    return 1 if a > b else term(a) * product_recur(term, next(a), next, b)


def factorial(n):
    def term(m):
        return m
    def next(a):
        return a + 1
    return product_recur(term, 1, next, n)


def pi_approx_recur(n):
    def term(m):
        return ((m ** 2 - 1) / m ** 2)
    def next(a):
        return a + 2
    return 4 * product_recur(term, 3, next, n)


#1.3.1 Q2---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def product_iter(term, a, next, b):
    def iterate(counter, result):
        return result if counter > b else iterate(next(counter), result * term(counter))
    return iterate(a, 1)


def pi_approx_iter(n):
    def term(m):
        return ((m ** 2 - 1) / m ** 2)
    def next(a):
        return a + 2
    return 4 * product_iter(term, 3, next, n)


#1.3.2 Q1---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def accumulate_recur(combiner, null_value, term, a, next, b):
    return null_value if a > b else combiner(term(a), accumulate_recur(combiner, null_value, term, next(a), next, b))


def sum_recur_accumulate(term, a, next, b):
    def combiner(x, y):
        return x + y
    return accumulate_recur(combiner, 0, term, a, next, b)


def product_recur_accumulate(term, a, next, b):
    def combiner(x, y):
        return x * y
    return accumulate_recur(combiner, 1, term, a, next, b)


def test_accumulate_recur():
    print(sum_recur_accumulate(lambda x: x ** 2, 1, lambda x: x + 1, 5)) #55
    print(product_recur_accumulate(lambda x: x ** 2, 1, lambda x: x + 1, 5)) #14400


#1.3.2 Q2---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def accumulate_iter(combiner, null_value, term, a, next, b):
    def iterate(counter, result):
        return result if counter > b else iterate(next(counter), combiner(term(counter), result))
    return iterate(a, null_value)


def test_accumulate_iter():
    print(accumulate_iter(lambda x,y: x + y, 0, lambda x: x ** 2, 1, lambda x: x + 1, 5)) #55
    print(accumulate_iter(lambda x,y: x * y, 1, lambda x: x ** 2, 1, lambda x: x + 1, 5)) #14400


#1.3.3---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filtered_accumulate(filter, combiner, null_value, term, a, next, b):
    return null_value if a > b else filtered_accumulate(filter, combiner, null_value, term, next(a), next, b) if filter(a) == False else combiner(term(a), filtered_accumulate(filter, combiner, null_value, term, next(a), next, b))


from sympy import isprime
def sum_squares_prime(a, b):
    return filtered_accumulate(isprime, (lambda x, y: x + y), 0, lambda x: x ** 2, a, lambda x: x + 1, b)


import math
def product_pos_int_relatively_prime(n):
    def is_gcd(x):
        return math.gcd(x, n) == 1
    return filtered_accumulate(is_gcd, (lambda x, y: x * y), 1, lambda x: x, 1, lambda x: x + 1, n - 1)


def test_ssp():
    print(sum_squares_prime(2, 6)) #38


def test_ppirp():
    print(product_pos_int_relatively_prime(8)) #105


test_ppirp()


#1.3.4
"""
syntax error. f(f) will result in calling a primitive data as a function.


notes has an error at the end of this question. 2 is a primitive.
"""



