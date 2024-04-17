import os
import csv
# Set the path for the CSV file
PyBankcsv = os.path.join("resources","budget_data.csv")

# Create lists to store data
margins = []
monthly_changes = []
date = []

# Initialize variables
count = 0
total_margins = 0
total_change_margins = 0
initial_margins = 0

# Open the CSV file
with open(PyBankcsv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Count the number of months
        count += 1

        # Append margins information and calculate total margins
        date.append(row[0])
        margins.append(int(row[1]))
        total_margins += int(row[1])

        # Calculate the monthly change in margins
        final_margins = int(row[1])
        monthly_change_margins = final_margins - initial_margins

        # Store monthly changes in a list
        monthly_changes.append(monthly_change_margins)

        total_change_margins += monthly_change_margins
        initial_margins = final_margins

    # Calculate the average change in margins
    average_change_margins = total_change_margins / (count - 1)

    # Find the greatest increase and decrease in margins
    greatest_increase_margins = max(monthly_changes)
    greatest_decrease_margins = min(monthly_changes)

    increase_date = date[monthly_changes.index(greatest_increase_margins)]
    decrease_date = date[monthly_changes.index(greatest_decrease_margins)]

    # Print the financial analysis
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total margins: $" + str(total_margins))
    print("Average Change: $" + str(round(average_change_margins, 2)))
    print("Greatest Increase in margins: " + increase_date + " ($" + str(greatest_increase_margins) + ")")
    print("Greatest Decrease in margins: " + decrease_date + " ($" + str(greatest_decrease_margins) + ")")
    print("----------------------------------------------------------")

    # Write the results to a text file
    with open('financial_analysis.txt', 'w') as text:
        text.write("----------------------------------------------------------\n")
        text.write("  Financial Analysis\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(count) + "\n")
        text.write("    Total margins: $" + str(total_margins) + "\n")
        text.write("    Average Change: $" + str(round(average_change_margins, 2)) + "\n")
        text.write("    Greatest Increase in margins: " + increase_date + " ($" + str(greatest_increase_margins) + ")\n")
        text.write("    Greatest Decrease in margins: " + decrease_date + " ($" + str(greatest_decrease_margins) + ")\n")
        text.write("----------------------------------------------------------\n")

   
