import pandas as pd
import numpy as np

team_stats = pd.read_csv("1617velv-FULL-StatsDet.csv", delimiter=",")

team_id = np.array(team_stats[[1]])
team_opr = np.array(team_stats[[10]])

# I called the array with id vs opr test but I wont change it cuz I am lazy

test = np.hstack((team_id, team_opr))
teamnum_tofind_string = input("team number: ")
teamnum_tofind = int(teamnum_tofind_string)

team_num_searcher = np.where(test[:, 0] == teamnum_tofind)
the_id_found = team_num_searcher[0]

the_opr_found_array = test[the_id_found, 1]
the_opr_found = the_opr_found_array[0]

print("the OPR of this team is: ", the_opr_found)
