#Module 3 Python Challenge Homework'

#PyBank 

#import libraries that are needed
import statistics
import os
import csv

#Pull data from the Budget Data Excel Sheet
budgetData= os.path.join("Resources", "budget_data.csv")

#Setting up variables and Lists 
numMonths = 0
profit = 0
changeList = []
monToMonChange = []
monToMonChange1 = []
monthsList = []
maxChange = 0
bestMonth = ''
minChange = 0
worstMonth = ''
    
with open(budgetData, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    #The total number of months included in the dataset (Total Months: 86)
    #The net total amount of "Profit/Losses" over the entire period (Total: $22564198)
    for row in csvreader:
        numMonths += 1
        monthsList.append(row[0])
        profit += int(row[1])
        
        #The changes in "Profit/Losses" over the entire period
        #The greatest increase in profits (date and amount) over the entire period (Greatest Increase in Profits: Aug-16 ($1862002))
        #The greatest decrease in profits (date and amount) over the entire period (Greatest Decrease in Profits: Feb-14 ($-1825558))
        if int(row[1]) > maxChange:
            bestMonth = (row[0])
            maxChange = int(row[1])
        elif int(row[1]) < minChange:
            worstMonth = (row[0])
            minChange = int(row[1])
        changeList.append(int(row[1]))
    
    for i in range(len(changeList)-1):
        monthlyChange = (changeList[i] - changeList[i-1])
        monToMonChange.append(monthlyChange)
        minChange = min(monToMonChange)
        maxChange = max(monToMonChange)
        minChangeDate = monthsList[monToMonChange.index(minChange)]
        maxChangeDate = monthsList[monToMonChange.index(maxChange)]
      
    for i in range(len(changeList)-1):
        monthlyChange1 = (changeList[i+1] - changeList[i])
        monToMonChange1.append(monthlyChange1)
    avgChange = round(statistics.mean(monToMonChange1), 3)
 

#print results 
print("Financial Analysis")
print("-----------------------------")
print(f'Total Months: {numMonths}')  
print(f'Total: ${profit}')    
print(f'Average Change: ${avgChange}')
print(f'Greatest Increase in Profits: {maxChangeDate} with ${maxChange}')
print(f'Greatest Decrease in Profits: {minChangeDate} with ${minChange}')
    

#write results in a new text file
f = open('results.txt','w')

f.write("Financial Analysis\n")
f.write("-----------------------------\n")
f.write(f'Total Months: {numMonths}\n')
f.write(f'Total: ${profit}\n')
f.write(f'Average Change: ${avgChange}\n')
f.write(f'Greatest Increase in Profits: ${maxChange}\n')
f.write(f'Greatest Decrease in Profits: ${minChange}\n')