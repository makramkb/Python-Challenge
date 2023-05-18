import csv

    
    # Declaring variables
    
    
month=[]
pl=[]
total_pl=0
total_pl_diff=0
pldiff=[]


    # Open file as a csv and read it with the csv.reader fct and skip the 1st row which is the header
    

with open('data_budget.csv','r') as csvfile:
    csvreader=csv.reader(csvfile)
    header=next(csvfile)
    
    
    # tansform data into lists
    
    
    for rows in csvreader:
        month.append(rows[0])
        pl.append(rows[1])
        
        
    #calcualate the total p/l diff of btw 2 consecutive dates for the entire  period
    
        
    for i in range(len(pl)):
        total_pl=total_pl+int(pl[i])
    for i in range(len(pl)-1):
        pl_diff=int(pl[i+1])-int(pl[i])
        total_pl_diff=total_pl_diff+pl_diff
        
    # transform the data into a list
    
    
        pldiff.append(pl_diff)
        
    # skip 1 row, by adding zero for the first date row
    
    
    pldiff.insert(0,0)
    
    
    # Get max , min diff and the nb of months
    

max_pldiff=max(pldiff)
min_pldiff=min(pldiff) 
nb_of_month=len(month)

    # Get the avg for the p/l price diff
    
    
avg_pl_diff=total_pl_diff/(len(pl)-1)

    
    # Get the index for the min and max and then get its date associated values
    
    
max_date=str(month[pldiff.index(max(pldiff))])
min_date=str(month[pldiff.index(min(pldiff))])
    


    # print all results
    
    
print('The total months number is=',nb_of_month)
print('Total PL=',total_pl)
print('Change avergage=',avg_pl_diff)
print('The greatest increase=',max_pldiff)
print('The greatest increase=',min_pldiff)
print(f"Greatest Increase in Profits: {max_date} (${max_pldiff})")
print(f"Greatest Decrease in Profits: {min_date} (${min_pldiff})")
