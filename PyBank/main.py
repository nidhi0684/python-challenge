import csv
import os
import inspect

rows = []

# Fetch the directory path where this python script is located. It will avoid FileNotFoundError 
# when the script is run from any directory on terminal.
script_directory = os.path.dirname(os.path.abspath(
  inspect.getfile(inspect.currentframe())))

# Read input csv file
csvpath = os.path.join(script_directory, "Resources", "budget_data.csv")
with open(csvpath, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    total = 0
    months = 0
    previous = 0
    plChangeList = []
    totalChange = 0.0
    avgChange = 0.00
    greatestProfit = 0
    greatestLoss = 0
    greatestLossDate = ""
    greatestProfitDate = ""

    # Loop through all the csv data
    for row in csvreader:
        rows.append(row)

        # Calculate Total Profit/Loss
        total = total + int(row.__getitem__(1))

        # Create a list to help calculate the average change in profit/Loss over the given period
        plChangeList.append([row.__getitem__(0), float(row.__getitem__(1)) - previous])
        previous = float(row.__getitem__(1))

    # Calculate the average change, the greatest profit and greatest loss over the given period
    i = 0  # to ignore first value
    for amount in plChangeList:
        if i > 0:
            totalChange = totalChange + amount.__getitem__(1)
        i += 1
        if amount.__getitem__(1) > greatestProfit:
            greatestProfit = int(amount.__getitem__(1))
            greatestProfitDate = amount.__getitem__(0)

        if amount.__getitem__(1) < greatestLoss:
            greatestLoss = int(amount.__getitem__(1))
            greatestLossDate = amount.__getitem__(0)

    avgChange = totalChange / (len(plChangeList)-1)

# Count of number of months
months = len(rows)

# Print results on the console/terminal
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {months}\n")
print(f"Total: ${total}\n")
print(f"Average Change: ${round(avgChange, 2)}\n")
print(f"Greatest Increase in Profits: {greatestProfitDate} (${greatestProfit})\n")
print(f"Greatest Decrease in Profits: {greatestLossDate} (${greatestLoss})\n")

# Print results in the output text file
outputPath = os.path.join(script_directory, "analysis", "output.txt")

with open(outputPath, 'w') as file:
    file.write("Financial Analysis \n\n")
    file.write("---------------------------- \n\n")
    file.write(f"Total Months: {months}\n\n")
    file.write(f"Total: ${total}\n\n")
    file.write(f"Average Change: ${round(avgChange, 2)}\n\n")
    file.write(f"Greatest Increase in Profits: {greatestProfitDate} (${greatestProfit})\n\n")
    file.write(f"Greatest Decrease in Profits: {greatestLossDate} (${greatestLoss})\n\n")
    file.close()

