"""
@author : Nishant Sanjay Kumbhar
@goal : To implement the matches between teams.
"""
teams = ["Mumbai Indians", "Chennai Super Kings", "Pune Warriors India", "Royal Challengers Bangalore", "Rajasthan Royals", "Kolkata Knight Rider", "Kings XI Punjab"]

for left_teams in teams:
    for right_teams in teams:
        if left_teams != right_teams:
            print(f"{left_teams} vs {right_teams}")
