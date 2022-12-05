import os
f = open(f"{os.path.dirname(__file__)}/input02.txt", "r")

# Dicionário de pontuações de acordo com o que entendemos das regras
scores = {}
# A/X (1pt): Rock
# B/Y (2pt): Paper
# C/Z (3pt): Scissors
# Win: 6pt / Draw: 3pt / Lose: 0pt 
scores["A X"] = 1+3 # Rock vs Rock: Draw
scores["A Y"] = 2+6 # Rock vs Paper: Win
scores["A Z"] = 3+0 # Rock vs Scissors: Lose
scores["B X"] = 1+0 # Paper vs Rock: Lose
scores["B Y"] = 2+3 # Paper vs Paper: Draw
scores["B Z"] = 3+6 # Paper vs Scissors: Win
scores["C X"] = 1+6 # Scissors vs Rock: Win
scores["C Y"] = 2+0 # Scissors vs Paper: Lose
scores["C Z"] = 3+3 # Scissors vs Scissors: Draw

total_score = 0
for line in f.readlines():
    line = line.replace("\n", "")
    total_score += scores[line]

print(f"{total_score}")