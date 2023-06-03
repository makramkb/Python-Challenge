import csv


    # Declare variables
    
    
total=0
count=0
ballot_id=[]
county=[]
candidate=[]
candidate_1='Charles Casper Stockham'
candidate_2='Diana DeGette'
candidate_3='Raymon Anthony Doane'
candidate_rcvd_votes=[]
votes_rcvd_by_candidate=[0,0,0]

    
    # Open file as a csv and read it with the csv.reader fct and skip the 1st row which is the header
    

with open('election_data.csv','r') as file:
    csvreader=csv.reader(file)
    header=next(file)
    
    
    # transformed data into list    
    
    
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
    
    # Get the total votes
    
    
    Total_Votes=len(candidate)
    
    
    #  Get the candidate list 
    
    
    for i in candidate:
        if i not in candidate_rcvd_votes:
            candidate_rcvd_votes.append(i)
            
    
    # Count the votes for each candidate
    
        
        if i==candidate_1:
            votes_rcvd_by_candidate[0]=votes_rcvd_by_candidate[0]+1
        if i==candidate_2:
            votes_rcvd_by_candidate[1]=votes_rcvd_by_candidate[1]+1
        if i==candidate_3:
            votes_rcvd_by_candidate[2]=votes_rcvd_by_candidate[2]+1

    
    # Get the percentage of votes for each candidate
    
    
    for i in range(len(candidate_rcvd_votes)):
        print(f'{candidate_rcvd_votes[i]} received {round((int(votes_rcvd_by_candidate[i])/Total_Votes)*100,2)} %')
    
    
    # Get the winner
    
    winner_candidate=max(votes_rcvd_by_candidate)
    winner=candidate_rcvd_votes[votes_rcvd_by_candidate.index(winner_candidate)]
    
    
    
    # Print the results
print('The winner is : ',winner)  
    
print('Total votes : ',Total_Votes)     
print('Candidates list : ',candidate_rcvd_votes)           
print('Total votes for each candidate : ',votes_rcvd_by_candidate)



print('Total votes : ', Total_Votes)
print('Candidates list : ', candidate_rcvd_votes)
print('Total votes for each candidate : ', votes_rcvd_by_candidate)
print('The winner is :', winner_candidate)
