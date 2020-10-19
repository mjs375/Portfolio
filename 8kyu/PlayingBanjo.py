def areYouPlayingBanjo(name):
    # Implement me!
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
The function takes a name as its only argument, and returns one of the following strings:
    name + " plays banjo" 
    name + " does not play banjo"
"""
