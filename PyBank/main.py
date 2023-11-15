import csv
import os

# Function to analyze financial data and export results
def analyze_and_export(file_path, output_path):
    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    dates = []

    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skip the header row
        header = next(csvreader)

        # Iterate through rows in the CSV
        for row in csvreader:
            # Extract date and profit/loss from the current row
            date = row[0]
            profit_loss = int(row[1])

            # Calculate total months and net total
            total_months += 1
            net_total += profit_loss

            # Calculate change in profit/loss and store values
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                dates.append(date)

            # Update previous profit/loss for the next iteration
            previous_profit_loss = profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes)

    # Find the greatest increase and decrease in profits
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
    
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]

    # Prepare the analysis results
    analysis_results = [
        "Financial Analysis",
        "-----------------------------",
        f"Total Months: {total_months}",
        f"Total: ${net_total}",
        f"Average Change: ${average_change:.2f}",
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})",
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
    ]

    # Print the analysis results to the terminal
    for result in analysis_results:
        print(result)

    # Export the analysis results to a text file
    with open(output_path, 'w') as output_file:
        for result in analysis_results:
            output_file.write(result + '\n')

# Specify the file paths
file_path = os.path.join("C:\\Users\\LabUser\\Documents\\python-challenge\\PyBank\\Resources", "budget_data.csv")
output_path = "C:\\Users\\LabUser\\Documents\\python-challenge\\PyBank\\Analysis\\financial_analysis.txt"


# Call the function with the specified file paths
analyze_and_export(file_path, output_path)
