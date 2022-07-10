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
file_to_save = "Election_Analysis\analysis\election_analysis.txt"
#Using the open() function with the "w" mode we will write data to the file path
#open(file_to_save, "w")
#open the election results and read the file
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
#read the file object with the reader function
    file_reader = csv.reader(election_data)
#Print the header row
    headers = next(file_reader)
    print(headers)

#for row in file_reader:
#    print(row)
   # print(election_data)
    #close the file
    #election_data.close()

#open the election results and read the file
#with open(file_to_load) as election_data:
    #print the file object
#   print(election_data)
#test to see if the file can be written to
#with open(file_to_save, "w") as text_file:
#    text_file.write("Hello World") 
#    print(text_file)
   
#perform analysis
# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popualr vote 