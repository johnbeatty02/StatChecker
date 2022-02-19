# Receives a set of teams, displays past tournament stats
# Points must be updated with updateStats before using this

import pandas as pd
from itertools import chain

updateStats = False
if updateStats == True:
    from allSheets import *
    reloadAll()

#imports premade teams
df2 = pd.read_csv('tryTeams.csv')
df2.columns = ['t1', 't2', 't3', 't4']
team1 = list(df2.t1)
team2 = list(df2.t2)
team3 = list(df2.t3)
team4 = list(df2.t4)

# puts all teams into one list
allTeams = [team1, team2, team3, team4]
playing = list(chain(*allTeams))


# imports all past game data
bedwars = pd.read_csv('bedwars.csv')
bedwars.columns = ['Players', 'Points']
players = list(bedwars.Players)
points = list(bedwars.Points)
bedwarsPoints = list(zip(players, points))

bridgeDuels = pd.read_csv('bridgeDuels.csv')
bridgeDuels.columns = ['Players', 'Points']
players = list(bridgeDuels.Players)
points = list(bridgeDuels.Points)
bridgeDuelsPoints = list(zip(players, points))

buildBattle = pd.read_csv('buildBattle.csv')
buildBattle.columns = ['Players', 'Points']
players = list(buildBattle.Players)
points = list(buildBattle.Points)
buildBattlePoints = list(zip(players, points))

miniWalls = pd.read_csv('miniWalls.csv')
miniWalls.columns = ['Players', 'Points']
players = list(miniWalls.Players)
points = list(miniWalls.Points)
miniWallsPoints = list(zip(players, points))

parkourDuels = pd.read_csv('parkourDuels.csv')
parkourDuels.columns = ['Players', 'Points']
players = list(parkourDuels.Players)
points = list(parkourDuels.Points)
parkourDuelsPoints = list(zip(players, points))

partyGames = pd.read_csv('partyGames.csv')
partyGames.columns = ['Players', 'Points']
players = list(partyGames.Players)
points = list(partyGames.Points)
partyGamesPoints = list(zip(players, points))

skywars = pd.read_csv('skywars.csv')
skywars.columns = ['Players', 'Points']
players = list(skywars.Players)
points = list(skywars.Points)
skywarsPoints = list(zip(players, points))

survivalGames = pd.read_csv('survivalGames.csv')
survivalGames.columns = ['Players', 'Points']
players = list(survivalGames.Players)
points = list(survivalGames.Points)
survivalGamesPoints = list(zip(players, points))

uhcDuels = pd.read_csv('uhcDuels.csv')
uhcDuels.columns = ['Players', 'Points']
players = list(uhcDuels.Players)
points = list(uhcDuels.Points)
uhcDuelsPoints = list(zip(players, points))

wobtafitv = pd.read_csv('wobtafitv.csv')
wobtafitv.columns = ['Players', 'Points']
players = list(wobtafitv.Players)
points = list(wobtafitv.Points)
wobtafitvPoints = list(zip(players, points))



# removes players who are not playing in a given week
bedwarsPoints = [i for i in bedwarsPoints if i[0] in playing]
bridgeDuelsPoints = [i for i in bridgeDuelsPoints if i[0] in playing]
buildBattlePoints = [i for i in buildBattlePoints if i[0] in playing]
miniWallsPoints = [i for i in miniWallsPoints if i[0] in playing]
parkourDuelsPoints = [i for i in parkourDuelsPoints if i[0] in playing]
partyGamesPoints = [i for i in partyGamesPoints if i[0] in playing]
skywarsPoints = [i for i in skywarsPoints if i[0] in playing]
survivalGamesPoints = [i for i in survivalGamesPoints if i[0] in playing]
uhcDuelsPoints = [i for i in uhcDuelsPoints if i[0] in playing]
wobtafitvPoints = [i for i in wobtafitvPoints if i[0] in playing]

# creates dictionaries for every game
bedwarsD = dict(bedwarsPoints)
bridgeDuelsD = dict(bridgeDuelsPoints)
buildBattleD = dict(buildBattlePoints)
miniWallsD = dict(miniWallsPoints)
parkourDuelsD = dict(parkourDuelsPoints)
partyGamesD = dict(partyGamesPoints)
skywarsD = dict(skywarsPoints)
survivalGamesD = dict(survivalGamesPoints)
uhcDuelsD = dict(uhcDuelsPoints)
wobtafitvD = dict(wobtafitvPoints)


# Creates empty arrays for team points for every possible game
t1bedwars = []
t2bedwars = []
t3bedwars = []
t4bedwars = []
t1bridgeDuels = []
t2bridgeDuels = []
t3bridgeDuels = []
t4bridgeDuels = []
t1buildBattle = []
t2buildBattle = []
t3buildBattle = []
t4buildBattle = []
t1miniWalls = []
t2miniWalls = []
t3miniWalls = []
t4miniWalls = []
t1parkourDuels = []
t2parkourDuels = []
t3parkourDuels = []
t4parkourDuels = []
t1partyGames = []
t2partyGames = []
t3partyGames = []
t4partyGames = []
t1skywars = []
t2skywars = []
t3skywars = []
t4skywars = []
t1survivalGames = []
t2survivalGames = []
t3survivalGames = []
t4survivalGames = []
t1uhcDuels = []
t2uhcDuels = []
t3uhcDuels = []
t4uhcDuels = []
t1wobtafitv = []
t2wobtafitv = []
t3wobtafitv = []
t4wobtafitv = []


# Matches player point values with their corrresponding team
for i in team1:
    pt = bedwarsD.get(i)
    t1bedwars.append(pt)
    pt = bridgeDuelsD.get(i)
    t1bridgeDuels.append(pt)
    pt = buildBattleD.get(i)
    t1buildBattle.append(pt)
    pt = miniWallsD.get(i)
    t1miniWalls.append(pt)
    pt = parkourDuelsD.get(i)
    t1parkourDuels.append(pt)
    pt = partyGamesD.get(i)
    t1partyGames.append(pt)
    pt = skywarsD.get(i)
    t1skywars.append(pt)
    pt = survivalGamesD.get(i)
    t1survivalGames.append(pt)
    pt = uhcDuelsD.get(i)
    t1uhcDuels.append(pt)
    pt = wobtafitvD.get(i)
    t1wobtafitv.append(pt)
for i in team2:
    pt = bedwarsD.get(i)
    t2bedwars.append(pt)
    pt = bridgeDuelsD.get(i)
    t2bridgeDuels.append(pt)
    pt = buildBattleD.get(i)
    t2buildBattle.append(pt)
    pt = miniWallsD.get(i)
    t2miniWalls.append(pt)
    pt = parkourDuelsD.get(i)
    t2parkourDuels.append(pt)
    pt = partyGamesD.get(i)
    t2partyGames.append(pt)
    pt = skywarsD.get(i)
    t2skywars.append(pt)
    pt = survivalGamesD.get(i)
    t2survivalGames.append(pt)
    pt = uhcDuelsD.get(i)
    t2uhcDuels.append(pt)
    pt = wobtafitvD.get(i)
    t2wobtafitv.append(pt)
for i in team3:
    pt = bedwarsD.get(i)
    t3bedwars.append(pt)
    pt = bridgeDuelsD.get(i)
    t3bridgeDuels.append(pt)
    pt = buildBattleD.get(i)
    t3buildBattle.append(pt)
    pt = miniWallsD.get(i)
    t3miniWalls.append(pt)
    pt = parkourDuelsD.get(i)
    t3parkourDuels.append(pt)
    pt = partyGamesD.get(i)
    t3partyGames.append(pt)
    pt = skywarsD.get(i)
    t3skywars.append(pt)
    pt = survivalGamesD.get(i)
    t3survivalGames.append(pt)
    pt = uhcDuelsD.get(i)
    t3uhcDuels.append(pt)
    pt = wobtafitvD.get(i)
    t3wobtafitv.append(pt)
for i in team4:
    pt = bedwarsD.get(i)
    t4bedwars.append(pt)
    pt = bridgeDuelsD.get(i)
    t4bridgeDuels.append(pt)
    pt = buildBattleD.get(i)
    t4buildBattle.append(pt)
    pt = miniWallsD.get(i)
    t4miniWalls.append(pt)
    pt = parkourDuelsD.get(i)
    t4parkourDuels.append(pt)
    pt = partyGamesD.get(i)
    t4partyGames.append(pt)
    pt = skywarsD.get(i)
    t4skywars.append(pt)
    pt = survivalGamesD.get(i)
    t4survivalGames.append(pt)
    pt = uhcDuelsD.get(i)
    t4uhcDuels.append(pt)
    pt = wobtafitvD.get(i)
    t4wobtafitv.append(pt)

# Combines averages

bedwarsAverages = [('Team 1', round(sum(t1bedwars)/4, 2)), ('Team 2', round(sum(t2bedwars)/4, 2)), ('Team 3', round(sum(t3bedwars)/4, 2)), ('Team 4', round(sum(t4bedwars)/4, 2))]
bridgeDuelsAverages = [('Team 1', round(sum(t1bridgeDuels)/4, 2)), ('Team 2', round(sum(t2bridgeDuels)/4, 2)), ('Team 3', round(sum(t3bridgeDuels)/4, 2)), ('Team 4', round(sum(t4bridgeDuels)/4, 2))]
buildBattleAverages = [('Team 1', round(sum(t1buildBattle)/4, 2)), ('Team 2', round(sum(t2buildBattle)/4, 2)), ('Team 3', round(sum(t3buildBattle)/4, 2)), ('Team 4', round(sum(t4buildBattle)/4, 2))]
miniWallsAverages = [('Team 1', round(sum(t1miniWalls)/4, 2)), ('Team 2', round(sum(t2miniWalls)/4, 2)), ('Team 3', round(sum(t3miniWalls)/4, 2)), ('Team 4', round(sum(t4miniWalls)/4, 2))]
parkourDuelsAverages = [('Team 1', round(sum(t1parkourDuels)/4, 2)), ('Team 2', round(sum(t2parkourDuels)/4, 2)), ('Team 3', round(sum(t3parkourDuels)/4, 2)), ('Team 4', round(sum(t4parkourDuels)/4, 2))]
partyGamesAverages = [('Team 1', round(sum(t1partyGames)/4, 2)), ('Team 2', round(sum(t2partyGames)/4, 2)), ('Team 3', round(sum(t3partyGames)/4, 2)), ('Team 4', round(sum(t4partyGames)/4, 2))]
skywarsAverages = [('Team 1', round(sum(t1skywars)/4, 2)), ('Team 2', round(sum(t2skywars)/4, 2)), ('Team 3', round(sum(t3skywars)/4, 2)), ('Team 4', round(sum(t4skywars)/4, 2))]
survivalGamesAverages = [('Team 1', round(sum(t1survivalGames)/4, 2)), ('Team 2', round(sum(t2survivalGames)/4, 2)), ('Team 3', round(sum(t3survivalGames)/4, 2)), ('Team 4', round(sum(t4survivalGames)/4, 2))]
uhcDuelsAverages = [('Team 1', round(sum(t1uhcDuels)/4, 2)), ('Team 2', round(sum(t2uhcDuels)/4, 2)), ('Team 3', round(sum(t3uhcDuels)/4, 2)), ('Team 4', round(sum(t4uhcDuels)/4, 2))]
wobtafitvAverages = [('Team 1', round(sum(t1wobtafitv)/4, 2)), ('Team 2', round(sum(t2wobtafitv)/4, 2)), ('Team 3', round(sum(t3wobtafitv)/4, 2)), ('Team 4', round(sum(t4wobtafitv)/4, 2))]

print('Bedwars:', bedwarsAverages)
print('Bridge Duels:',bridgeDuelsAverages)
print('Build Battle:',buildBattleAverages)
print('Mini Walls:',miniWallsAverages)
print('Parkour Duels:',parkourDuelsAverages)
print('Party Games:',partyGamesAverages)
print('Skywars:',skywarsAverages)
print('Survival Games:',survivalGamesAverages)
print('UHC Duels:',uhcDuelsAverages)
print('WOBTAFITV:',wobtafitvAverages)