# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    soma = a + b
    if a == b:
        soma += soma
    return soma