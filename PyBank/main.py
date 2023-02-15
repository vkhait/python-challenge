import os
import csv

#specify the path to read the file

budget_csv = os.path.join('Resources','budget_data.csv')
output_file = os.path.join('analysis', 'budget_analysis.txt')
#open csv file

with open(budget_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

#using next

        csv_header = next(csv_file)
        csv_list = list(csv_reader)
        
        #print(f'header:{csv_header}')
        print("Financial Analysis")
        print("----------------------------")

#sum up the total months
#sum up the net change

        
        

        total_net = sum(int(row[1]) for row in csv_list)
        

#assign file variables

        
        months = []
        change_list = []
        current = 0
        previous = 0
        x_change = 0
        
#loop through rows to calculate the difference between each current cell with the previous cell
        
        for row in csv_list:
                
                
                current = int(row[1]) 
                
                
                if row == 1:
                    
                
                        previous = current
                
                else:
                        
                        
                        months.append(row[0])
                        change_list.append(int(current-previous))
                        
                        previous = int(row[1])
                        
                   #Calculate greatest increase and decrease in profits with max function     
                        
                        x_max = max(change_list)
                        x_min = min(change_list)
                        
                        
                        maxMonth_index = change_list.index(x_max)
                        minMonth_index = change_list.index(x_min)
                        
                        MaxMonth = months[maxMonth_index]
                        MinMonth = months[minMonth_index]
               
            #find the average of changes
                        
                        
        av_count = int(len(csv_list)-1)
            
        x_average = float(sum(change_list[1:]) / av_count)
        y_average = round(x_average, 2)

txt_output = (
        f"Analysis\n"
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Months : {len(csv_list)}\n"
        f"Total : ${total_net}\n"
        f"Average Change : $ {y_average}\n"
        f"Greatest Increase in Profits:  {MaxMonth} (${x_max})\n"
        f"Greatest Decrease in Profits:  {MinMonth} (${x_min})\n"
)


print(txt_output)

with open (output_file,"w") as txt_file:
        txt_file.write(txt_output)


#print the results
# print(f"Total Months : {len(csv_list)}")
# print(f"Total : ${total_net}")
# print(f"Average Change : $ {y_average}")
# print(f"Greatest Increase in Profits:  {MaxMonth} (${x_max})")
# print(f"Greatest Decrease in Profits:  {MinMonth} (${x_min})")

