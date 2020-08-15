#PyPoll.py
# Add dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and Candidate Votes.
candidate_options = []
   # Declare an empty dictionary for Candidate Votes.
candidate_votes = {}

# Tracking the Winning: Candidate, Vote Count, and Percentage Vote.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that Candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote to that Candidate's count.
        candidate_votes[candidate_name] += 1
    
    # Determine % of votes for ea candidate with a for loop thru the counts.
    # iterate thru the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count for a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate % of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print out each candidate's name, vote count, and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate.
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

# Print out the winning candidate, vote count and percentage to terminal.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


        # Print the candidate name and % of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")


# Print the candidate list.    
#print(candidate_options)


# Print the Candidate Vote dictionary.
#print(candidate_votes)

