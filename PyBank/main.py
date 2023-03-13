"""
Create a Python script that analyzes the records to calculate each of the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period
Your analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""
# Modules
import os
import csv

# Set path for file
financialData = os.path.join('Resources','budget_data.csv')

# Declare the variables / empty list
totalNumberMonths = []
totalAmt = []
changesProfitLosses = []
totalProfits = 0

# Open CSV
with open(financialData, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the headers
    next(csvreader, None)  
    
    # Loop through the data and compute
    for row in csvreader:
        totalNumberMonths.append(row[0])
        totalAmt.append(row[1])
        totalProfits = totalProfits + int(row[1])
    
    for i in range(1, len(totalAmt)):
        changesProfitLosses.append(int(totalAmt[i])- int(totalAmt[i-1]))  
    
    
# Get the max and min changes; use the max & min function
increaseProfit = max(changesProfitLosses) 
decreaseProfit = min(changesProfitLosses)

# index the max and min by + 1 for the correct month / the next month is related to the change
increaseMonth = changesProfitLosses.index(max(changesProfitLosses)) + 1
decreaseMonth = changesProfitLosses.index(min(changesProfitLosses)) + 1

# Print the analysis to the terminal 
print("Financial Analysis")
print("----------------------------") 
print(f'Total Months: {len(totalNumberMonths)}') 
print(f'Total: ${totalProfits}')
print(f'Average Change: ${round(sum(changesProfitLosses) / len(changesProfitLosses), 2)}')
print(f'Greatest Increase in Profits: {totalNumberMonths[increaseMonth]} (${(str(increaseProfit))})')
print(f'Greatest Decrease in Profits: {totalNumberMonths[decreaseMonth]} (${(str(decreaseProfit))})')
 
  
# Export a text file with the results
# path to the output file
outputFile = os.path.join('analysis','financialAnalysis.txt')

# Export a text file (budget_analysis.txt) with the results
with open(outputFile, 'w') as text:
    text.write('Financial Analysis' + '\n')
    text.write('----------------------------' + '\n') 
    text.write(f'Total Months: {len(totalNumberMonths)}' + '\n') 
    text.write(f'Total: ${totalProfits}' + '\n')
    text.write(f'Average Change: ${round(sum(changesProfitLosses) / len(changesProfitLosses), 2)}' + '\n')
    text.write(f'Greatest Increase in Profits: {totalNumberMonths[increaseMonth]} (${(str(increaseProfit))})' + '\n')
    text.write(f'Greatest Decrease in Profits: {totalNumberMonths[decreaseMonth]} (${(str(decreaseProfit))})' + '\n')

