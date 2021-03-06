# Receives a set of teams, displays past tournament stats
# Points must be updated with updateStats before using this

import pandas as pd
from itertools import chain
from matplotlib import pyplot as plt
import numpy as np

updateStats = False         # Refreshes the stats from the Google Sheet
output = False              # Outputs each team's points in each mode to the console
graphAll = True            # Graphs each team's stats for every gamemode
printDifferentials = True  # Prints the expected point differentials
graphDifferentials = True  # Graphs the expected point differentials
displayGameAverages = False
pvpGames = 6                # Number of PvP games
nonPvPGames = 4             # Number of non-PvP games
colorOrder = ['red', 'gold', 'green', 'blue']

if updateStats:
    from allSheets import *
    reloadAll()

games = ['Bedwars', 'Bridge Duels', 'Build Battle', 'Mini Walls', 'Parkour Duels', 'Party Games', 'Skywars',
             #'Survival Games',
         'UHC Duels', 'WOBTAFITV', 'PvP', 'Non-PvP']
shortGames = ['BW', 'BD', 'BB', 'MW', 'PD', 'PG', 'SW',
              # 'SG',
              'UD', 'WO', "PvP", 'nP']

# imports premade teams
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
overall = pd.read_csv('overall.csv')
overall.columns = ['Players', 'Points']
players = list(overall.Players)
points = list(overall.Points)
overallPoints = list(zip(players, points))

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

pvp = pd.read_csv('pvp.csv')
pvp.columns = ['Players', 'Points']
players = list(pvp.Players)
points = list(pvp.Points)
pvpPoints = list(zip(players, points))

nonPvP = pd.read_csv('nonPvP.csv')
nonPvP.columns = ['Players', 'Points']
players = list(nonPvP.Players)
points = list(nonPvP.Points)
nonPvPPoints = list(zip(players, points))


# removes players who are not playing in a given week
overallPoints = [i for i in overallPoints if i[0] in playing]
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
pvpPoints = [i for i in pvpPoints if i[0] in playing]
nonPvPPoints = [i for i in nonPvPPoints if i[0] in playing]

# Catches inactive players
allPoints = [overallPoints, bedwarsPoints, bridgeDuelsPoints, buildBattlePoints, miniWallsPoints, parkourDuelsPoints, partyGamesPoints, skywarsPoints, survivalGamesPoints, uhcDuelsPoints, wobtafitvPoints, pvpPoints, nonPvPPoints]
for i in allPoints:
    for j in i:
        if None in i:
            raise ValueError(f'Player is not in {i}!')

# creates dictionaries for every game
overallD = dict(overallPoints)
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
pvpD = dict(pvpPoints)
nonPvPD = dict(nonPvPPoints)


# Creates empty arrays for team points for every possible game
t1overall = []
t2overall = []
t3overall = []
t4overall = []
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
t1pvp = []
t2pvp = []
t3pvp = []
t4pvp = []
t1nonPvP = []
t2nonPvP = []
t3nonPvP = []
t4nonPvP = []


# Matches player point values with their corrresponding team
for i in team1:
    pt = overallD.get(i)
    t1overall.append(pt)
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
    pt = pvpD.get(i)
    t1pvp.append(pt)
    pt = nonPvPD.get(i)
    t1nonPvP.append(pt)
for i in team2:
    pt = overallD.get(i)
    t2overall.append(pt)
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
    pt = pvpD.get(i)
    t2pvp.append(pt)
    pt = nonPvPD.get(i)
    t2nonPvP.append(pt)
for i in team3:
    pt = overallD.get(i)
    t3overall.append(pt)
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
    pt = pvpD.get(i)
    t3pvp.append(pt)
    pt = nonPvPD.get(i)
    t3nonPvP.append(pt)
for i in team4:
    pt = overallD.get(i)
    t4overall.append(pt)
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
    pt = pvpD.get(i)
    t4pvp.append(pt)
    pt = nonPvPD.get(i)
    t4nonPvP.append(pt)
# Checks that all player names are valid:


# Calculates game average points for each team
stats = [t1pvp, t2pvp, t3pvp, t4pvp]
print(stats)
overallPointAverages = [round(sum(t1overall)/4, 2), round(sum(t2overall)/4, 2), round(sum(t3overall)/4, 2), round(sum(t4overall)/4, 2)]
bedwarsPointAverages = [round(sum(t1bedwars)/4, 2), round(sum(t2bedwars)/4, 2), round(sum(t3bedwars)/4, 2), round(sum(t4bedwars)/4, 2)]
bridgeDuelsPointAverages = [round(sum(t1bridgeDuels)/4, 2), round(sum(t2bridgeDuels)/4, 2), round(sum(t3bridgeDuels)/4, 2), round(sum(t4bridgeDuels)/4, 2)]
buildBattlePointAverages = [round(sum(t1buildBattle)/4, 2), round(sum(t2buildBattle)/4, 2), round(sum(t3buildBattle)/4, 2), round(sum(t4buildBattle)/4, 2)]
miniWallsPointAverages = [round(sum(t1miniWalls)/4, 2), round(sum(t2miniWalls)/4, 2), round(sum(t3miniWalls)/4, 2), round(sum(t4miniWalls)/4, 2)]
parkourDuelsPointAverages = [round(sum(t1parkourDuels)/4, 2), round(sum(t2parkourDuels)/4, 2), round(sum(t3parkourDuels)/4, 2), round(sum(t4parkourDuels)/4, 2)]
partyGamesPointAverages = [round(sum(t1partyGames)/4, 2), round(sum(t2partyGames)/4, 2), round(sum(t3partyGames)/4, 2), round(sum(t4partyGames)/4, 2)]
skywarsPointAverages = [round(sum(t1skywars)/4, 2), round(sum(t2skywars)/4, 2), round(sum(t3skywars)/4, 2), round(sum(t4skywars)/4, 2)]
# survivalGamesPointAverages = [round(sum(t1survivalGames)/4, 2), round(sum(t2survivalGames)/4, 2), round(sum(t3survivalGames)/4, 2), round(sum(t4survivalGames)/4, 2)]
uhcDuelsPointAverages = [round(sum(t1uhcDuels)/4, 2), round(sum(t2uhcDuels)/4, 2), round(sum(t3uhcDuels)/4, 2), round(sum(t4uhcDuels)/4, 2)]
wobtafitvPointAverages = [round(sum(t1wobtafitv)/4, 2), round(sum(t2wobtafitv)/4, 2), round(sum(t3wobtafitv)/4, 2), round(sum(t4wobtafitv)/4, 2)]
pvpPointAverages = [round(sum(t1pvp)/4, 2), round(sum(t2pvp)/4, 2), round(sum(t3pvp)/4, 2), round(sum(t4pvp)/4, 2)]
nonPvPPointAverages = [round(sum(t1nonPvP)/(4*nonPvPGames), 2), round(sum(t2nonPvP)/(4*nonPvPGames), 2), round(sum(t3nonPvP)/(4*nonPvPGames), 2), round(sum(t4nonPvP)/(4*nonPvPGames), 2)]

# Combines each team's averages by gamemode
overallAverages = [('Team 1', round(sum(t1overall)/4, 2)), ('Team 2', round(sum(t2overall)/4, 2)), ('Team 3', round(sum(t3overall)/4, 2)), ('Team 4', round(sum(t4overall)/4, 2))]
bedwarsAverages = [('Team 1', round(sum(t1bedwars)/4, 2)), ('Team 2', round(sum(t2bedwars)/4, 2)), ('Team 3', round(sum(t3bedwars)/4, 2)), ('Team 4', round(sum(t4bedwars)/4, 2))]
bridgeDuelsAverages = [('Team 1', round(sum(t1bridgeDuels)/4, 2)), ('Team 2', round(sum(t2bridgeDuels)/4, 2)), ('Team 3', round(sum(t3bridgeDuels)/4, 2)), ('Team 4', round(sum(t4bridgeDuels)/4, 2))]
buildBattleAverages = [('Team 1', round(sum(t1buildBattle)/4, 2)), ('Team 2', round(sum(t2buildBattle)/4, 2)), ('Team 3', round(sum(t3buildBattle)/4, 2)), ('Team 4', round(sum(t4buildBattle)/4, 2))]
miniWallsAverages = [('Team 1', round(sum(t1miniWalls)/4, 2)), ('Team 2', round(sum(t2miniWalls)/4, 2)), ('Team 3', round(sum(t3miniWalls)/4, 2)), ('Team 4', round(sum(t4miniWalls)/4, 2))]
parkourDuelsAverages = [('Team 1', round(sum(t1parkourDuels)/4, 2)), ('Team 2', round(sum(t2parkourDuels)/4, 2)), ('Team 3', round(sum(t3parkourDuels)/4, 2)), ('Team 4', round(sum(t4parkourDuels)/4, 2))]
partyGamesAverages = [('Team 1', round(sum(t1partyGames)/4, 2)), ('Team 2', round(sum(t2partyGames)/4, 2)), ('Team 3', round(sum(t3partyGames)/4, 2)), ('Team 4', round(sum(t4partyGames)/4, 2))]
skywarsAverages = [('Team 1', round(sum(t1skywars)/4, 2)), ('Team 2', round(sum(t2skywars)/4, 2)), ('Team 3', round(sum(t3skywars)/4, 2)), ('Team 4', round(sum(t4skywars)/4, 2))]
# survivalGamesAverages = [('Team 1', round(sum(t1survivalGames)/4, 2)), ('Team 2', round(sum(t2survivalGames)/4, 2)), ('Team 3', round(sum(t3survivalGames)/4, 2)), ('Team 4', round(sum(t4survivalGames)/4, 2))]
uhcDuelsAverages = [('Team 1', round(sum(t1uhcDuels)/4, 2)), ('Team 2', round(sum(t2uhcDuels)/4, 2)), ('Team 3', round(sum(t3uhcDuels)/4, 2)), ('Team 4', round(sum(t4uhcDuels)/4, 2))]
wobtafitvAverages = [('Team 1', round(sum(t1wobtafitv)/4, 2)), ('Team 2', round(sum(t2wobtafitv)/4, 2)), ('Team 3', round(sum(t3wobtafitv)/4, 2)), ('Team 4', round(sum(t4wobtafitv)/4, 2))]
pvpAverages = [('Team 1', round(sum(t1pvp)/4, 2)), ('Team 2', round(sum(t2pvp)/4, 2)), ('Team 3', round(sum(t3pvp)/4, 2)), ('Team 4', round(sum(t4pvp)/4, 2))]
nonPvPAverages = [('Team 1', round(sum(t1nonPvP)/(4*nonPvPGames), 2)), ('Team 2', round(sum(t2nonPvP)/(4*nonPvPGames), 2)), ('Team 3', round(sum(t3nonPvP)/(4*nonPvPGames), 2)), ('Team 4', round(sum(t4nonPvP)/(4*nonPvPGames), 2))]

# Prints results
if output:
    print('Overall:', overallAverages)
    print('Bedwars:', bedwarsAverages)
    print('Bridge Duels:', bridgeDuelsAverages)
    print('Build Battle:', buildBattleAverages)
    print('Mini Walls:', miniWallsAverages)
    print('Parkour Duels:', parkourDuelsAverages)
    print('Party Games:', partyGamesAverages)
    print('Skywars:', skywarsAverages)
    #print('Survival Games:', survivalGamesAverages)
    print('UHC Duels:', uhcDuelsAverages)
    print('WOBTAFITV:', wobtafitvAverages)
    print('PvP:', pvpAverages)
    print('Non-PvP:', nonPvPAverages)

# Graphs everything!
if graphAll:
    labels = np.arange(1, 5)
    fig, axs = plt.subplots(4, 3)
    fig.suptitle('Average Points for All Games')
    fig.tight_layout()
    axs[0, 0].bar(labels, bedwarsPointAverages, color=colorOrder)
    axs[0, 0].set_title('Bedwars')
    axs[0, 1].bar(labels, bridgeDuelsPointAverages, color=colorOrder)
    axs[0, 1].set_title('Bridge Duels')
    axs[1, 0].bar(labels, buildBattlePointAverages, color=colorOrder)
    axs[1, 0].set_title('Build Battle')
    axs[1, 1].bar(labels, miniWallsPointAverages, color=colorOrder)
    axs[1, 1].set_title('Mini Walls')
    axs[2, 0].bar(labels, parkourDuelsPointAverages, color=colorOrder)
    axs[2, 0].set_title('Parkour Duels')
    axs[2, 1].bar(labels, partyGamesPointAverages, color=colorOrder)
    axs[2, 1].set_title('Party Games')
    axs[0, 2].bar(labels, skywarsPointAverages, color=colorOrder)
    axs[0, 2].set_title('Skywars')
    #axs[1, 2].bar(labels, survivalGamesPointAverages, color=colorOrder)
    axs[1, 2].set_title('Survival Games')
    axs[2, 2].bar(labels, uhcDuelsPointAverages, color=colorOrder)
    axs[2, 2].set_title('UHC Duels')
    axs[3, 0].bar(labels, wobtafitvPointAverages, color=colorOrder)
    axs[3, 0].set_title('WOBTAFITV')
    axs[3, 1].bar(labels, pvpPointAverages, color=colorOrder)
    axs[3, 1].set_title('PvP')
    axs[3, 2].bar(labels, nonPvPPointAverages, color=colorOrder)
    axs[3, 2].set_title('Non-PvP')

    for ax in axs.flat:  # Maintains spacing, titles get squished without this
        ax.set(xlabel='', ylabel='')
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.show()

# Calculates each team's best and worst games
# Calculates averages for each game
# overallAverage = round(((sum(t1overall)+sum(t2overall)+sum(t3overall)+sum(t4overall))/4), 2)
bedwarsAverage = round(((sum(t1bedwars)+sum(t2bedwars)+sum(t3bedwars)+sum(t4bedwars))/4), 2)
bridgeDuelsAverage = round(((sum(t1bridgeDuels)+sum(t2bridgeDuels)+sum(t3bridgeDuels)+sum(t4bridgeDuels))/4), 2)
buildBattleAverage = round(((sum(t1buildBattle)+sum(t2buildBattle)+sum(t3buildBattle)+sum(t4buildBattle))/4), 2)
miniWallsAverage = round(((sum(t1miniWalls)+sum(t2miniWalls)+sum(t3miniWalls)+sum(t4miniWalls))/4), 2)
parkourDuelsAverage = round(((sum(t1parkourDuels)+sum(t2parkourDuels)+sum(t3parkourDuels)+sum(t4parkourDuels))/4), 2)
partyGamesAverage = round(((sum(t1partyGames)+sum(t2partyGames)+sum(t3partyGames)+sum(t4partyGames))/4), 2)
skywarsAverage = round(((sum(t1skywars)+sum(t2skywars)+sum(t3skywars)+sum(t4skywars))/4), 2)
#survivalGamesAverage = round(((sum(t1survivalGames)+sum(t2survivalGames)+sum(t3survivalGames)+sum(t4survivalGames))/4), 2)
uhcDuelsAverage = round(((sum(t1uhcDuels)+sum(t2uhcDuels)+sum(t3uhcDuels)+sum(t4uhcDuels))/4), 2)
wobtafitvAverage =round(((sum(t1wobtafitv)+sum(t2wobtafitv)+sum(t3wobtafitv)+sum(t4wobtafitv))/4), 2)
pvpAverage =round(((sum(t1pvp)+sum(t2pvp)+sum(t3pvp)+sum(t4pvp))/4), 2)
nonPvPAverage =round(((sum(t1nonPvP)+sum(t2nonPvP)+sum(t3nonPvP)+sum(t4nonPvP))/4), 2)

allAverages = np.round([bedwarsAverage, bridgeDuelsAverage, buildBattleAverage, miniWallsAverage, parkourDuelsAverage, partyGamesAverage, skywarsAverage,
                        # survivalGamesAverage,
                        uhcDuelsAverage, wobtafitvAverage, pvpAverage, nonPvPAverage])

t1Averages = np.round([sum(t1bedwars), sum(t1bridgeDuels), sum(t1buildBattle), sum(t1miniWalls), sum(t1parkourDuels), sum(t1partyGames), sum(t1skywars),
                       # sum(t1survivalGames),
                       sum(t1uhcDuels), sum(t1wobtafitv), sum(t1pvp), sum(t1nonPvP)])
t2Averages = np.round([sum(t2bedwars), sum(t2bridgeDuels), sum(t2buildBattle), sum(t2miniWalls), sum(t2parkourDuels), sum(t2partyGames), sum(t2skywars),
                       # sum(t2survivalGames),
                       sum(t2uhcDuels), sum(t2wobtafitv), sum(t2pvp), sum(t2nonPvP)])
t3Averages = np.round([sum(t3bedwars), sum(t3bridgeDuels), sum(t3buildBattle), sum(t3miniWalls), sum(t3parkourDuels), sum(t3partyGames), sum(t3skywars),
                       #REMOVE sum(t3survivalGames),
                       sum(t3uhcDuels), sum(t3wobtafitv), sum(t3pvp), sum(t3nonPvP)])
t4Averages = np.round([sum(t4bedwars), sum(t4bridgeDuels), sum(t4buildBattle), sum(t4miniWalls), sum(t4parkourDuels), sum(t4partyGames), sum(t4skywars),
                       #REMOVE sum(t4survivalGames),
                       sum(t4uhcDuels), sum(t4wobtafitv), sum(t4pvp), sum(t4nonPvP)])

# Calculates advantages (point differentials)
t1Differentials = [i - j for (i, j) in zip(t1Averages, allAverages)]
t1DifferentialsZipped = list(zip(games, t1Differentials))
t1DifferentialsZipped.sort(key = lambda x: x[1], reverse = True)

t2Differentials = [i - j for (i, j) in zip(t2Averages, allAverages)]
t2DifferentialsZipped = list(zip(games, t2Differentials))
t2DifferentialsZipped.sort(key = lambda x: x[1], reverse = True)

t3Differentials = [i - j for (i, j) in zip(t3Averages, allAverages)]
t3DifferentialsZipped = list(zip(games, t3Differentials))
t3DifferentialsZipped.sort(key = lambda x: x[1], reverse = True)

t4Differentials = [i - j for (i, j) in zip(t4Averages, allAverages)]
t4DifferentialsZipped = list(zip(games, t4Differentials))
t4DifferentialsZipped.sort(key = lambda x: x[1], reverse = True)

# Graphs point differentials
if graphDifferentials:
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Point Differentials for All Teams')
    fig.tight_layout()
    axs[0, 0].bar(shortGames, t1Differentials, color=colorOrder[0])
    axs[0, 0].set_title(colorOrder[0])
    axs[0, 1].bar(shortGames, t2Differentials, color=colorOrder[1])
    axs[0, 1].set_title(colorOrder[1])
    axs[1, 0].bar(shortGames, t3Differentials, color=colorOrder[2])
    axs[1, 0].set_title(colorOrder[2])
    axs[1, 1].bar(shortGames, t4Differentials, color=colorOrder[3])
    axs[1, 1].set_title(colorOrder[3])
    plt.show()
if printDifferentials:
    differentials = [sum(t1Differentials), sum(t2Differentials), sum(t3Differentials), sum(t4Differentials)]
    print(differentials)
t1AbsDiff = sum([abs(i) for i in t1Differentials])
t2AbsDiff = sum([abs(i) for i in t2Differentials])
t3AbsDiff = sum([abs(i) for i in t3Differentials])
t4AbsDiff = sum([abs(i) for i in t4Differentials])
absDiff = [t1AbsDiff, t2AbsDiff, t3AbsDiff, t4AbsDiff]
if displayGameAverages:
    print(allAverages)
    print(np.std(allAverages))
    plt.bar(games, allAverages)
    plt.title('Average Points For Each Game')
    plt.show()
