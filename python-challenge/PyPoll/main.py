import csv
import os

election_data_csv = "/Users/emelyzelaya/Desktop/Data-Analyst/python-challenge/PyPoll/Resources/election_data.csv"
output_directory = "/Users/emelyzelaya/Desktop/Data-Analyst/python-challenge/PyPoll/analysis"
textfile = "ElectionsResults.txt"

# Read the election data from the CSV file
with open(election_data_csv, "r") as f:
    reader = csv.reader(f)
    data = list(reader)

# Calculate the total number of votes cast
total_votes = len(data)

# Create a dictionary to store the candidate names and their vote counts
candidate_votes = {}
for row in data:
    candidate = row[2]
    if candidate not in candidate_votes:
        candidate_votes[candidate] = 0
    candidate_votes[candidate] += 1

# Calculate the total number of votes each candidate won
candidate_total_votes = {}
for candidate, vote_count in candidate_votes.items():
    candidate_total_votes[candidate] = vote_count

# Calculate the percentage of votes each candidate won with three decimal places
candidate_percentages = {}
for candidate, vote_count in candidate_votes.items():
    percentage = (vote_count / total_votes) * 100
    candidate_percentages[candidate] = round(percentage, 3)

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Set the output path for the text file
text_path = os.path.join(output_directory, textfile)

# Export the results to a text file
with open(text_path, "w") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, percentage in candidate_percentages.items():
        if percentage != 0:  # Exclude candidates with 0 votes
            f.write(f"{candidate}: {percentage:.3f}% ({candidate_total_votes[candidate]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in candidate_percentages.items():
    if percentage != 0:  # Exclude candidates with 0 votes
        print(f"{candidate}: {percentage:.3f}% ({candidate_total_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
