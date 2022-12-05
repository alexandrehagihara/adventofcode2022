import os
f = open(f"{os.path.dirname(__file__)}/input02.txt", "r")

# Dicionário de pontuações de acordo com o que entendemos das regras. A regra mudou.
scores = {}
# A: Rock (1pt)
# B: Paper (2pt)
# C: Scissors (3pt)
# X: Lose
# Y: Draw
# Z: Win
# Win: 6pt / Draw: 3pt / Lose: 0pt 
scores["A X"] = 3+0 # Rock vs Scissors: Lose
scores["A Y"] = 1+3 # Rock vs Rock: Draw
scores["A Z"] = 2+6 # Rock vs Paper: Win
scores["B X"] = 1+0 # Paper vs Rock: Lose
scores["B Y"] = 2+3 # Paper vs Paper: Draw
scores["B Z"] = 3+6 # Paper vs Scissors: Win
scores["C X"] = 2+0 # Scissors vs Paper: Lose
scores["C Y"] = 3+3 # Scissors vs Scissors: Draw
scores["C Z"] = 1+6 # Scissors vs Rock: Win

total_score = 0
for line in f.readlines():
    line = line.replace("\n", "")
    total_score += scores[line]

print(f"{total_score}")