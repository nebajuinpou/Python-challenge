import os
import sys
import csv
csvpath = os.path.join("Resources" ,"budget_data.csv" )
total_months = 0
total_amount = 0
average_change = 0
total_change = 0
greatest_decrease =[]
dates = []
current_amount=[]
Final_amount =[]
months =[]
with open (csvpath, newline="") as csvfile :
    csvreader = csv.reader(csvfile, delimiter = "," )
    headers = next(csvreader)
    print(f"next(csvreader) returns : {headers}")
    for row in csvreader:
        total_months = total_months + 1
        months.append(row[0])
        total_amount =total_amount+ int(row[1])
        current_amount.append(int(row[1]))
        Final_amount.append(int(row[1]))
    del(Final_amount[0])
    del(current_amount[total_months-1])
    changes=[m - n for m,n in zip(current_amount, Final_amount)]
    average_change = sum(changes)/(total_months - 1)
    other_changes=[(m , n) for m,n in zip(months,changes )]
    greatest_date = [x for x,y in other_changes if y==max(changes)]
    least_date = [x for x,y in other_changes if y==min(changes)]
print("Financial Analysis")
print("-------------------------")
print ("Total Months: "+str(total_months))
print ("Total_amount: "+str(total_amount))
print ("Average_change: "+str(average_change))
print ("Greatest_date: "+str(greatest_date))
print ("Greatest Decrease in Profits: "+str(least_date)+" "+str(min(changes)))
print ("Greatest Increase in Profits: "+str(greatest_date)+" "+str(max(changes)))
sys.stdout.close()
sys.stdout=stdoutOrigin