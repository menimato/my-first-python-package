from emoji import emojize

def hello(name = "world"):
  """hello
  
  Prints a brief charming message greeting a person.
  
  Parameters
  ----------
  name : str
    Name of the user/person to be greeted.

  Returns
  -------
  None.
  
  Examples
  --------
  >>> hello('Bruno')
  """
  
  message = f"Hello {name}! Welcome to my first Python package! {emojize(':thumbs_up:')}"

  return message