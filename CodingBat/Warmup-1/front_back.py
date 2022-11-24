# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    meio = str[1:len(str) - 1]

    if len(str) <= 1:
        return str

    return str[len(str) - 1] + meio + str[0]
