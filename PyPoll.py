#The Data we need to retreive
#Add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")
#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)

#Print each row in the CSV file


#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")


#Write some data to the file
with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of cotes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the electino based on popular vote