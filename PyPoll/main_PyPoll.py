#PyPoll Python Challenge

#import libraries that are needed
import os
import csv

#Pull data from the Election Data Excel Sheet
electionData= os.path.join("Resources", "election_data.csv")

#Set the Total Values to start at 0
totalVotes = 0

#Create empy list and Dictionary to hold the list of unique candidates and number of votes for each
candidateList = []
candidateVotes ={}

#setting the variables for the winner
winner = ""
winnerCount = 0
  
#pulling data from the election_data.csv file  
with open(electionData, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    #The total number of votes cast (Total Votes: 369711) & creating the unique candidate list
    for row in csvreader:
        totalVotes += 1
        candidate = row[2]
        
        if candidate not in candidateList:
            candidateList.append(candidate)
            candidateVotes[candidate] = 0
        candidateVotes[candidate] += 1

#printed results
    print("Election Results")  
    print("-----------------------")
    print(f"Total Votes: {totalVotes}")
    
#write results in a new text file
    f = open('results.txt','w')
    
    f.write("Election Results\n")
    f.write("-----------------------------\n")
    f.write(f"Total Votes: {totalVotes}\n")

    #A complete list of candidates who received votes 
    #The percentage of votes each candidate won    
    #The total number of votes each candidate won
            #(Charles Casper Stockham: 23.049% (85213)
            #Diana DeGette: 73.812% (272892)
            #Raymon Anthony Doane: 3.139% (11606))
    for candidate in candidateVotes:
        votes = candidateVotes[candidate]
        votePercentage = round((votes / totalVotes)*100, 3)
        print(f"{candidate}: {votePercentage:}% ({votes:,})")
        f.write(f"{candidate}: {votePercentage:}% ({votes:,})\n")
        
        #The winner of the election based on popular vote (Winner: Diana DeGette)
        if (votes > winnerCount):
            winnerCount = votes
            winner = candidate
  
#printed results of the winner        
print("-----------------------")
print(f'Winner: {winner}')

#write results of the winner in a new text file
f.write("-----------------------------\n")
f.write(f'Winner: {winner}')    


    
    
    