import os
import csv

# Set the path for the CSV file
PyPollcsv = os.path.join("resources", "election_data.csv")

# Create lists to store data
count = 0
partcipant_list = []
unique_partcipant = []
vote_count = []
vote_percent = []

# Open the CSV file
with open(PyPollcsv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Process the data
    for row in csvreader:
        count += 1
        partcipant_list.append(row[2])

    # Calculate unique partcipants
    unique_partcipant = list(set(partcipant_list))

    # Calculate vote count and percentage
    for partcipant in unique_partcipant:
        votes = partcipant_list.count(partcipant)
        vote_count.append(votes)
        vote_percent.append((votes / count) * 100)

    # Find the winner
    max_votes = max(vote_count)
    winner_index = vote_count.index(max_votes)
    winner = unique_partcipant[winner_index]

    # Print results
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")
    for i in range(len(unique_partcipant)):
        print(f"{unique_partcipant[i]}: {vote_percent[i]:.3f}% ({vote_count[i]})")
    print("-------------------------")
    print(f"The winner is: {winner}")
    print("-------------------------")

    # Write results to a text file
    with open('election_results.txt', 'w') as text:
        text.write("Election Results\n")
        text.write("---------------------------------------\n")
        text.write(f"Total Votes: {count}\n")
        text.write("---------------------------------------\n")
        for i in range(len(unique_partcipant)):
            text.write(f"{unique_partcipant[i]}: {vote_percent[i]:.3f}% ({vote_count[i]})\n")
        text.write("---------------------------------------\n")
        text.write(f"The winner is: {winner}\n")
        text.write("---------------------------------------\n")