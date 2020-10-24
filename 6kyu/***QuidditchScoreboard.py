def quidditch_scoreboard(teams, actions):
    #
    ## 1. GET TEAM_NAMES/SCORE DICT
    team_list = teams.split(" vs ") # ['Kenmare Kestrels', 'Barnton']
    game_dict = dict.fromkeys(team_list, 0) #turn list into dict to tally points
    #print(game_dict) #{'Appleby Arrows': 0, 'Montrose Magpies': 0}
    #
    ## 2. GET TEAM/ACTIONS DICT
    #
    game = dict(kv.split(":") for kv in actions.split(",")) #creates kv pairs of team:action, team:action in DICT
    #print(game) 
    #
    ## 3. Iterate through 'game'
    #
    game_items = game.items() #[(key, value), (key, value), ...] Creates iterable dict
    for team, action in game_items: #iterate moments of gameplay
        #print(team, "|", action) # Montrose Magpies | Quaffle goal
        for who in team_list:
            if team == who: #ID team
                #print (team, who, action) # Montrose Magpies Montrose Magpies
                if action[-4:] == "goal": #goal: add 10 pts to 'team/who'
                    #print("goal", action)#determine action
                    game_dict = pts(game_dict, team, 10)
                elif action[-4:] == "foul": #foul: deduct 30 pts from 'team/who'
                    game_dict = pts(game_dict, team, -30)
                else: # ...=="Caught Snitch": add 150 pts
                    #print("SNITCH CAUGHT!")
                    game_dict = pts(game_dict, team, 150)
    #print(game_dict)
    # GAME FULLY PROCESSED, RETURN OUTCOME:
    outcome = ""
    for k, v in game_dict.items():
        outcome = outcome + "{}:{}, ".format(k, v)
    #Remove trailing ", " on 2nd team:
    outcome = outcome[0:-2] #remove last 2 elem of string
    return outcome 

def pts(game_dict, team, points): #scoreboard, scoring_team, score(+-)
    #ex_dict["key"] = value #How to update a dictionary
    oldscore = game_dict[team]
    newscore = int(oldscore) + points
    game_dict[team] = newscore
    return game_dict




"""
print(type(teams)) #str
    print(teams) #"Appleby Arrows vs Montrose Magpies"
    print(type(actions)) #str
    print(actions) #"Team: Quaffle goal, Team: Type Foul, ... , Team: Caught Snitch"
"""
