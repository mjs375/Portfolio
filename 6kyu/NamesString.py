def namelist(names):
    if not names:
        return ""
    if len(names) == 1:
        return names[0]["name"]
    
    x = ""
    for i, name in enumerate(names[::-1]):
        if i == 0:
            x = f"& {name['name']}" + x
        elif i == 1:
            x = f"{name['name']} " + x
        else:
            x = f"{name['name']}, " + x
    return x
  
  
"""
Given: an array containing hashes of names
Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
  Example:
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
      # returns 'Bart, Lisa & Maggie'
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
      # returns 'Bart & Lisa'
    namelist([ {'name': 'Bart'} ])
      # returns 'Bart'
  """
