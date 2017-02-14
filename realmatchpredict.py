import pandas as pd
import numpy as np


match_details = pd.read_csv(
    "1617velv-FULL-MatchResultsRaw.csv", delimiter=",")
# convert match_details to numpyarray
match_details = np.array(match_details)
X_teamid = match_details[:, 4:9]


def simulate():
    def create_team(teamnum_tofind):
        searcher = np.where(X_teamid == teamnum_tofind)
        searcher = np.array(searcher)
        searchershape = searcher.shape
        number_of_matches = searchershape[1]
        match_colors = searcher[1]
        matchid = searcher[0]

        beaconspressedauto = np.zeros(number_of_matches)
        beaconspressedtele = np.zeros(number_of_matches)
        ballsscoredcentervortexauto = np.zeros(number_of_matches)
        ballsscoredcornervortexauto = np.zeros(number_of_matches)
        ballsscoredcentervortextele = np.zeros(number_of_matches)
        ballsscoredcornervortextele = np.zeros(number_of_matches)
        capballlevel = np.zeros(number_of_matches)

        i = 0
        # teamcolor = "null"
        while i < number_of_matches:
            if match_colors[i] <= 2:
                # teamcolor = "red"
                beaconspressedauto[i] = (match_details[matchid[i], 29])
                beaconspressedtele[i] = (match_details[matchid[i], 35])
                ballsscoredcentervortexauto[i] = (
                    match_details[matchid[i], 31])
                ballsscoredcornervortexauto[i] = (
                    match_details[matchid[i], 32])
                ballsscoredcentervortextele[i] = (
                    match_details[matchid[i], 36])
                ballsscoredcornervortextele[i] = (
                    match_details[matchid[i], 37])
                capballlevel[i] = (match_details[matchid[i], 38])
            else:
                # teamcolor = "blue"
                beaconspressedauto[i] = (match_details[matchid[i], 43])
                beaconspressedtele[i] = (match_details[matchid[i], 49])
                ballsscoredcentervortexauto[i] = (
                    match_details[matchid[i], 45])
                ballsscoredcornervortexauto[i] = (
                    match_details[matchid[i], 46])
                ballsscoredcentervortextele[i] = (
                    match_details[matchid[i], 50])
                ballsscoredcornervortextele[i] = (
                    match_details[matchid[i], 51])
                capballlevel[i] = (match_details[matchid[i], 52])
            i = i + 1
        average_balls_scored_by_team_tele = np.average(
            ballsscoredcentervortextele)
        average_balls_scored_by_team_auto = np.average(
            ballsscoredcentervortexauto)
        average_beacons_scored_by_team_auto = np.average(beaconspressedauto)
        average_beacons_scored_by_team_tele = np.average(beaconspressedtele)
        average_capball_level_by_team = np.average(capballlevel)

        team_individual_strengthvec = np.array([average_balls_scored_by_team_tele,
                                                average_balls_scored_by_team_auto,
                                                average_beacons_scored_by_team_tele,
                                                average_beacons_scored_by_team_auto,
                                                average_capball_level_by_team
                                                ])
        team_individual_strengthvec[0] = (
            team_individual_strengthvec[0]) * (0.5) * (5)
        team_individual_strengthvec[1] = (
            team_individual_strengthvec[1]) * (0.5) * (15)
        team_individual_strengthvec[2] = (
            team_individual_strengthvec[2]) * (0.5) * (10)
        team_individual_strengthvec[3] = (
            team_individual_strengthvec[3]) * (0.5) * (30)
        team_individual_strengthvec[4] = (
            team_individual_strengthvec[4]) * (0.5) * (10)
        team_projected_points = np.sum(team_individual_strengthvec)
        return team_projected_points

    strengthvec_details = np.array(["average_balls_scored_by_team_tele",
                                    "average_balls_scored_by_team_auto",
                                    "average_beacons_scored_by_team_tele",
                                    "average_beacons_scored_by_team_auto",
                                    "average_capball_level_by_team"
                                    ])
    count = 0
    while count < 4:
        if count == 0:
            teamnum_tofind_string = input("blue team number one: ")
            teamnum_tofind = int(teamnum_tofind_string)
        elif count == 1:
            teamnum_tofind_string = input("blue team number two: ")
            teamnum_tofind = int(teamnum_tofind_string)
        elif count == 2:
            teamnum_tofind_string = input("red team number one: ")
            teamnum_tofind = int(teamnum_tofind_string)
        else:
            teamnum_tofind_string = input("red team number two: ")
            teamnum_tofind = int(teamnum_tofind_string)
        if count == 0:
            team_one = create_team(teamnum_tofind)
        elif count == 1:
            team_two = create_team(teamnum_tofind)
        elif count == 2:
            team_three = create_team(teamnum_tofind)
        else:
            team_four = create_team(teamnum_tofind)
        count = count + 1
    print("team one power: ", team_one)
    print("team two power: ", team_two)
    print("team three power: ", team_three)
    print("team four power: ", team_four)
    blue_score = team_one + team_two
    red_score = team_three + team_four
    blue_chance = ((blue_score) / (blue_score + red_score)) * 100
    red_chance = ((red_score) / (blue_score + red_score)) * 100
    print ("blue alliance power: ", blue_score,
           " red alliance power: ", red_score)
    print ("blue win chance: ", blue_chance, "%")
    print ("red win chance: ", red_chance, "%")
    return (blue_chance, red_chance)


print(simulate())
# find total averages of all matches
balls_scored_center_teleop = match_details[:, 36]
balls_scored_center_auto = match_details[:, 31]
sumofballscentertele = np.sum(balls_scored_center_teleop, dtype=float)
sumofballscenterauto = np.sum(balls_scored_center_auto, dtype=float)
numberofdatas = match_details.shape
average_balls_scored_center_teleop = (
    sumofballscentertele) / (numberofdatas[0])
average_balls_scored_center_auto = (sumofballscenterauto) / (numberofdatas[0])
