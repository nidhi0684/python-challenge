import csv
import os
import inspect

rows = []
totalVotes = 0
votingDict = {}

# Fetch the directory path where this python script is located. It will avoid FileNotFoundError 
# when the script is run from any directory on terminal.
script_directory = os.path.dirname(os.path.abspath(
  inspect.getfile(inspect.currentframe())))

# Read input csv file
csvpath = os.path.join(script_directory, "Resources", "election_data.csv")
with open(csvpath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    # Loop through all the csv data to get total number of votes for each candidate 
    # and their names
    for row in csvreader:
        rows.append(row)
        candidateName = row.__getitem__(2)
        if not (votingDict.__contains__(candidateName)):
            votingDict[candidateName] = 1
        else:
            votingDict[candidateName] = votingDict.get(candidateName) + 1

# Calculate Total Votes
totalVotes = len(rows)

# Print results on the console/terminal
print("Election Results\n")
print("----------------------------\n")
print(f"Total Votes: {totalVotes}\n")
print("----------------------------\n")

# Print and write on the output text file the percentage of votes each candidate won, 
# total number of votes for each candidate and winner candidate name
winnerName = ''
voteCount = 0

# Set the output file path
outputPath = os.path.join(script_directory, "analysis", "output.txt")

with open(outputPath, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n\n")
    file.write("Total Votes: " + str(totalVotes) + "\n\n")
    file.write("----------------------------\n\n")

    for name, vote in votingDict.items():
        percentage = str(round((vote/totalVotes)*100,3))
        print(f"{name}: {percentage}% ({vote}) \n")
        file.write(f"{name}: {percentage}% ({vote}) \n\n")
        if vote > voteCount:
            winnerName = name
            voteCount = vote
    print("----------------------------\n")
    file.write("----------------------------\n\n")
    print("Winner: %s" % winnerName)
    file.write("Winner: %s" % winnerName)
    print("\n----------------------------\n")
    file.write("\n\n----------------------------\n")
    file.close()


