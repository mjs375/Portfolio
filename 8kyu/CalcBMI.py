"""
Write function bmi that calculates body mass index (bmi = weight / height2).
  if bmi <= 18.5 return "Underweight"
  if bmi <= 25.0 return "Normal"
  if bmi <= 30.0 return "Overweight"
  if bmi > 30 return "Obese"
The exercise is about Body-Mass Index, but as data scientists, the context of the problem is [usually] inconsequential to us. Really, the problem is about matching to some threshold/below, and outputting a label.
"""

def bmi(weight, height):
    bmi = (weight / height**2)
    if bmi <= 18.5: return "Underweight"
    elif bmi <= 25.0: return "Normal"
    elif bmi <= 30.0: return "Overweight"
    else: return "Obese"
    
# # # # # # # # # # # # # # # # # # # #
    
def bmi2(weight, height): 
    bmi = (weight / height**2)
    # DICT of bmi/term:
    bmis = {
        # "18.5": "Underweight", # BUG!: str/float error
        18.5: "Underweight",
        25.0: "Normal",
        30.0: "Overweight",
        # Why not   30.0[000]1: "Obese",   ?
    }
    # why write out if statements for every level?...
    for level, term in bmis.items():
        if bmi <= level:
            return term
    return "Obese" # ELSE (if none above matched) return "Obese", the upper-bound...
