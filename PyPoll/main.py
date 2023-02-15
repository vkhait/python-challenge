import os
import csv

#path
election_data = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('analysis', 'election_analysis.txt')
#open csv file

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    

    #set up variables
    total_votes = 0
    candidates = []
    vote_number = []
    candidates_dict = {}
    vote_percent = []
    winning_count = 0
    winning_candidate = ""
    
    #skip header
    
    csv_header = next(csv_file)
    #print(f'header:{csv_header}')

    print("Election Results")
    print("-------------------------")

#loop through data row by row

    for row in csv_reader:

        #calculate total number of votes
        total_votes = total_votes + 1
        
        

        #names of candidates location
        name_candidate = row[2]
        

        #grab candidate names using if in function and update vote stats
        
        if name_candidate not in candidates:
            
            #define the name of the candidate and add to vote number
            candidates.append(name_candidate)
            candidates_dict[name_candidate] = 0
           
        
        candidates_dict[name_candidate] = candidates_dict[name_candidate] + 1
        
    print(f"Total Votes :{total_votes}")
    print("-------------------------")
    
    for name in candidates_dict:
            
        votes = candidates_dict.get(name)
         
        #calculate the percentage and the winning votes
        
        vote_percentage = votes/total_votes*100
        vote_percentage = round(vote_percentage, 2)    
        if (votes > winning_count):
                
            winning_count = votes
            winning_candidate = name
            
        print(f"{name}: {vote_percentage}% {votes}")
        
    txt_output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes :{total_votes}\n"
        
        
        
        f"Winner: {winning_candidate}\n"
        f"---------------------------\n"
    )

    print("---------------------------")
    print(f"Winner: {winning_candidate}")
    print("---------------------------")

print(txt_output)



with open (output_file,"w") as txt_file:
    txt_file.write(txt_output)

