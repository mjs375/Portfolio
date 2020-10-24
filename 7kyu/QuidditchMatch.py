# # # # # # R E F A C T O R E D : # # # # # # #






# # # # # # 1 S T _ A T T E M P T : # # # # # #
def game_winners(gryffindor, slytherin):
    #list = [gryffindor, slytherin] #list of lists
    g_pts, s_pts = int(), int() #zero'd scorecard
    #
    for item in gryffindor:
        if isinstance(item, int):
            g_pts += item
        elif item in "yes":
            g_pts += 150
        else: #no
            pass
    for item in slytherin:
        if isinstance(item, int):
            s_pts += item
        elif item in "yes":
            s_pts += 150
        else: #no snitch
            pass
    if g_pts > s_pts:
        return "Gryffindor wins!"
    elif s_pts > g_pts:
        return "Slytherin wins!"
    else: #tie
        return "It's a draw!"



"""
It's the most hotly anticipated game of the school year - Gryffindor vs Slytherin! Write a function which returns the winning team.
You will be given two arrays with two values.
The first given value is the number of points scored by the team's Chasers and the second a string with a 'yes' or 'no' value if the team caught the golden snitch!
The team who catches the snitch wins their team an extra 150 points - but doesn't always win them the game.
  gameWinners([150, 'yes'],[200, 'no']) //'Gryffindor wins!'
  gameWinners([400, 'no'],[350, 'yes']) //'Slytherin wins!'
If the score is a tie return "It's a draw!""
  The game only ends when someone catches the golden snitch, so one array will always include 'yes' or 'no.' Points scored by Chasers can be any positive integer.
"""
