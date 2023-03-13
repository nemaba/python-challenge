"""
In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

Your analysis should look similar to the following:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""

# Modules
import os
import csv

# Set path for file
electionData = os.path.join('Resources', 'election_data.csv')

# Declare the variables / empty list
# Candidates
candidates = []
votesCount = []
percentageVotes = []
totalVotes = 0


# Open csv
with open(electionData, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # skip the headers
    next(csvreader, None)

    # Loop through the data and compute
    for row in csvreader:
        
        # Compute the total votes
        totalVotes = totalVotes + 1 
        
        #append the candidate's name and the vote to the variable list
        if row[2] not in candidates:
           candidates.append(row[2])
           index = candidates.index(row[2])
           votesCount.append(1)
        else:
            index = candidates.index(row[2]) 
            votesCount[index] = votesCount[index]  + 1  
        
    # percentageVotes
    for vote in votesCount:
        #compute for the percent votes
        percentV = vote / totalVotes
        percentageVotes.append(percentV)

    # Look for the winning candidate
    winner = max(votesCount)
    index = votesCount.index(winner)
    winningCandidate = candidates[index]   

# Print the analysis to the terminal     
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(totalVotes)}")   
print("-------------------------")  
for i in range(len(candidates)):
  print(f"{candidates[i]}: {(percentageVotes[i]):.3%} ({str(votesCount[i])})")
print("-------------------------")  
print(f"Winner: {winningCandidate}")  
print("-------------------------")   
  
# Export a text file with the results
# path to the output file
outputFile = os.path.join('analysis','electionResults.txt')


# Export a text file (election_analysis.txt) with the results
with open(outputFile, 'w') as text:
    text.write("Election Results" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Total Votes: {str(totalVotes)}" + "\n")
    text.write("-------------------------" + "\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: {(percentageVotes[i]):.3%} ({str(votesCount[i])})\n")
    text.write("-------------------------" + "\n")
    text.write(f"Winner: {winningCandidate}" + "\n")
    text.write("-------------------------")



