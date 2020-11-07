def my_languages(results):
    scores = [] # Get list of passing scores
    for key, value in results.items():
        if value >= 60:
            scores.append(value)
    scores.sort(reverse=True) # Sort the scores High>>>Low
    langs = []
    for score in scores:
        for k, v in results.items():
            if score == v: # Re-match score to lang,
                langs.append(k) # and add lang to list
    return langs

"""
You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the results.
Note: the scores will always be unique (so no duplicate values)
  Examples
    {"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
    {"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
    {"C++": 50, "ASM": 10, "Haskell": 20}     -->  []
"""
