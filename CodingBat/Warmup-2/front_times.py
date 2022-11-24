#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
  result = ""
  tres = ""
  cont = 0
  if len(str) < 3:
    tres = str
    while cont < n:
      result += tres
      cont += 1
  else:
    tres = str[:3]
    while cont < n:
      result += tres
      cont += 1
  return result