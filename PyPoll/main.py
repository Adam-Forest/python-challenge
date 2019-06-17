# PyPoll
# program to analyze voter data

# import path setting, and csv helping
import os
import csv

# path to data

# set path for input file
# data directory is to levels below program location
election_data_csv = os.path.join("..", "..", "Data", "election_data.csv")

# set path for output file
outfile = os.path.join("..", "..", "Data", "Election_Summary.txt")

# store total votes here
total_votes=0
results={}
with open(election_data_csv, 'r') as csvfile:
    # split the data
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the headers
    next(csvreader)

    # loop through the data
    for row in csvreader:

        # grab candidate name into variable
        candidate=str(row[2])

        # make dictionary from candidate name, value = votes
        if candidate in results:
            results[candidate] = results[candidate]+1   
        else:
            results[candidate] = 1

winner = max(results, key=results.get)

# print to terminal
print("Election Results")
print("________________________________________________")
print("Total Votes: " + str(sum(results.values() )))
print("________________________________________________")

for key in results:
    print (key + ": " + str(  round( (results[key]/sum(results.values() ))*100 , 3 )  ) + "% (" + str(results[key]) + ")")

print("________________________________________________")
print(f"Winner: {winner}")
print("________________________________________________")