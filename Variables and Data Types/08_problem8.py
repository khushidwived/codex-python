""" 
Ask number of games played in a tournament. Ask the user number of games won and number of games loss.
Calculate number of tie and total points. (1 win= 4 points, 1 tie =2 points)
"""

# Ask user for inputs
total_games = int(input("Enter total number of games played: "))
games_won = int(input("Enter number of games won: "))
games_lost = int(input("Enter number of games lost: "))

# Calculate number of ties
games_tied = total_games - (games_won + games_lost)

# Calculate total points
# 1 win = 4 points, 1 tie = 2 points
total_points = (games_won * 4) + (games_tied * 2)

print("\nTournament Summary")
print("Total Games Played:", total_games)
print("Games Won:", games_won)
print("Games Lost:", games_lost)
print("Games Tied:", games_tied)
print("Total Points:", total_points)