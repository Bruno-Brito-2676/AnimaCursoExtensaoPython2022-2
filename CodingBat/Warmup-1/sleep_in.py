#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(fim_de_semana, ferias):
  if not fim_de_semana or ferias:
    return True
  else:
    return False
