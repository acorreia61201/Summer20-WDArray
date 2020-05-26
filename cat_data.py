'''
This script is to be run manually from each of the mass directories after receiving results from each of the models. When executed, this script will concatenate
the history.data files from each of the three segments of every model and create a new file, "full_history.data," within the model directories. If one or both of the 
latter two history files is missing, the script will instead add to a counter that will report how many failed models there are in a given directory.
'''

import os

counter = 0
models = [f for f in os.listdir('.') if os.path.isdir(f)]

for model in models:
	#cd to each of the model directories
	os.chdir(model)
	
	#check if the model progressed to WD; otherwise, continue the loop without doing anything        
	if os.path.exists("controls/LOGS_part2/history.data") and os.path.exists("controls/LOGS_part3/history.data"):
		#make new history files omitting the first few lines
		os.system("tail -n +7 controls/LOGS_part2/history.data > history2.data")
		os.system("tail -n +7 controls/LOGS_part3/history.data > history3.data")
		
		#concatenate the results from each controls directory to the model directory
	        os.system("cat controls/LOGS_part1/history.data controls/LOGS_part2/history2.data controls/LOGS_part3/history3.data >> full_history.data")
		os.chdir("..")
	else:
		counter = counter + 1
		os.chdir("..")

print(counter)
