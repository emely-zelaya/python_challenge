import os
import csv

budget_data_csv = os.path.join("/Users/emelyzelaya/Desktop/Data-Analyst/python-challenge/PyBank/Resources/budget_data.csv")
output_directory = "/Users/emelyzelaya/Desktop/Data-Analyst/python-challenge/PyBank/analysis"
textfile = "financial_analysis.txt"

# Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

# Open the csv file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    # Loop through to find total months and perform calculations
    for row in csvreader:
        # Count the total of months
        total_months += 1

        # Calculate the total revenue over the entire period
        total_revenue += int(row[1])

        # Calculate the average change in revenue between months over the entire period
        revenue_change = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
        revenue_change_list.append(revenue_change)
        month_of_change.append(row[0])

        # Find the greatest increase in revenue (date and amount) over the entire period
        if revenue_change > greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        # Find the greatest decrease in revenue (date and amount) over the entire period
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]

    # Calculate the average revenue change
    if len(revenue_change_list) > 1:
        revenue_average = sum(revenue_change_list[1:]) / (len(revenue_change_list) - 1)
    else:
        revenue_average = 0  # Set a default value in case there's insufficient data for the average

# Set the output of the text file
text_path = os.path.join(output_directory, textfile)

# Write changes to a text file
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total Revenue: ${total_revenue}\n")
    file.write(f"Average Revenue Change: ${revenue_average:.2f}\n")
    file.write(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the analysis to the terminal
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${revenue_average:.2f}")
print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})")

print("Analysis has been saved to:", text_path)