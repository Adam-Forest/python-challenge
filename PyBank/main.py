# PyBank
# program to analyze financial records for profits / losses over time

# import path setting, and csv helping
import os
import csv

# path to data

# set path for input file
# data directory is to levels below program location
financials_csv = os.path.join("..", "..", "Data", "budget-data.csv")

# set path for output file
outfile = os.path.join("..", "..", "Data", "PyBank_Financial_Summary.txt")

# initialize output variables
avg_change=0
greatest_increase_profit=0
greatest_decrease_loss=0

# to keep track of change from month to month
monthly_changes=[]
# to keep track of month of change
monthly_changes_month=[]

with open(financials_csv, 'r') as csvfile:
    # split the data
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the headers
    next(csvreader)
    # read file into dictionary, in retrospect this was not the best descision
    month_profit=dict(csvreader)

    # collect monthly proffits
    profits=list(month_profit.values())
    months=list(month_profit.keys())
    profits=list(map(int, profits))

    # 
    for i in range(len(profits)-1):
        # collect change from month to month in profits
        monthly_changes.append(profits[i+1]-profits[i])
        monthly_changes_month.append(months[i])
        

    # find the largest profits/losses
    # increase
    greatest_increase_profit=max(monthly_changes)
    greatest_increase_month_index=monthly_changes.index(greatest_increase_profit)
    greatest_increase_month=months[greatest_increase_month_index+1]
    # decrease
    greatest_decrease_loss=min(monthly_changes)
    greatest_decrease_month_index=monthly_changes.index(greatest_decrease_loss)
    greatest_decrease_month=months[greatest_decrease_month_index+1]

    # find average change in profits
    avg_change=sum(monthly_changes)/len(monthly_changes)

    # find total sum of profits
    net_total=sum(profits)
    

# print to terminal
print("Financial Analysis")
print("________________________________________________")
#length of dictionary is total months, 1 per row
print("Total Months: " + str(len(month_profit))) 
print(f"Net Profits: ${net_total}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase: {greatest_increase_month} (${greatest_increase_profit})")
print(f"Greatest Decrease: {greatest_decrease_month} (${greatest_decrease_loss})")

# print to file
with open(outfile,"w") as file:
    file.write("Financial Analysis\n")
    file.write("________________________________________________\n")
    file.write("Total Months: " + str(len(month_profit)))
    file.write("\n")
    file.write(f"Net Profits: ${net_total}\n")
    file.write(f"Average Change: ${round(avg_change,2)}\n")
    file.write(f"Greatest Increase: {greatest_increase_month} (${greatest_increase_profit})\n")
    file.write(f"Greatest Decrease: {greatest_decrease_month} (${greatest_decrease_loss})")