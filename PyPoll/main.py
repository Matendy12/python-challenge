import csv
import os

# Function to analyze election data and export results
def analyze_and_export(file_path, output_path):
    # Initialize variables
    total_votes = 0
    candidates = {}
    
    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skip the header row
        header = next(csvreader)

        # Iterate through rows in the CSV
        for row in csvreader:
            # Extract candidate from the current row
            candidate = row[2]

            # Update total votes
            total_votes += 1

            # Update candidate's vote count
            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

    # Determine the winner
    winner = max(candidates, key=candidates.get)

    # Prepare the analysis results
    analysis_results = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_votes}",
        "-------------------------"
    ]

    # Calculate and print the percentage of votes each candidate won
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        analysis_results.append(f"{candidate}: {percentage:.3f}% ({votes})")

    # Append the winner to the results
    analysis_results.append("-------------------------")
    analysis_results.append(f"Winner: {winner}")
    analysis_results.append("-------------------------")

    # Print the analysis results to the terminal
    for result in analysis_results:
        print(result)

    # Export the analysis results to a text file
    with open(output_path, 'w') as output_file:
        for result in analysis_results:
            output_file.write(result + '\n')

# Specify the file paths
file_path = os.path.join("C:\\Users\\LabUser\\Documents\\python-challenge\\PyPoll\\Resources", "election_data.csv")
output_path = os.path.join("C:\\Users\\LabUser\\Documents\\python-challenge\\PyPoll\\Analysis", "analysis")

# Call the function with the specified file paths
analyze_and_export(file_path, output_path)
