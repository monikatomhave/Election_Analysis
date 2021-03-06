# Add our dependencies.
import csv
import os
#assign a variable for the file to load the path. 3.4.2
#path to access CSV file if not in the same folder
#Resources\election_results.csv
#path to file in same folder
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = "Election_Analysis\Resources\election_results.csv"
#create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Election_Analysis\analysis", "Election_Analysis\analysis\election_analysis.txt")
file_to_save = "C:/Users/butte/Classwork/Election_Analysis/analysis/election_analysis.txt"

#1.) Initilize a total vote counter
total_votes = 0

#new list to hold candidate names
candidate_options = []
#new dictionary to hold candidate votes
candidate_votes = {}

#winning candidate and winning vote count and percentge tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Using the open() function with the "w" mode we will write data to the file path
#open(file_to_save, "w")
#open the election results and read the file
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
#read the file object with the reader function
    file_reader = csv.reader(election_data)
#read and Print the header row
    headers = next(file_reader)
    #print(headers)#test for checking code

    for row in file_reader:
#print each row in the CSV file
    #2.) Add to the total vote count
        total_votes += 1
        #print(row)
   # print(election_data)
    #close the file
    #election_data.close()
        candidate_name = row[2]
        #add candidate name to the list, if matches do not add
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #add count out of if statement but in for loop
        candidate_votes[candidate_name] += 1
#        candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes}
#saving data to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\n Election Results \n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end = "")
    txt_file.write(election_results)

#3.) print the total votes 
#print(f"Total votes:  {total_votes}")#testing code
#print candidte names
#print(candidate_options)#testing code
#print(candidate_votes)#testing code

#perentage of vote calculation and print out
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) *100
    candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)
    with open(file_to_save, "a") as txt_file:
        txt_file.write(candidate_results)
    #print out each candidate name, vote count, and percentage of votes
    #print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,.0f})\n")
    #determint winning vote count and candidate
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
#print(f"Winning candidiate is {winning_candidate} with {winning_count:,.0f} votes and overall {winning_percentage:.1f}% of the vote.")
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)
with open(file_to_save, "a") as txt_file:
    txt_file.write(winning_candidate_summary)