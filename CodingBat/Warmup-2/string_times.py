# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  cont = 0
  result = ""
  while cont < n:
    result += str
    cont += 1
  return result